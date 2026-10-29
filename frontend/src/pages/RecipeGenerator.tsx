import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import {
  BookOpen,
  Printer,
  Bookmark,
  Share2,
  Clock,
  Users,
  ChefHat,
  Sparkles,
  AlertTriangle,
  Check,
  RefreshCw,
  Plus,
  ArrowLeft,
  Heart,
  UtensilsCrossed,
  ShoppingBag,
  Flame
} from 'lucide-react';
import { api } from '../services/api';
import { Recipe, SelectedIngredient } from '../types';

export const RecipeGenerator: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();

  // Location state can pass preselected ingredients or prediction
  const incomingIngredients: SelectedIngredient[] = location.state?.ingredients || [];
  const incomingTitle: string = location.state?.title || '';

  const [ingredients, setIngredients] = useState<SelectedIngredient[]>(incomingIngredients);
  const [recipe, setRecipe] = useState<Recipe | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Configuration options
  const [servings, setServings] = useState(2);
  const [cuisine, setCuisine] = useState('Fusion');
  const [mealType, setMealType] = useState('Dinner');
  const [preferNoCook, setPreferNoCook] = useState(false);
  const [preferQuick, setPreferQuick] = useState(false);
  const [savedSuccess, setSavedSuccess] = useState(false);
  const [wishlistSuccess, setWishlistSuccess] = useState(false);

  useEffect(() => {
    if (ingredients.length > 0) {
      handleGenerate();
    }
  }, []);

  const handleGenerate = async () => {
    if (ingredients.length === 0) {
      setError('Please add at least one ingredient to generate a recipe.');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const generated = await api.recipes.generate({
        ingredients,
        servings,
        cuisine,
        meal_type: incomingTitle || mealType,
        prefer_no_cook: preferNoCook,
        prefer_quick: preferQuick,
      });
      setRecipe(generated);
    } catch (err: any) {
      setError(err.message || 'Error generating recipe');
    } finally {
      setLoading(false);
    }
  };

  const handleToggleSave = async () => {
    if (!recipe?.id) return;
    try {
      const res = await api.recipes.toggleSave(recipe.id);
      setRecipe((prev) => (prev ? { ...prev, is_saved: res.is_saved } : null));
      setSavedSuccess(true);
      setTimeout(() => setSavedSuccess(false), 2000);
    } catch (err: any) {
      alert(err.message || 'Failed to update recipe bookmark');
    }
  };

  const handleToggleWishlist = async () => {
    if (!recipe?.id) return;
    try {
      const res = await api.recipes.toggleWishlist(recipe.id);
      setRecipe((prev) => (prev ? { ...prev, is_wishlisted: res.is_wishlisted } : null));
      setWishlistSuccess(true);
      setTimeout(() => setWishlistSuccess(false), 2000);
    } catch (err: any) {
      alert(err.message || 'Failed to update recipe wishlist');
    }
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Toast Alert */}
      {savedSuccess && (
        <div className="fixed bottom-6 right-6 z-50 bg-forest-700 text-ivory-50 px-5 py-3 rounded-2xl shadow-xl flex items-center space-x-2 border border-forest-500">
          <Check className="w-4 h-4 text-sage-300" />
          <span className="text-sm font-semibold">Recipe saved to your dashboard!</span>
        </div>
      )}

      {wishlistSuccess && (
        <div className="fixed bottom-6 right-6 z-50 bg-terracotta-700 text-white px-5 py-3 rounded-2xl shadow-xl flex items-center space-x-2 border border-terracotta-500">
          <Heart className="w-4 h-4 fill-current text-white" />
          <span className="text-sm font-semibold">
            {recipe?.is_wishlisted ? 'Added to your Wishlist!' : 'Removed from Wishlist'}
          </span>
        </div>
      )}

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <button
            onClick={() => navigate('/lab')}
            className="flex items-center space-x-1 text-xs font-semibold text-stone-500 dark:text-stone-400 hover:text-forest-700 dark:hover:text-sage-300 mb-2 transition-colors"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Back to Flavor Lab</span>
          </button>
          <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
            Formulated Recipe Generator
          </h1>
          <p className="text-sm text-stone-600 dark:text-stone-300 mt-1">
            Transform validated ingredient combinations into complete step-by-step culinary dishes.
          </p>
        </div>

        {recipe && (
          <div className="flex items-center space-x-2">
            <button
              onClick={handleToggleWishlist}
              className={`flex items-center space-x-1.5 px-3.5 py-2 rounded-xl text-xs font-semibold border transition-all ${
                recipe.is_wishlisted
                  ? 'bg-terracotta-600 text-white border-terracotta-600 shadow-sm'
                  : 'bg-white dark:bg-[#18201d] text-stone-700 dark:text-stone-300 border-ivory-300 dark:border-forest-800 hover:bg-terracotta-50 dark:hover:bg-terracotta-900/30'
              }`}
            >
              <Heart className={`w-4 h-4 ${recipe.is_wishlisted ? 'fill-current text-white' : 'text-terracotta-500'}`} />
              <span>{recipe.is_wishlisted ? 'Wishlisted ❤️' : 'Wishlist'}</span>
            </button>
            <button
              onClick={handleToggleSave}
              className={`flex items-center space-x-1.5 px-3.5 py-2 rounded-xl text-xs font-semibold border transition-all ${
                recipe.is_saved
                  ? 'bg-forest-600 text-white border-forest-600'
                  : 'bg-white dark:bg-[#18201d] text-stone-700 dark:text-stone-300 border-ivory-300 dark:border-forest-800 hover:bg-ivory-100 dark:hover:bg-forest-900'
              }`}
            >
              <Bookmark className="w-4 h-4" />
              <span>{recipe.is_saved ? 'Saved' : 'Save'}</span>
            </button>
            <button
              onClick={handlePrint}
              className="flex items-center space-x-1.5 px-3.5 py-2 rounded-xl bg-white dark:bg-[#18201d] text-stone-700 dark:text-stone-300 border border-ivory-300 dark:border-forest-800 hover:bg-ivory-100 dark:hover:bg-forest-900 text-xs font-semibold shadow-sm transition-all"
            >
              <Printer className="w-4 h-4" />
              <span>Print</span>
            </button>
          </div>
        )}
      </div>

      {/* Controls Card */}
      <div className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-4">
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 text-xs">
          {/* Servings */}
          <div>
            <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Serving Size</label>
            <div className="flex items-center space-x-2">
              <button
                type="button"
                onClick={() => setServings(Math.max(1, servings - 1))}
                className="w-8 h-8 rounded-lg bg-white dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 font-bold hover:bg-ivory-100"
              >
                -
              </button>
              <span className="font-mono text-sm font-bold w-6 text-center text-stone-800 dark:text-ivory-100">{servings}</span>
              <button
                type="button"
                onClick={() => setServings(servings + 1)}
                className="w-8 h-8 rounded-lg bg-white dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 font-bold hover:bg-ivory-100"
              >
                +
              </button>
            </div>
          </div>

          {/* Cuisine */}
          <div>
            <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Cuisine Style</label>
            <select
              value={cuisine}
              onChange={(e) => setCuisine(e.target.value)}
              className="w-full px-3 py-2 rounded-xl bg-white dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs"
            >
              <option value="Fusion">Contemporary Fusion</option>
              <option value="Indian">Traditional Indian</option>
              <option value="Mediterranean">Mediterranean</option>
              <option value="Italian">Italian Regional</option>
              <option value="Mexican">Mexican Inspired</option>
            </select>
          </div>

          {/* Meal Type */}
          <div>
            <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Meal Occasion</label>
            <select
              value={mealType}
              onChange={(e) => setMealType(e.target.value)}
              className="w-full px-3 py-2 rounded-xl bg-white dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs"
            >
              <option value="Dinner">Dinner Main</option>
              <option value="Lunch">Light Lunch</option>
              <option value="Breakfast">Breakfast / Brunch</option>
              <option value="Dessert">Dessert / Sweet Treat</option>
              <option value="Beverage">Infusion / Elixir</option>
            </select>
          </div>

          {/* Toggles */}
          <div className="flex flex-col justify-end space-y-1.5 pt-1">
            <label className="flex items-center space-x-2 cursor-pointer">
              <input
                type="checkbox"
                checked={preferNoCook}
                onChange={(e) => setPreferNoCook(e.target.checked)}
                className="rounded accent-forest-600"
              />
              <span className="text-stone-700 dark:text-stone-300">No-Cook / Fresh</span>
            </label>
            <label className="flex items-center space-x-2 cursor-pointer">
              <input
                type="checkbox"
                checked={preferQuick}
                onChange={(e) => setPreferQuick(e.target.checked)}
                className="rounded accent-forest-600"
              />
              <span className="text-stone-700 dark:text-stone-300">Quick Prep (&lt; 20m)</span>
            </label>
          </div>
        </div>

        <div className="pt-2 flex justify-end">
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="flex items-center space-x-2 px-6 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-xs shadow-sm transition-all disabled:opacity-50"
          >
            {loading ? (
              <>
                <RefreshCw className="w-4 h-4 animate-spin text-sage-200" />
                <span>Formulating Culinary Recipe...</span>
              </>
            ) : (
              <>
                <Sparkles className="w-4 h-4 text-sage-200" />
                <span>Regenerate Recipe ({servings} Servings)</span>
              </>
            )}
          </button>
        </div>
      </div>

      {/* Error state */}
      {error && (
        <div className="p-4 rounded-2xl bg-terracotta-50 dark:bg-terracotta-950/40 border border-terracotta-200 dark:border-terracotta-800 text-terracotta-800 dark:text-terracotta-200 text-xs flex items-center space-x-2">
          <AlertTriangle className="w-4 h-4 text-terracotta-600 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Recipe Presentation Card */}
      {recipe && (
        <article className="bg-white dark:bg-[#151c19] rounded-3xl p-6 sm:p-10 border border-ivory-300 dark:border-forest-900 shadow-sm space-y-8 print:shadow-none print:border-none">
          {/* Header */}
          <div className="border-b border-ivory-200 dark:border-forest-900 pb-6 space-y-3">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[11px] font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2.5 py-1 rounded-md border border-sage-200 dark:border-forest-800">
                {recipe.cuisine} • {recipe.meal_type}
              </span>
              <span className="text-[11px] font-semibold text-stone-500 dark:text-stone-400 bg-ivory-100 dark:bg-[#1d2622] px-2.5 py-1 rounded-md">
                Difficulty: {recipe.difficulty}
              </span>
              <span className="text-[11px] text-stone-400 ml-auto italic">
                Engine: {recipe.generation_mode}
              </span>
            </div>

            <h2 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
              {recipe.title}
            </h2>
            <p className="text-sm text-stone-600 dark:text-stone-300 leading-relaxed max-w-2xl">
              {recipe.summary}
            </p>

            {/* Quick stats strip */}
            <div className="flex flex-wrap items-center gap-6 pt-4 text-xs text-stone-700 dark:text-stone-300 border-t border-ivory-100 dark:border-forest-900 font-medium">
              <div className="flex items-center space-x-2">
                <Clock className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                <span>Prep: <strong>{recipe.prep_time_mins} mins</strong></span>
              </div>
              <div className="flex items-center space-x-2">
                <Flame className="w-4 h-4 text-terracotta-600 dark:text-terracotta-400" />
                <span>Cook: <strong>{recipe.cook_time_mins} mins</strong></span>
              </div>
              <div className="flex items-center space-x-2">
                <ChefHat className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                <span>Total: <strong>{recipe.prep_time_mins + recipe.cook_time_mins} mins</strong></span>
              </div>
              <div className="flex items-center space-x-2">
                <Users className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                <span>Servings: <strong>{recipe.servings} Portions</strong></span>
              </div>
              {recipe.allergens.length > 0 && (
                <div className="text-terracotta-700 dark:text-terracotta-400">
                  Allergen Notice: <strong>{recipe.allergens.join(', ')}</strong>
                </div>
              )}
            </div>

            {/* Required Kitchen Tools & Equipment */}
            {recipe.required_tools && recipe.required_tools.length > 0 && (
              <div className="mt-4 p-4 bg-sage-50/70 dark:bg-forest-950/60 rounded-2xl border border-sage-200 dark:border-forest-800 space-y-2">
                <div className="flex items-center space-x-2 text-forest-800 dark:text-sage-300">
                  <UtensilsCrossed className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                  <span className="font-bold text-xs uppercase tracking-wider">Required Kitchen Tools & Equipment</span>
                </div>
                <div className="flex flex-wrap gap-2 pt-1">
                  {recipe.required_tools.map((tool, idx) => (
                    <span
                      key={idx}
                      className="px-3 py-1.5 rounded-xl bg-white dark:bg-[#1a2320] border border-sage-300 dark:border-forest-700 text-stone-800 dark:text-ivory-100 text-xs font-medium shadow-xs flex items-center space-x-1.5"
                    >
                      <span className="w-1.5 h-1.5 rounded-full bg-forest-500 dark:bg-sage-400"></span>
                      <span>{tool}</span>
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Two column layout: Ingredients on Left, Steps on Right */}
          <div className="grid grid-cols-1 md:grid-cols-12 gap-8">
            {/* Ingredients column */}
            <div className="md:col-span-5 space-y-4">
              <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-100 border-b border-ivory-200 dark:border-forest-900 pb-2">
                Your Ingredients (Scaled)
              </h3>
              <ul className="space-y-2 text-xs divide-y divide-ivory-100 dark:divide-forest-900">
                {recipe.ingredients_list.map((item, idx) => (
                  <li key={idx} className="pt-2 flex items-start justify-between">
                    <div>
                      <span className="font-semibold text-stone-900 dark:text-ivory-100">{item.name}</span>
                      {item.notes && <p className="text-[11px] text-stone-500 dark:text-stone-400">{item.notes}</p>}
                    </div>
                    <span className="font-mono font-bold text-forest-700 dark:text-sage-300 ml-2 whitespace-nowrap">
                      {item.quantity} {item.unit === 'piece' ? (item.quantity === 1 ? 'piece' : 'pieces') : item.unit}
                    </span>
                  </li>
                ))}
              </ul>

              {/* Needed / Additional Ingredients (Pantry Staples & Seasonings) */}
              {recipe.needed_ingredients && recipe.needed_ingredients.length > 0 && (
                <div className="p-4 bg-terracotta-50/90 dark:bg-[#1c1614] rounded-2xl border border-terracotta-200 dark:border-[#3d241c] space-y-2.5 mt-4 shadow-xs">
                  <div className="flex items-center space-x-2 text-terracotta-800 dark:text-terracotta-300">
                    <ShoppingBag className="w-4 h-4 text-terracotta-600 dark:text-terracotta-400" />
                    <span className="font-bold text-xs uppercase tracking-wider">Needed Pantry Ingredients</span>
                  </div>
                  <ul className="space-y-2 text-xs divide-y divide-terracotta-100 dark:divide-[#2e1d17]">
                    {recipe.needed_ingredients.map((item, idx) => (
                      <li key={idx} className="pt-2 flex items-start justify-between">
                        <div>
                          <span className="font-semibold text-stone-900 dark:text-ivory-100">{item.name}</span>
                          {item.purpose && (
                            <p className="text-[11px] text-stone-600 dark:text-stone-300 mt-0.5">{item.purpose}</p>
                          )}
                        </div>
                        <span className="font-mono font-bold text-terracotta-700 dark:text-terracotta-300 ml-2 whitespace-nowrap bg-white dark:bg-[#121715] px-2.5 py-1 rounded-lg border border-terracotta-200 dark:border-[#3d241c] shadow-xs">
                          {item.amount}
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Missing Ingredients & Substitutions */}
              {recipe.missing_ingredients.length > 0 && (
                <div className="p-3 bg-ivory-50 dark:bg-[#1d2622] rounded-xl border border-ivory-200 dark:border-forest-800 text-xs space-y-1 mt-4">
                  <span className="font-bold text-stone-800 dark:text-ivory-100">Chef's Garnish & Finishing Ideas:</span>
                  <ul className="list-disc list-inside text-stone-600 dark:text-stone-400 space-y-0.5">
                    {recipe.missing_ingredients.map((m, i) => (
                      <li key={i}>{m}</li>
                    ))}
                  </ul>
                </div>
              )}

              {recipe.substitutions.length > 0 && (
                <div className="p-3 bg-sage-50/60 dark:bg-forest-900/30 rounded-xl border border-sage-200 dark:border-forest-800 text-xs space-y-1">
                  <span className="font-bold text-forest-800 dark:text-sage-300">Flexible Substitutions:</span>
                  <ul className="list-disc list-inside text-stone-600 dark:text-stone-400 space-y-0.5">
                    {recipe.substitutions.map((s, i) => (
                      <li key={i}>{s}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>

            {/* Preparation steps column */}
            <div className="md:col-span-7 space-y-4">
              <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-100 border-b border-ivory-200 dark:border-forest-900 pb-2">
                Step-by-Step Culinary Preparation
              </h3>
              <ol className="space-y-4">
                {recipe.steps.map((step, idx) => (
                  <li key={idx} className="flex items-start space-x-3 text-xs leading-relaxed text-stone-700 dark:text-stone-300">
                    <span className="w-6 h-6 rounded-full bg-forest-600/10 dark:bg-forest-900 text-forest-700 dark:text-sage-300 font-bold flex items-center justify-center shrink-0 mt-0.5 text-[11px]">
                      {idx + 1}
                    </span>
                    <span className="pt-0.5">{step}</span>
                  </li>
                ))}
              </ol>
            </div>
          </div>
        </article>
      )}
    </div>
  );
};
