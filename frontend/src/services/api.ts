import {
  Ingredient,
  CombinationAnalysis,
  SelectedIngredient,
  VisionIdentifyResponse,
  Recipe,
  RecommendationItem,
  User,
  UserPreferences,
  AssistantChatResponse
} from '../types';

const API_BASE = (import.meta.env.VITE_API_BASE || '/api').replace(/\/$/, '');

function getAuthHeader(): Record<string, string> {
  const token = localStorage.getItem('flavorfusion_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    let errorDetail = 'An error occurred';
    try {
      const errJson = await res.json();
      errorDetail = errJson.detail || errJson.message || errorDetail;
    } catch {
      errorDetail = res.statusText || errorDetail;
    }
    throw new Error(errorDetail);
  }
  return res.json();
}

export const api = {
  // Authentication
  auth: {
    async register(data: { email: string; password: string; full_name?: string }) {
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const result = await handleResponse<{ access_token: string; user: User }>(res);
      localStorage.setItem('flavorfusion_token', result.access_token);
      localStorage.setItem('flavorfusion_user', JSON.stringify(result.user));
      return result;
    },

    async login(data: { email: string; password: string }) {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const result = await handleResponse<{ access_token: string; user: User }>(res);
      localStorage.setItem('flavorfusion_token', result.access_token);
      localStorage.setItem('flavorfusion_user', JSON.stringify(result.user));
      return result;
    },

    async getMe(): Promise<User | null> {
      const token = localStorage.getItem('flavorfusion_token');
      if (!token) return null;
      try {
        const res = await fetch(`${API_BASE}/auth/me`, {
          headers: getAuthHeader(),
        });
        const user = await handleResponse<User>(res);
        localStorage.setItem('flavorfusion_user', JSON.stringify(user));
        return user;
      } catch {
        localStorage.removeItem('flavorfusion_token');
        localStorage.removeItem('flavorfusion_user');
        return null;
      }
    },

    logout() {
      localStorage.removeItem('flavorfusion_token');
      localStorage.removeItem('flavorfusion_user');
    },

    getCurrentUser(): User | null {
      const raw = localStorage.getItem('flavorfusion_user');
      return raw ? JSON.parse(raw) : null;
    }
  },

  // Ingredients
  ingredients: {
    async getAll(params?: { category?: string; cuisine?: string; exclude_allergen?: string }): Promise<Ingredient[]> {
      const search = new URLSearchParams();
      if (params?.category) search.set('category', params.category);
      if (params?.cuisine) search.set('cuisine', params.cuisine);
      if (params?.exclude_allergen) search.set('exclude_allergen', params.exclude_allergen);
      const res = await fetch(`${API_BASE}/ingredients?${search.toString()}`);
      return handleResponse<Ingredient[]>(res);
    },

    async search(query: string): Promise<Ingredient[]> {
      const res = await fetch(`${API_BASE}/ingredients/search?q=${encodeURIComponent(query)}`);
      return handleResponse<Ingredient[]>(res);
    },

    async getById(id: number): Promise<Ingredient> {
      const res = await fetch(`${API_BASE}/ingredients/${id}`);
      return handleResponse<Ingredient>(res);
    },

    async create(data: Partial<Ingredient>): Promise<Ingredient> {
      const res = await fetch(`${API_BASE}/ingredients`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(data),
      });
      return handleResponse<Ingredient>(res);
    }
  },

  // Flavor Lab & Analysis
  combinations: {
    async analyze(ingredients: SelectedIngredient[], title?: string): Promise<CombinationAnalysis> {
      const res = await fetch(`${API_BASE}/combinations/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify({ ingredients, title }),
      });
      return handleResponse<CombinationAnalysis>(res);
    },

    async getById(id: number): Promise<CombinationAnalysis> {
      const res = await fetch(`${API_BASE}/combinations/${id}`);
      return handleResponse<CombinationAnalysis>(res);
    },

    async save(prediction_id: number, custom_title?: string, notes?: string, tags?: string[]) {
      const res = await fetch(`${API_BASE}/combinations/save`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify({ prediction_id, custom_title, notes, tags }),
      });
      return handleResponse(res);
    },

    async getSaved() {
      const res = await fetch(`${API_BASE}/combinations/user/saved`, {
        headers: getAuthHeader(),
      });
      return handleResponse<any[]>(res);
    },

    async deleteSaved(id: number) {
      const res = await fetch(`${API_BASE}/combinations/user/saved/${id}`, {
        method: 'DELETE',
        headers: getAuthHeader(),
      });
      if (!res.ok) throw new Error('Failed to delete saved combination');
      return true;
    }
  },

  // Vision / Ingredient Identification
  vision: {
    async identify(file: File): Promise<VisionIdentifyResponse> {
      const formData = new FormData();
      formData.append('file', file);
      const res = await fetch(`${API_BASE}/vision/identify`, {
        method: 'POST',
        headers: getAuthHeader(),
        body: formData,
      });
      return handleResponse<VisionIdentifyResponse>(res);
    },

    async confirm(confirmed_ingredients: string[]) {
      const res = await fetch(`${API_BASE}/vision/confirm`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify({ confirmed_ingredients }),
      });
      return handleResponse(res);
    }
  },

  // Recommendations
  recommendations: {
    async getPersonalized(params?: { cuisine?: string; novelty?: string; limit?: number }): Promise<RecommendationItem[]> {
      const search = new URLSearchParams();
      if (params?.cuisine) search.set('cuisine', params.cuisine);
      if (params?.novelty) search.set('novelty', params.novelty);
      if (params?.limit) search.set('limit', params.limit.toString());
      const res = await fetch(`${API_BASE}/recommendations/personalized?${search.toString()}`, {
        headers: getAuthHeader(),
      });
      return handleResponse<RecommendationItem[]>(res);
    },

    async submitFeedback(data: { combination_name: string; ingredients: string[]; score: number; comment?: string; liked: boolean }) {
      const res = await fetch(`${API_BASE}/recommendations/feedback`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(data),
      });
      return handleResponse(res);
    }
  },

  // Recipes
  recipes: {
    async getCatalog(params?: { q?: string; cuisine?: string; meal_type?: string; difficulty?: string }): Promise<Recipe[]> {
      const search = new URLSearchParams();
      if (params?.q) search.set('q', params.q);
      if (params?.cuisine) search.set('cuisine', params.cuisine);
      if (params?.meal_type) search.set('meal_type', params.meal_type);
      if (params?.difficulty) search.set('difficulty', params.difficulty);
      const res = await fetch(`${API_BASE}/recipes/catalog?${search.toString()}`, {
        headers: getAuthHeader(),
      });
      return handleResponse<Recipe[]>(res);
    },

    async getCatalogById(id: number): Promise<Recipe> {
      const res = await fetch(`${API_BASE}/recipes/catalog/${id}`, {
        headers: getAuthHeader(),
      });
      return handleResponse<Recipe>(res);
    },

    async generate(data: {
      ingredients?: SelectedIngredient[];
      prediction_id?: number;
      cuisine?: string;
      meal_type?: string;
      servings?: number;
      prefer_quick?: boolean;
      prefer_no_cook?: boolean;
    }): Promise<Recipe> {
      const res = await fetch(`${API_BASE}/recipes/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(data),
      });
      return handleResponse<Recipe>(res);
    },

    async getById(id: number): Promise<Recipe> {
      const res = await fetch(`${API_BASE}/recipes/${id}`);
      return handleResponse<Recipe>(res);
    },

    async toggleSave(id: number) {
      const res = await fetch(`${API_BASE}/recipes/${id}/save`, {
        method: 'POST',
        headers: getAuthHeader(),
      });
      return handleResponse<{ id: number; is_saved: boolean; message: string }>(res);
    },

    async getSaved(): Promise<Recipe[]> {
      const res = await fetch(`${API_BASE}/recipes/user/saved`, {
        headers: getAuthHeader(),
      });
      return handleResponse<Recipe[]>(res);
    },

    async toggleWishlist(id: number) {
      const res = await fetch(`${API_BASE}/recipes/${id}/wishlist`, {
        method: 'POST',
        headers: getAuthHeader(),
      });
      return handleResponse<{ id: number; is_wishlisted: boolean; message: string }>(res);
    },

    async getWishlist(): Promise<Recipe[]> {
      const res = await fetch(`${API_BASE}/recipes/user/wishlist`, {
        headers: getAuthHeader(),
      });
      return handleResponse<Recipe[]>(res);
    }
  },

  // User Preferences & Dashboard
  users: {
    async getPreferences(): Promise<UserPreferences> {
      const res = await fetch(`${API_BASE}/users/preferences`, {
        headers: getAuthHeader(),
      });
      return handleResponse<UserPreferences>(res);
    },

    async updatePreferences(pref: Partial<UserPreferences>): Promise<UserPreferences> {
      const res = await fetch(`${API_BASE}/users/preferences`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(pref),
      });
      return handleResponse<UserPreferences>(res);
    },

    async getDashboard(): Promise<any> {
      const res = await fetch(`${API_BASE}/users/dashboard`, {
        headers: getAuthHeader(),
      });
      return handleResponse(res);
    }
  },

  // Ratings
  ratings: {
    async submit(data: { score: number; comment?: string; combination_id?: number; recipe_id?: number; would_make_again?: boolean }) {
      const res = await fetch(`${API_BASE}/ratings`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(data),
      });
      return handleResponse(res);
    },

    async getAll() {
      const res = await fetch(`${API_BASE}/ratings`, {
        headers: getAuthHeader(),
      });
      return handleResponse<any[]>(res);
    }
  },

  // Admin
  admin: {
    async getStats() {
      const res = await fetch(`${API_BASE}/admin/stats`, {
        headers: getAuthHeader(),
      });
      return handleResponse<any>(res);
    },

    async getFeedback() {
      const res = await fetch(`${API_BASE}/admin/feedback`, {
        headers: getAuthHeader(),
      });
      return handleResponse<any[]>(res);
    },

    async deleteIngredient(id: number) {
      const res = await fetch(`${API_BASE}/admin/ingredients/${id}`, {
        method: 'DELETE',
        headers: getAuthHeader(),
      });
      if (!res.ok) throw new Error('Failed to delete ingredient');
      return true;
    }
  },

  // AI Assistant ("Chef Fusion AI")
  assistant: {
    async chat(data: { message: string; current_ingredients?: string[] }): Promise<AssistantChatResponse> {
      const res = await fetch(`${API_BASE}/assistant/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeader(),
        },
        body: JSON.stringify(data),
      });
      return handleResponse<AssistantChatResponse>(res);
    }
  }
};
