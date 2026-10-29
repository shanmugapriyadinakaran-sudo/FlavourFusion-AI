import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import {
  Search,
  BookOpen,
  Clock,
  Users,
  Flame,
  ChefHat,
  Bookmark,
  Heart,
  Wrench,
  Utensils,
  CheckCircle2,
  Sparkles,
  ArrowRight,
  Filter,
  Layers,
  X,
  ExternalLink,
  Printer
} from 'lucide-react';
import { api } from '../services/api';
import { Recipe, SelectedIngredient } from '../types';

interface RecipeLibraryProps {
  onAddIngredientsToLab?: (ingredients: SelectedIngredient[]) => void;
}

export const RecipeLibrary: React.FC<RecipeLibraryProps> = ({ onAddIngredientsToLab }) => {
  const navigate = useNavigate();
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCuisine, setSelectedCuisine] = useState('All');
  const [selectedMealType, setSelectedMealType] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [activeRecipe, setActiveRecipe] = useState<Recipe | null>(null);
  const [checkedSteps, setCheckedSteps] = useState<Record<number, boolean>>({});

  const cuisines = ['All', 'Italian', 'Chinese', 'Spanish', 'Mexican', 'French', 'Japanese', 'Indian'];
  const mealTypes = ['All', 'Dinner', 'Lunch', 'Breakfast', 'Dessert', 'Appetizer', 'Snack'];
  const difficulties = ['All', 'Easy', 'Medium', 'Advanced'];

  useEffect(() => {
    fetchCatalog();
  }, [selectedCuisine, selectedMealType, selectedDifficulty]);

  const fetchCatalog = async () => {
    try {
      setLoading(true);
      const data = await api.recipes.getCatalog({
        q: searchQuery || undefined,
        cuisine: selectedCuisine,
        meal_type: selectedMealType,
        difficulty: selectedDifficulty,
      });
      setRecipes(data);
    } catch (err) {
      console.error('Failed to load recipe catalog:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchCatalog();
  };

  const handleToggleSave = async (recipe: Recipe, e?: React.MouseEvent) => {
    e?.stopPropagation();
    if (!recipe.id) return;
    try {
      const res = await api.recipes.toggleSave(recipe.id);
      setRecipes((prev) =>
        prev.map((r) => (r.id === recipe.id ? { ...r, is_saved: res.is_saved } : r))
      );
      if (activeRecipe && activeRecipe.id === recipe.id) {
        setActiveRecipe({ ...activeRecipe, is_saved: res.is_saved });
      }
    } catch (err) {
      console.error('Failed to save recipe:', err);
    }
  };

  const handleToggleWishlist = async (recipe: Recipe, e?: React.MouseEvent) => {
    e?.stopPropagation();
    if (!recipe.id) return;
    try {
      const res = await api.recipes.toggleWishlist(recipe.id);
      setRecipes((prev) =>
        prev.map((r) => (r.id === recipe.id ? { ...r, is_wishlisted: res.is_wishlisted } : r))
      );
      if (activeRecipe && activeRecipe.id === recipe.id) {
        setActiveRecipe({ ...activeRecipe, is_wishlisted: res.is_wishlisted });
      }
    } catch (err) {
      console.error('Failed to wishlist recipe:', err);
    }
  };

  const handleSendToFlavorLab = (recipe: Recipe, e?: React.MouseEvent) => {
    e?.stopPropagation();
    if (!onAddIngredientsToLab) {
      navigate('/lab');
      return;
    }
    const labItems: SelectedIngredient[] = recipe.ingredients_list.map((ing) => ({
      name: ing.name,
      quantity: ing.quantity || 100,
      unit: ing.unit || 'g',
      preparation_method: 'Raw',
    }));
    onAddIngredientsToLab(labItems);
    navigate('/lab');
  };

  const toggleStepCheck = (index: number) => {
    setCheckedSteps((prev) => ({ ...prev, [index]: !prev[index] }));
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 transition-colors">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-forest-100 dark:bg-forest-900/50 text-forest-800 dark:text-forest-200 text-xs font-semibold uppercase tracking-wider mb-2">
            <BookOpen className="w-3.5 h-3.5" />
            Master Culinary Archive
          </div>
          <h1 className="text-3xl sm:text-4xl font-serif font-bold text-stone-900 dark:text-ivory-100">
            Recipe Library & Catalog
          </h1>
          <p className="mt-2 text-stone-600 dark:text-stone-300 max-w-2xl text-sm sm:text-base">
            Search iconic global dishes. Explore complete ingredients, exact kitchen tools, cooking vessels, and step-by-step preparation without overriding custom combinations.
          </p>
        </div>

        <button
          onClick={() => navigate('/recipes')}
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl border border-forest-300 dark:border-forest-800 text-forest-800 dark:text-forest-200 hover:bg-forest-50 dark:hover:bg-forest-950/40 text-sm font-medium transition-all shadow-sm"
        >
          <Sparkles className="w-4 h-4 text-forest-600 dark:text-forest-400" />
          Open Dynamic Recipe Generator
        </button>
      </div>

      {/* Search & Filters */}
      <div className="bg-white dark:bg-stone-900 rounded-2xl border border-stone-200/80 dark:border-stone-800 p-4 sm:p-6 mb-8 shadow-sm">
        <form onSubmit={handleSearchSubmit} className="relative mb-5">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search recipes by name, ingredient (e.g. Pizza dough, Beef tenderloin), tools, or vessels..."
            className="w-full pl-11 pr-24 py-3 rounded-xl bg-ivory-50 dark:bg-stone-800/80 border border-stone-300 dark:border-stone-700 text-stone-900 dark:text-ivory-100 placeholder-stone-400 dark:placeholder-stone-500 text-sm focus:outline-none focus:ring-2 focus:ring-forest-500 focus:border-forest-500 transition-all"
          />
          <Search className="w-5 h-5 text-stone-400 dark:text-stone-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <button
            type="submit"
            className="absolute right-2 top-1/2 -translate-y-1/2 px-4 py-1.5 rounded-lg bg-forest-800 hover:bg-forest-700 dark:bg-forest-700 dark:hover:bg-forest-600 text-white text-xs font-medium transition-colors shadow-sm"
          >
            Search
          </button>
        </form>

        {/* Filter Rows */}
        <div className="space-y-3 pt-2 border-t border-stone-100 dark:border-stone-800/60">
          {/* Cuisines */}
          <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
            <span className="text-xs font-semibold text-stone-500 dark:text-stone-400 flex items-center gap-1 shrink-0 mr-1">
              <Filter className="w-3 h-3" /> Cuisine:
            </span>
            {cuisines.map((c) => (
              <button
                key={c}
                onClick={() => setSelectedCuisine(c)}
                className={`px-3 py-1 rounded-full text-xs font-medium shrink-0 transition-all ${
                  selectedCuisine === c
                    ? 'bg-forest-800 text-white dark:bg-forest-600 shadow-sm'
                    : 'bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700'
                }`}
              >
                {c}
              </button>
            ))}
          </div>

          {/* Meal Types & Difficulty */}
          <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2 overflow-x-auto pb-1">
              <span className="font-semibold text-stone-500 dark:text-stone-400 shrink-0">Meal:</span>
              {mealTypes.map((m) => (
                <button
                  key={m}
                  onClick={() => setSelectedMealType(m)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                    selectedMealType === m
                      ? 'bg-sage-600 text-white dark:bg-sage-700'
                      : 'bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700'
                  }`}
                >
                  {m}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-2">
              <span className="font-semibold text-stone-500 dark:text-stone-400">Difficulty:</span>
              {difficulties.map((d) => (
                <button
                  key={d}
                  onClick={() => setSelectedDifficulty(d)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                    selectedDifficulty === d
                      ? 'bg-terracotta-700 text-white dark:bg-terracotta-800'
                      : 'bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700'
                  }`}
                >
                  {d}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Recipe Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((n) => (
            <div
              key={n}
              className="h-80 rounded-2xl bg-stone-100 dark:bg-stone-800 animate-pulse border border-stone-200 dark:border-stone-700"
            />
          ))}
        </div>
      ) : recipes.length === 0 ? (
        <div className="text-center py-16 bg-white dark:bg-stone-900 rounded-2xl border border-stone-200 dark:border-stone-800">
          <BookOpen className="w-12 h-12 text-stone-300 dark:text-stone-600 mx-auto mb-3" />
          <h3 className="text-lg font-medium text-stone-900 dark:text-ivory-100">No matching recipes found</h3>
          <p className="text-sm text-stone-500 dark:text-stone-400 mt-1">
            Try adjusting your search terms or clearing cuisine filters.
          </p>
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedCuisine('All');
              setSelectedMealType('All');
              setSelectedDifficulty('All');
            }}
            className="mt-4 px-4 py-2 rounded-xl bg-forest-800 text-white text-xs font-medium hover:bg-forest-700 transition-colors"
          >
            Reset Filters
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe) => (
            <motion.div
              key={recipe.id || recipe.title}
              whileHover={{ y: -4 }}
              onClick={() => {
                setActiveRecipe(recipe);
                setCheckedSteps({});
              }}
              className="cursor-pointer bg-white dark:bg-stone-900 rounded-2xl border border-stone-200/90 dark:border-stone-800 overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
            >
              <div>
                {/* Card Header with Badges */}
                <div className="p-5 pb-3">
                  <div className="flex items-center justify-between gap-2 mb-2.5">
                    <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-forest-50 dark:bg-forest-950/60 text-forest-800 dark:text-forest-300 border border-forest-200 dark:border-forest-800">
                      {recipe.cuisine} • {recipe.meal_type}
                    </span>
                    <div className="flex items-center gap-1.5">
                      <button
                        onClick={(e) => handleToggleWishlist(recipe, e)}
                        className={`p-1.5 rounded-lg transition-colors ${
                          recipe.is_wishlisted
                            ? 'text-rose-500 bg-rose-50 dark:bg-rose-950/40'
                            : 'text-stone-400 hover:text-rose-500 hover:bg-stone-100 dark:hover:bg-stone-800'
                        }`}
                        title="Add to wishlist"
                      >
                        <Heart className="w-4 h-4 fill-current" />
                      </button>
                      <button
                        onClick={(e) => handleToggleSave(recipe, e)}
                        className={`p-1.5 rounded-lg transition-colors ${
                          recipe.is_saved
                            ? 'text-amber-500 bg-amber-50 dark:bg-amber-950/40'
                            : 'text-stone-400 hover:text-amber-500 hover:bg-stone-100 dark:hover:bg-stone-800'
                        }`}
                        title="Save recipe"
                      >
                        <Bookmark className="w-4 h-4 fill-current" />
                      </button>
                    </div>
                  </div>

                  <h3 className="text-lg font-serif font-bold text-stone-900 dark:text-ivory-100 line-clamp-1">
                    {recipe.title}
                  </h3>
                  <p className="text-xs text-stone-500 dark:text-stone-400 mt-1 line-clamp-2 leading-relaxed">
                    {recipe.summary}
                  </p>
                </div>

                {/* Metrics */}
                <div className="px-5 py-2.5 bg-ivory-50/70 dark:bg-stone-800/40 border-y border-stone-100 dark:border-stone-800/80 flex items-center justify-between text-xs text-stone-600 dark:text-stone-300">
                  <span className="flex items-center gap-1.5">
                    <Clock className="w-3.5 h-3.5 text-stone-400" />
                    {recipe.prep_time_mins + recipe.cook_time_mins}m total
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Users className="w-3.5 h-3.5 text-stone-400" />
                    {recipe.servings} Servings
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Flame className="w-3.5 h-3.5 text-terracotta-500" />
                    {recipe.difficulty}
                  </span>
                </div>

                {/* Key Tools & Vessels Preview */}
                <div className="p-5 pt-3 space-y-2">
                  <div className="text-xs">
                    <span className="font-semibold text-stone-700 dark:text-stone-300 flex items-center gap-1.5 mb-1">
                      <Wrench className="w-3 h-3 text-stone-400" /> Key Tools & Vessels:
                    </span>
                    <div className="flex flex-wrap gap-1">
                      {((recipe.required_vessels || []).concat(recipe.required_tools || [])).slice(0, 3).map((item, idx) => (
                        <span
                          key={idx}
                          className="px-2 py-0.5 rounded bg-stone-100 dark:bg-stone-800 text-[11px] text-stone-600 dark:text-stone-300 truncate max-w-[190px]"
                        >
                          {item}
                        </span>
                      ))}
                      {((recipe.required_vessels?.length || 0) + (recipe.required_tools?.length || 0)) > 3 && (
                        <span className="text-[10px] text-stone-400 self-center">
                          +{((recipe.required_vessels?.length || 0) + (recipe.required_tools?.length || 0)) - 3} more
                        </span>
                      )}
                    </div>
                  </div>

                  <div className="text-xs">
                    <span className="font-semibold text-stone-700 dark:text-stone-300 flex items-center gap-1.5 mb-1">
                      <Utensils className="w-3 h-3 text-stone-400" /> Ingredients ({recipe.ingredients_list?.length || 0}):
                    </span>
                    <p className="text-[11px] text-stone-500 dark:text-stone-400 line-clamp-1">
                      {recipe.ingredients_list?.map((i) => `${i.name} (${i.quantity} ${i.unit})`).join(', ')}
                    </p>
                  </div>
                </div>
              </div>

              {/* Bottom Actions */}
              <div className="p-5 pt-0 flex items-center justify-between gap-2">
                <button
                  onClick={(e) => handleSendToFlavorLab(recipe, e)}
                  className="px-3 py-1.5 rounded-lg border border-forest-300 dark:border-forest-800 text-forest-700 dark:text-forest-300 hover:bg-forest-50 dark:hover:bg-forest-950/40 text-xs font-medium flex items-center gap-1 transition-colors"
                  title="Send ingredients to Flavor Lab"
                >
                  <Sparkles className="w-3.5 h-3.5 text-forest-600" />
                  Analyze in Lab
                </button>

                <span className="text-xs font-medium text-forest-600 dark:text-forest-400 flex items-center gap-1 group-hover:underline">
                  View Full Recipe <ArrowRight className="w-3 h-3" />
                </span>
              </div>
            </motion.div>
          ))}
        </div>
      )}

      {/* Full Recipe Modal View */}
      <AnimatePresence>
        {activeRecipe && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-950/60 backdrop-blur-sm overflow-y-auto">
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 10 }}
              className="bg-white dark:bg-stone-900 rounded-3xl border border-stone-200 dark:border-stone-800 shadow-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto my-8 relative"
            >
              {/* Close Button */}
              <button
                onClick={() => setActiveRecipe(null)}
                className="absolute top-5 right-5 p-2 rounded-full bg-stone-100 dark:bg-stone-800 text-stone-500 hover:text-stone-900 dark:hover:text-ivory-100 transition-colors z-10"
              >
                <X className="w-5 h-5" />
              </button>

              {/* Modal Header */}
              <div className="p-6 sm:p-8 border-b border-stone-100 dark:border-stone-800">
                <div className="flex flex-wrap items-center gap-2 mb-2">
                  <span className="px-3 py-1 rounded-full text-xs font-semibold bg-forest-50 dark:bg-forest-950/80 text-forest-800 dark:text-forest-300 border border-forest-200 dark:border-forest-800">
                    {activeRecipe.cuisine} • {activeRecipe.meal_type}
                  </span>
                  <span className="px-3 py-1 rounded-full text-xs font-medium bg-amber-50 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300">
                    {activeRecipe.difficulty}
                  </span>
                  <span className="text-xs text-stone-400">
                    Mode: {activeRecipe.generation_mode}
                  </span>
                </div>

                <h2 className="text-2xl sm:text-3xl font-serif font-bold text-stone-900 dark:text-ivory-100">
                  {activeRecipe.title}
                </h2>
                <p className="mt-2 text-stone-600 dark:text-stone-300 text-sm leading-relaxed">
                  {activeRecipe.summary}
                </p>

                {/* Timing & Servings bar */}
                <div className="grid grid-cols-3 gap-4 mt-6 p-4 rounded-2xl bg-ivory-50 dark:bg-stone-800/50 border border-stone-200/80 dark:border-stone-800 text-center">
                  <div>
                    <div className="text-xs text-stone-400 font-medium">Prep Time</div>
                    <div className="text-sm font-bold text-stone-900 dark:text-ivory-100 mt-0.5">
                      {activeRecipe.prep_time_mins} mins
                    </div>
                  </div>
                  <div>
                    <div className="text-xs text-stone-400 font-medium">Cook Time</div>
                    <div className="text-sm font-bold text-stone-900 dark:text-ivory-100 mt-0.5">
                      {activeRecipe.cook_time_mins} mins
                    </div>
                  </div>
                  <div>
                    <div className="text-xs text-stone-400 font-medium">Servings</div>
                    <div className="text-sm font-bold text-stone-900 dark:text-ivory-100 mt-0.5">
                      {activeRecipe.servings} People
                    </div>
                  </div>
                </div>
              </div>

              {/* Modal Body */}
              <div className="p-6 sm:p-8 space-y-8">
                {/* Required Tools & Vessels Section */}
                <div className="p-5 rounded-2xl bg-amber-50/50 dark:bg-amber-950/20 border border-amber-200/60 dark:border-amber-900/40">
                  <h4 className="text-sm font-bold text-amber-900 dark:text-amber-200 flex items-center gap-2 mb-3">
                    <Wrench className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                    Kitchen Tools & Cooking Vessels Needed
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    {activeRecipe.required_vessels && activeRecipe.required_vessels.length > 0 && (
                      <div>
                        <span className="text-xs font-semibold text-amber-800/80 dark:text-amber-300/80 uppercase tracking-wider">
                          Pans, Pots & Vessels:
                        </span>
                        <ul className="mt-1.5 space-y-1">
                          {activeRecipe.required_vessels.map((v, i) => (
                            <li key={i} className="text-xs text-stone-800 dark:text-stone-200 flex items-center gap-2">
                              <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
                              {v}
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {activeRecipe.required_tools && activeRecipe.required_tools.length > 0 && (
                      <div>
                        <span className="text-xs font-semibold text-amber-800/80 dark:text-amber-300/80 uppercase tracking-wider">
                          Tools & Cutlery:
                        </span>
                        <ul className="mt-1.5 space-y-1">
                          {activeRecipe.required_tools.map((t, i) => (
                            <li key={i} className="text-xs text-stone-800 dark:text-stone-200 flex items-center gap-2">
                              <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
                              {t}
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                </div>

                {/* Ingredients Section */}
                <div>
                  <h4 className="text-base font-serif font-bold text-stone-900 dark:text-ivory-100 flex items-center gap-2 mb-3">
                    <Utensils className="w-4 h-4 text-forest-600 dark:text-forest-400" />
                    Ingredients Required ({activeRecipe.ingredients_list.length})
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                    {activeRecipe.ingredients_list.map((ing, idx) => (
                      <div
                        key={idx}
                        className="p-3 rounded-xl bg-ivory-50/70 dark:bg-stone-800/60 border border-stone-200/70 dark:border-stone-800 flex items-center justify-between"
                      >
                        <span className="text-xs font-semibold text-stone-900 dark:text-ivory-100">
                          {ing.name}
                        </span>
                        <div className="text-right">
                          <span className="text-xs font-bold text-forest-700 dark:text-forest-300">
                            {ing.quantity} {ing.unit}
                          </span>
                          {ing.notes && (
                            <p className="text-[10px] text-stone-400 dark:text-stone-500 max-w-[150px] truncate">
                              {ing.notes}
                            </p>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>

                  {/* Pantry staples needed */}
                  {activeRecipe.needed_ingredients && activeRecipe.needed_ingredients.length > 0 && (
                    <div className="mt-4 p-4 rounded-xl bg-stone-50 dark:bg-stone-800/40 border border-stone-200/80 dark:border-stone-800">
                      <span className="text-xs font-semibold text-stone-600 dark:text-stone-300">
                        Additional Pantry Essentials:
                      </span>
                      <div className="flex flex-wrap gap-2 mt-2">
                        {activeRecipe.needed_ingredients.map((pantry, pidx) => (
                          <span
                            key={pidx}
                            className="px-2.5 py-1 rounded-lg bg-white dark:bg-stone-800 text-xs border border-stone-200 dark:border-stone-700 text-stone-700 dark:text-stone-300"
                          >
                            <strong>{pantry.name}</strong> ({pantry.amount})
                            {pantry.purpose ? ` — ${pantry.purpose}` : ''}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}
                </div>

                {/* Step-by-Step Preparation */}
                <div>
                  <h4 className="text-base font-serif font-bold text-stone-900 dark:text-ivory-100 flex items-center gap-2 mb-3">
                    <ChefHat className="w-4 h-4 text-forest-600 dark:text-forest-400" />
                    Preparation Method & Cooking Steps
                  </h4>
                  <div className="space-y-3">
                    {activeRecipe.steps.map((step, sIdx) => {
                      const isDone = !!checkedSteps[sIdx];
                      return (
                        <div
                          key={sIdx}
                          onClick={() => toggleStepCheck(sIdx)}
                          className={`p-4 rounded-xl border transition-all cursor-pointer flex items-start gap-3.5 ${
                            isDone
                              ? 'bg-forest-50/60 dark:bg-forest-950/30 border-forest-200 dark:border-forest-800/60 opacity-75'
                              : 'bg-white dark:bg-stone-800/60 border-stone-200/90 dark:border-stone-700/80 hover:border-forest-300 dark:hover:border-forest-700'
                          }`}
                        >
                          <div
                            className={`w-6 h-6 rounded-full flex items-center justify-center shrink-0 mt-0.5 text-xs font-bold transition-all ${
                              isDone
                                ? 'bg-forest-600 text-white'
                                : 'bg-stone-100 dark:bg-stone-700 text-stone-600 dark:text-stone-300'
                            }`}
                          >
                            {isDone ? <CheckCircle2 className="w-4 h-4" /> : sIdx + 1}
                          </div>
                          <p
                            className={`text-xs sm:text-sm leading-relaxed ${
                              isDone
                                ? 'line-through text-stone-400 dark:text-stone-500'
                                : 'text-stone-800 dark:text-stone-200'
                            }`}
                          >
                            {step}
                          </p>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Allergens & Substitutions */}
                {(activeRecipe.allergens.length > 0 || activeRecipe.substitutions.length > 0) && (
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-4 border-t border-stone-100 dark:border-stone-800 text-xs">
                    {activeRecipe.allergens.length > 0 && (
                      <div>
                        <span className="font-semibold text-rose-600 dark:text-rose-400">Allergen Notice:</span>
                        <div className="flex flex-wrap gap-1.5 mt-1">
                          {activeRecipe.allergens.map((all, aIdx) => (
                            <span
                              key={aIdx}
                              className="px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-900"
                            >
                              {all}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}

                    {activeRecipe.substitutions.length > 0 && (
                      <div>
                        <span className="font-semibold text-stone-700 dark:text-stone-300">Culinary Substitutions:</span>
                        <ul className="mt-1 space-y-0.5 text-stone-600 dark:text-stone-400 list-disc list-inside">
                          {activeRecipe.substitutions.map((sub, subIdx) => (
                            <li key={subIdx}>{sub}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                )}
              </div>

              {/* Modal Footer Controls */}
              <div className="p-6 bg-ivory-50/80 dark:bg-stone-800/80 border-t border-stone-200/80 dark:border-stone-800 flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => handleToggleWishlist(activeRecipe)}
                    className={`px-3 py-2 rounded-xl text-xs font-medium flex items-center gap-1.5 transition-colors border ${
                      activeRecipe.is_wishlisted
                        ? 'bg-rose-50 dark:bg-rose-950/60 border-rose-200 dark:border-rose-900 text-rose-600 dark:text-rose-300'
                        : 'bg-white dark:bg-stone-800 border-stone-300 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-700'
                    }`}
                  >
                    <Heart className="w-3.5 h-3.5 fill-current" />
                    {activeRecipe.is_wishlisted ? 'Wishlisted' : 'Add to Wishlist'}
                  </button>

                  <button
                    onClick={() => handleToggleSave(activeRecipe)}
                    className={`px-3 py-2 rounded-xl text-xs font-medium flex items-center gap-1.5 transition-colors border ${
                      activeRecipe.is_saved
                        ? 'bg-amber-50 dark:bg-amber-950/60 border-amber-200 dark:border-amber-900 text-amber-700 dark:text-amber-300'
                        : 'bg-white dark:bg-stone-800 border-stone-300 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-700'
                    }`}
                  >
                    <Bookmark className="w-3.5 h-3.5 fill-current" />
                    {activeRecipe.is_saved ? 'Saved' : 'Save Recipe'}
                  </button>

                  <button
                    onClick={() => window.print()}
                    className="px-3 py-2 rounded-xl text-xs font-medium bg-white dark:bg-stone-800 border border-stone-300 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-700 flex items-center gap-1.5 transition-colors"
                  >
                    <Printer className="w-3.5 h-3.5" />
                    Print
                  </button>
                </div>

                <button
                  onClick={() => handleSendToFlavorLab(activeRecipe)}
                  className="px-4 py-2.5 rounded-xl bg-forest-800 hover:bg-forest-700 dark:bg-forest-600 dark:hover:bg-forest-500 text-white text-xs font-semibold flex items-center gap-2 shadow-sm transition-all"
                >
                  <Sparkles className="w-4 h-4 text-emerald-300" />
                  Load Ingredients into Flavor Lab
                </button>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </div>
  );
};
