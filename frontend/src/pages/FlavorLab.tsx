import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  FlaskConical,
  Plus,
  Trash2,
  Sparkles,
  AlertTriangle,
  BookOpen,
  Bookmark,
  Star,
  RefreshCw,
  Camera,
  ChevronDown,
  Info,
  CheckCircle,
  HelpCircle,
  ArrowRight,
  ShieldCheck,
  Zap,
  ChefHat,
  Heart
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { api } from '../services/api';
import { SelectedIngredient, CombinationAnalysis, Ingredient, DishSuggestion } from '../types';
import { RadarTasteChart } from '../components/RadarTasteChart';
import { CompatibilityGauge } from '../components/CompatibilityGauge';

interface FlavorLabProps {
  selectedIngredients: SelectedIngredient[];
  onRemoveIngredient: (index: number) => void;
  onClearAll: () => void;
  onUpdateQuantity: (index: number, quantity: number) => void;
  onUpdateUnit: (index: number, unit: string) => void;
  onUpdatePrep: (index: number, prep: string) => void;
  onAddIngredient: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const FlavorLab: React.FC<FlavorLabProps> = ({
  selectedIngredients,
  onRemoveIngredient,
  onClearAll,
  onUpdateQuantity,
  onUpdateUnit,
  onUpdatePrep,
  onAddIngredient,
}) => {
  const navigate = useNavigate();

  // Search to add inside lab
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Ingredient[]>([]);

  // Analysis state
  const [analysis, setAnalysis] = useState<CombinationAnalysis | null>(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [analysisError, setAnalysisError] = useState<string | null>(null);
  const [wishlistToast, setWishlistToast] = useState<string | null>(null);

  // Modals for Saving & Rating
  const [showSaveModal, setShowSaveModal] = useState(false);
  const [customTitle, setCustomTitle] = useState('');
  const [notes, setNotes] = useState('');
  const [savedSuccess, setSavedSuccess] = useState(false);

  const [showRateModal, setShowRateModal] = useState(false);
  const [ratingScore, setRatingScore] = useState(5);
  const [ratingComment, setRatingComment] = useState('');
  const [ratedSuccess, setRatedSuccess] = useState(false);

  // Check for duplicates in current selection
  const nameCounts: Record<string, number> = {};
  selectedIngredients.forEach((item) => {
    const clean = item.name.toLowerCase().trim();
    nameCounts[clean] = (nameCounts[clean] || 0) + 1;
  });
  const hasDuplicates = Object.values(nameCounts).some((count) => count > 1);

  const handleSearchChange = async (val: string) => {
    setSearchQuery(val);
    if (!val.trim()) {
      setSearchResults([]);
      return;
    }
    try {
      const results = await api.ingredients.search(val);
      setSearchResults(results.slice(0, 5));
    } catch {
      setSearchResults([]);
    }
  };

  const handleSelectSearchResult = (ing: Ingredient) => {
    onAddIngredient(ing.name, 100, ing.default_unit, 'Raw');
    setSearchQuery('');
    setSearchResults([]);
  };

  const triggerAnalysis = async () => {
    if (selectedIngredients.length === 0) return;
    setAnalyzing(true);
    setAnalysisError(null);
    try {
      const result = await api.combinations.analyze(selectedIngredients);
      setAnalysis(result);
      if (result.overall_compatibility >= 85) {
        confetti({ particleCount: 80, spread: 60, origin: { y: 0.6 } });
      }
    } catch (err: any) {
      setAnalysisError(err.message || 'Error analyzing flavor combination');
    } finally {
      setAnalyzing(false);
    }
  };

  const handleSaveCombination = async () => {
    if (!analysis?.id) return;
    try {
      await api.combinations.save(analysis.id, customTitle || analysis.title, notes);
      setSavedSuccess(true);
      setTimeout(() => {
        setSavedSuccess(false);
        setShowSaveModal(false);
      }, 1500);
    } catch (err: any) {
      alert(err.message || 'Failed to save combination');
    }
  };

  const handleRateCombination = async () => {
    if (!analysis?.id) return;
    try {
      await api.ratings.submit({
        score: ratingScore,
        comment: ratingComment,
        combination_id: analysis.id,
        would_make_again: ratingScore >= 3,
      });
      setRatedSuccess(true);
      setTimeout(() => {
        setRatedSuccess(false);
        setShowRateModal(false);
      }, 1500);
    } catch (err: any) {
      alert(err.message || 'Failed to record rating');
    }
  };

  const handleGenerateRecipe = () => {
    navigate('/recipes', {
      state: {
        ingredients: selectedIngredients,
        prediction_id: analysis?.id,
        title: analysis?.title,
      },
    });
  };

  const handleWishlistDish = async (dish: DishSuggestion) => {
    try {
      const recipe = await api.recipes.generate({
        ingredients: selectedIngredients,
        prediction_id: analysis?.id,
        meal_type: dish.name
      });
      if (recipe.id) {
        await api.recipes.toggleWishlist(recipe.id);
        setWishlistToast(`Added "${dish.name}" to your Wishlist! ❤️`);
        setTimeout(() => setWishlistToast(null), 3000);
      }
    } catch (err: any) {
      alert(err.message || 'Failed to wishlist recipe');
    }
  };

  const handleCookDish = (dish: DishSuggestion) => {
    navigate('/recipes', {
      state: {
        ingredients: selectedIngredients,
        prediction_id: analysis?.id,
        title: dish.name,
      },
    });
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Toast Notification */}
      {wishlistToast && (
        <div className="fixed top-24 right-6 z-50 px-4 py-2.5 rounded-xl bg-forest-600 text-white font-bold text-xs shadow-xl flex items-center space-x-2 animate-in fade-in slide-in-from-top-4">
          <Heart className="w-4 h-4 fill-current text-terracotta-300" />
          <span>{wishlistToast}</span>
        </div>
      )}

      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <div className="flex items-center space-x-2 text-forest-700 dark:text-sage-400 mb-1">
            <FlaskConical className="w-5 h-5 text-sage-600 dark:text-sage-400" />
            <span className="text-xs font-bold uppercase tracking-wider">Multi-Ingredient Synergy Engine</span>
          </div>
          <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
            Flavor Lab Workspace
          </h1>
          <p className="text-sm text-stone-600 dark:text-stone-300 mt-1">
            Combine any number of ingredients (up to 30), adjust quantities and cooking techniques, and evaluate culinary harmony.
          </p>
        </div>

        {selectedIngredients.length > 0 && (
          <div className="flex items-center space-x-2 self-start md:self-auto">
            <button
              onClick={onClearAll}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold text-stone-600 dark:text-stone-300 bg-ivory-200 dark:bg-forest-900/60 hover:bg-ivory-300 dark:hover:bg-forest-800 transition-colors"
            >
              Clear Workspace
            </button>
            <button
              onClick={triggerAnalysis}
              disabled={analyzing}
              className="flex items-center space-x-2 px-6 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-md transition-all disabled:opacity-50"
            >
              {analyzing ? (
                <>
                  <RefreshCw className="w-4 h-4 animate-spin text-sage-200" />
                  <span>Computing Flavor Palate...</span>
                </>
              ) : (
                <>
                  <Sparkles className="w-4 h-4 text-sage-200" />
                  <span>Analyze Combination ({selectedIngredients.length})</span>
                </>
              )}
            </button>
          </div>
        )}
      </div>

      {/* Duplicate Warning Alert */}
      {hasDuplicates && (
        <div className="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 text-amber-900 dark:text-amber-200 text-xs flex items-center space-x-3">
          <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0" />
          <div>
            <span className="font-bold">Duplicate Ingredient Notice: </span>
            You have added the same ingredient multiple times. The engine will aggregate their masses together for the analysis.
          </div>
        </div>
      )}

      {/* Main Grid: Left is Workbench, Right is Analysis Panel */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Left Column: Interactive Workbench (5 cols or 12 if no analysis) */}
        <div className={`space-y-6 ${analysis ? 'lg:col-span-5' : 'lg:col-span-12'}`}>
          {/* Quick Add Bar */}
          <div className="bg-ivory-50 dark:bg-[#151c19] p-4 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm relative">
            <label className="block text-xs font-bold text-stone-700 dark:text-stone-300 uppercase tracking-wider mb-2">
              Add Ingredient to Formula
            </label>
            <div className="relative">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => handleSearchChange(e.target.value)}
                placeholder="Type ingredient (e.g. Cardamom, Mango, Curd, Soy Sauce)..."
                className="w-full px-4 py-2.5 rounded-xl bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 text-sm text-stone-900 dark:text-ivory-100 focus:outline-none focus:ring-2 focus:ring-forest-500"
              />
              {searchResults.length > 0 && (
                <div className="absolute left-0 right-0 top-full mt-1.5 bg-white dark:bg-[#1b2420] rounded-xl shadow-xl border border-ivory-300 dark:border-forest-800 z-30 p-1.5">
                  {searchResults.map((ing) => (
                    <button
                      key={ing.id}
                      onClick={() => handleSelectSearchResult(ing)}
                      className="w-full text-left px-3 py-2 rounded-lg text-xs font-semibold hover:bg-ivory-100 dark:hover:bg-forest-900 flex items-center justify-between text-stone-800 dark:text-stone-200"
                    >
                      <span>{ing.name} ({ing.category})</span>
                      <Plus className="w-3.5 h-3.5 text-forest-600 dark:text-sage-400" />
                    </button>
                  ))}
                </div>
              )}
            </div>
            <div className="mt-2 flex items-center justify-between text-xs text-stone-500 dark:text-stone-400">
              <span>{selectedIngredients.length} / 35 ingredients selected</span>
              <button
                onClick={() => navigate('/vision')}
                className="text-forest-700 dark:text-sage-300 font-semibold hover:underline flex items-center space-x-1"
              >
                <Camera className="w-3.5 h-3.5" />
                <span>Snap / Upload Photo</span>
              </button>
            </div>
          </div>

          {/* Selected Ingredients Workbench List */}
          {selectedIngredients.length === 0 ? (
            <div className="bg-ivory-50 dark:bg-[#151c19] border-2 border-dashed border-ivory-300 dark:border-forest-900 rounded-3xl p-10 text-center space-y-4">
              <div className="w-16 h-16 rounded-2xl bg-sage-100 dark:bg-forest-900 text-forest-600 dark:text-sage-300 flex items-center justify-center mx-auto">
                <FlaskConical className="w-8 h-8" />
              </div>
              <div>
                <h3 className="font-serif text-lg font-bold text-stone-800 dark:text-ivory-100">
                  Your Flavor Lab is Empty
                </h3>
                <p className="text-xs text-stone-500 dark:text-stone-400 max-w-sm mx-auto mt-1">
                  Search above, choose from the Explorer, upload a food photo, or ask Chef AI to load a flavor synergy!
                </p>
              </div>
              <div className="flex flex-wrap justify-center gap-2 pt-2">
                <button
                  onClick={() => {
                    onAddIngredient('Vanilla', 100, 'g', 'Raw');
                    onAddIngredient('Soy Sauce', 15, 'ml', 'Raw');
                  }}
                  className="px-3 py-1.5 rounded-full text-xs font-semibold bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700"
                >
                  ⚡ Try: Vanilla + Soy Sauce
                </button>
                <button
                  onClick={() => {
                    onAddIngredient('Mango', 150, 'g', 'Raw');
                    onAddIngredient('Curd', 100, 'g', 'Raw');
                    onAddIngredient('Cardamom', 2, 'g', 'Raw');
                  }}
                  className="px-3 py-1.5 rounded-full text-xs font-semibold bg-sage-100 dark:bg-forest-900 text-forest-700 dark:text-sage-300 border border-sage-300 dark:border-forest-700"
                >
                  🥭 Try: Mango + Curd + Cardamom
                </button>
              </div>
            </div>
          ) : (
            <div className="space-y-3">
              {selectedIngredients.map((item, index) => (
                <div
                  key={`${item.name}-${index}`}
                  className="bg-white dark:bg-[#151c19] p-4 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-2xs hover:shadow-xs transition-shadow flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                >
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 rounded-xl bg-ivory-200 dark:bg-forest-900/60 flex items-center justify-center font-bold text-forest-800 dark:text-sage-200 text-xs">
                      {index + 1}
                    </div>
                    <div>
                      <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-sm">{item.name}</h4>
                      <span className="text-[11px] text-stone-500 dark:text-stone-400 capitalize">
                        {item.preparation_method} • {item.quantity} {item.unit}
                      </span>
                    </div>
                  </div>

                  {/* Quantity, Unit & Preparation Controls */}
                  <div className="flex items-center space-x-2">
                    {/* Quantity input */}
                    <div className="flex items-center space-x-1">
                      <input
                        type="number"
                        min="1"
                        max="5000"
                        value={item.quantity}
                        onChange={(e) => onUpdateQuantity(index, Number(e.target.value))}
                        className="w-16 px-2 py-1 rounded-lg bg-ivory-100 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-xs font-semibold text-stone-800 dark:text-ivory-100 text-center focus:outline-none"
                      />
                      {/* Unit dropdown */}
                      <select
                        value={item.unit}
                        onChange={(e) => onUpdateUnit(index, e.target.value)}
                        className="px-2 py-1 rounded-lg bg-ivory-100 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-xs font-medium text-stone-700 dark:text-stone-300 focus:outline-none"
                      >
                        <option value="g">g</option>
                        <option value="ml">ml</option>
                        <option value="piece">piece</option>
                        <option value="tbsp">tbsp</option>
                        <option value="tsp">tsp</option>
                        <option value="pinch">pinch</option>
                      </select>
                    </div>

                    {/* Preparation method dropdown */}
                    <select
                      value={item.preparation_method}
                      onChange={(e) => onUpdatePrep(index, e.target.value)}
                      className="px-2 py-1 rounded-lg bg-ivory-100 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-xs font-medium text-stone-700 dark:text-stone-300 focus:outline-none"
                    >
                      <option value="Raw">Raw</option>
                      <option value="Roasted">Roasted</option>
                      <option value="Sautéed">Sautéed</option>
                      <option value="Cooked">Cooked</option>
                      <option value="Boiled">Boiled</option>
                    </select>

                    {/* Delete button */}
                    <button
                      onClick={() => onRemoveIngredient(index)}
                      className="p-1.5 rounded-lg text-stone-400 hover:text-terracotta-600 hover:bg-terracotta-50 dark:hover:bg-terracotta-900/30 transition-colors"
                      title="Remove ingredient"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              ))}

              <div className="pt-2">
                <button
                  onClick={triggerAnalysis}
                  disabled={analyzing}
                  className="w-full py-3.5 rounded-2xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-md transition-all flex items-center justify-center space-x-2"
                >
                  {analyzing ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin text-sage-200" />
                      <span>Computing Compound Interactions...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles className="w-4 h-4 text-sage-200" />
                      <span>Analyze Combination ({selectedIngredients.length} Ingredients)</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Right Column: In-Depth Flavor Analysis Results */}
        {analysis && (
          <div className="lg:col-span-7 space-y-6 animate-fade-in">
            {/* Top Summary Card */}
            <div className="bg-ivory-50 dark:bg-[#151c19] rounded-3xl p-6 sm:p-8 border border-ivory-300 dark:border-forest-900 shadow-sm space-y-6">
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-ivory-200 dark:border-forest-900 pb-5">
                <div>
                  <div className="flex items-center space-x-2 text-xs font-semibold text-sage-600 dark:text-sage-400 mb-1">
                    <CheckCircle className="w-4 h-4" />
                    <span>Analysis Verified • {analysis.evidence_quality}</span>
                  </div>
                  <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{analysis.title}</h2>
                </div>

                <div className="flex items-center space-x-2">
                  <button
                    onClick={() => setShowSaveModal(true)}
                    className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 hover:bg-ivory-100 dark:hover:bg-forest-900 text-xs font-semibold text-stone-700 dark:text-stone-300 shadow-sm transition-all"
                  >
                    <Bookmark className="w-3.5 h-3.5 text-forest-600 dark:text-sage-400" />
                    <span>Save</span>
                  </button>
                  <button
                    onClick={() => setShowRateModal(true)}
                    className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 hover:bg-ivory-100 dark:hover:bg-forest-900 text-xs font-semibold text-stone-700 dark:text-stone-300 shadow-sm transition-all"
                  >
                    <Star className="w-3.5 h-3.5 text-terracotta-500" />
                    <span>Rate</span>
                  </button>
                </div>
              </div>

              {/* Emergent Flavor Illusion (e.g. Vanilla + Soy Sauce = Salted Caramel) */}
              {analysis.tastes_like && (
                <div className="p-5 rounded-2xl bg-linear-to-r from-amber-50 to-orange-50 dark:from-amber-950/40 dark:to-orange-950/30 border-2 border-amber-300 dark:border-amber-700/60 shadow-sm space-y-2">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2 text-amber-900 dark:text-amber-200">
                      <Sparkles className="w-5 h-5 text-amber-600 dark:text-amber-400 animate-spin" />
                      <span className="text-xs font-black uppercase tracking-wider">
                        Sensory Flavor Alchemy (Emergent Flavor Illusion)
                      </span>
                    </div>
                    {analysis.vibe_check && (
                      <span className="px-2.5 py-0.5 rounded-full bg-amber-200 dark:bg-amber-900 text-amber-900 dark:text-amber-100 font-extrabold text-[11px] shadow-2xs">
                        {analysis.vibe_check}
                      </span>
                    )}
                  </div>
                  <div className="text-xl font-serif font-black text-amber-950 dark:text-amber-100">
                    ✨ Tastes Like: <span className="underline decoration-amber-400 decoration-wavy">{analysis.tastes_like}</span>
                  </div>
                  {analysis.tastes_like_explanation && (
                    <p className="text-xs text-amber-900 dark:text-amber-300/90 leading-relaxed font-medium">
                      {analysis.tastes_like_explanation}
                    </p>
                  )}
                </div>
              )}

              {/* Dishes You Can Make Using These Ingredients */}
              {analysis.possible_dishes && analysis.possible_dishes.length > 0 && (
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <ChefHat className="w-5 h-5 text-forest-700 dark:text-sage-300" />
                      <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-100">
                        Dishes You Can Make Using These Ingredients
                      </h3>
                    </div>
                    <span className="text-xs text-stone-500 dark:text-stone-400 font-medium">
                      {analysis.possible_dishes.length} ideas unlocked
                    </span>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {analysis.possible_dishes.map((dish, dIdx) => (
                      <div
                        key={dIdx}
                        className="p-4 rounded-2xl bg-white dark:bg-[#1b2420] border border-ivory-200 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:border-forest-400 transition-all"
                      >
                        <div>
                          <div className="flex items-start justify-between gap-2">
                            <h4 className="font-bold text-stone-900 dark:text-ivory-100 text-sm">
                              {dish.name}
                            </h4>
                            {dish.vibe_tag && (
                              <span className="shrink-0 text-[10px] font-bold px-2 py-0.5 rounded-full bg-forest-50 dark:bg-forest-900/60 text-forest-700 dark:text-sage-300 border border-forest-200 dark:border-forest-800">
                                {dish.vibe_tag}
                              </span>
                            )}
                          </div>
                          <p className="mt-1 text-xs text-stone-600 dark:text-stone-300 line-clamp-2">
                            {dish.description}
                          </p>
                          <div className="mt-2 flex items-center space-x-3 text-[11px] text-stone-500 dark:text-stone-400">
                            <span>⏱️ ~{dish.cook_time_mins || dish.estimated_time_mins || 15} mins</span>
                            {dish.difficulty && <span>• {dish.difficulty}</span>}
                          </div>
                        </div>

                        <div className="mt-3 pt-2.5 border-t border-ivory-200 dark:border-forest-900/80 flex items-center justify-between gap-2">
                          <button
                            onClick={() => handleWishlistDish(dish)}
                            className="flex items-center space-x-1 px-3 py-1.5 rounded-xl bg-ivory-100 dark:bg-forest-900/40 hover:bg-terracotta-50 hover:text-terracotta-600 dark:hover:bg-terracotta-900/30 text-stone-700 dark:text-stone-300 text-xs font-semibold transition-all"
                          >
                            <Heart className="w-3.5 h-3.5 text-terracotta-500" />
                            <span>Wishlist</span>
                          </button>
                          <button
                            onClick={() => handleCookDish(dish)}
                            className="flex items-center space-x-1 px-3 py-1.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-xs font-semibold shadow-2xs transition-all"
                          >
                            <BookOpen className="w-3.5 h-3.5" />
                            <span>Cook Recipe</span>
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Gauges: Overall Compatibility vs Personalized Match */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-white dark:bg-[#1b2420] p-6 rounded-2xl border border-ivory-200 dark:border-forest-900">
                <CompatibilityGauge
                  score={analysis.overall_compatibility}
                  label="General Compatibility"
                  sublabel="Culinary science & shared compounds"
                  size="md"
                />
                <CompatibilityGauge
                  score={analysis.personalized_match !== null && analysis.personalized_match !== undefined ? analysis.personalized_match : analysis.overall_compatibility}
                  label="Personalized Match"
                  sublabel={analysis.personalized_match === 0 ? "Blocked by Allergy Constraint!" : "Tailored to your taste profile"}
                  highlightColor={analysis.personalized_match === 0 ? "#A84523" : undefined}
                  size="md"
                />
              </div>

              {/* Scientific Explanation Summary */}
              <div className="bg-sage-50/70 dark:bg-forest-900/30 p-4 rounded-2xl border border-sage-200 dark:border-forest-800 text-xs text-stone-700 dark:text-stone-300 leading-relaxed space-y-1">
                <p className="font-semibold text-forest-800 dark:text-sage-300">Sensory Evaluation Summary</p>
                <p>{analysis.explanation}</p>
              </div>

              {/* Radar Chart for 6 Basic Tastes */}
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <h3 className="font-serif text-base font-bold text-stone-900 dark:text-ivory-100">
                    Palate Profile (6 Basic Tastes)
                  </h3>
                  <span className="text-[11px] text-stone-500 dark:text-stone-400">0 to 10 intensity scale</span>
                </div>
                <div className="bg-white dark:bg-[#1b2420] p-4 rounded-2xl border border-ivory-200 dark:border-forest-900 shadow-sm">
                  <RadarTasteChart tasteProfile={analysis.taste_profile} />
                </div>
              </div>

              {/* Dominant Aromas Breakdown */}
              {Object.keys(analysis.aroma_profile).length > 0 && (
                <div className="space-y-2">
                  <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-xs uppercase tracking-wider">
                    Aroma Volatile Distribution
                  </h4>
                  <div className="flex flex-wrap gap-2">
                    {Object.entries(analysis.aroma_profile).map(([aroma, pct]) => (
                      <span
                        key={aroma}
                        className="inline-flex items-center space-x-1 px-3 py-1.5 rounded-xl bg-ivory-200 dark:bg-[#1f2824] text-stone-800 dark:text-stone-200 text-xs font-medium border border-ivory-300 dark:border-forest-800"
                      >
                        <span className="font-semibold text-forest-700 dark:text-sage-300">{aroma}:</span>
                        <span className="font-mono text-stone-600 dark:text-stone-400">{pct}%</span>
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Flavor Conflicts or Warnings */}
              {analysis.flavor_conflicts.length > 0 && (
                <div className="p-4 rounded-2xl bg-amber-50/80 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 text-xs space-y-1.5">
                  <div className="flex items-center space-x-1.5 font-bold text-amber-900 dark:text-amber-200">
                    <AlertTriangle className="w-4 h-4 text-amber-600" />
                    <span>Culinary Synergy & Balance Warnings ({analysis.flavor_conflicts.length})</span>
                  </div>
                  <ul className="list-disc list-inside space-y-1 text-amber-800 dark:text-amber-300">
                    {analysis.flavor_conflicts.map((c, i) => (
                      <li key={i}>{c}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Suggested Ingredient Ratios */}
              {analysis.suggested_ratios.length > 0 && (
                <div className="space-y-2">
                  <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-xs uppercase tracking-wider">
                    Recommended Culinary Ratios
                  </h4>
                  <div className="bg-white dark:bg-[#1b2420] rounded-2xl border border-ivory-200 dark:border-forest-900 overflow-hidden divide-y divide-ivory-200 dark:divide-forest-900 text-xs">
                    {analysis.suggested_ratios.map((item) => (
                      <div key={item.ingredient} className="flex items-center justify-between px-4 py-2.5">
                        <span className="font-medium text-stone-800 dark:text-ivory-100">{item.ingredient}</span>
                        <div className="space-x-3 text-stone-500 dark:text-stone-400">
                          <span className="text-[11px]">Recommended: <strong className="text-forest-700 dark:text-sage-300">{item.ratio}</strong></span>
                          <span>Current: {item.recommended_grams}g</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Pairwise Interaction Matrix */}
              {analysis.pairwise_matrix.length > 0 && (
                <div className="space-y-2">
                  <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-xs uppercase tracking-wider">
                    Pairwise Chemical & Culinary Interactions
                  </h4>
                  <div className="space-y-2">
                    {analysis.pairwise_matrix.slice(0, 4).map((pair, idx) => (
                      <div key={idx} className="bg-white dark:bg-[#1b2420] p-3.5 rounded-xl border border-ivory-200 dark:border-forest-900 text-xs space-y-1">
                        <div className="flex items-center justify-between font-semibold">
                          <span className="text-stone-900 dark:text-ivory-100">{pair.ingredient_a} ↔ {pair.ingredient_b}</span>
                          <span className="text-forest-700 dark:text-sage-300 font-mono">{pair.affinity_score}% affinity</span>
                        </div>
                        <p className="text-stone-600 dark:text-stone-400 text-[11px]">{pair.reason}</p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Complementary Suggestions */}
              {analysis.complementary_suggestions.length > 0 && (
                <div className="p-4 rounded-2xl bg-sage-50 dark:bg-forest-900/40 border border-sage-200 dark:border-forest-800 text-xs space-y-2">
                  <span className="font-bold text-forest-800 dark:text-sage-300 flex items-center space-x-1.5">
                    <Sparkles className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                    <span>Suggested Complementary Additions:</span>
                  </span>
                  <div className="flex flex-wrap gap-2">
                    {analysis.complementary_suggestions.map((comp) => (
                      <button
                        key={comp}
                        onClick={() => {
                          const baseName = comp.split('(')[0].trim();
                          onAddIngredient(baseName, 20, 'g', 'Raw');
                        }}
                        className="px-3 py-1.5 rounded-xl bg-white dark:bg-[#1b2420] hover:bg-forest-50 dark:hover:bg-forest-900 text-forest-700 dark:text-sage-300 font-semibold border border-sage-300 dark:border-forest-700 text-xs transition-colors"
                      >
                        + Add {comp}
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* Generate Recipe CTA */}
              <div className="pt-2">
                <button
                  onClick={handleGenerateRecipe}
                  className="w-full py-3.5 rounded-2xl bg-terracotta-600 hover:bg-terracotta-500 text-white font-semibold text-sm shadow-md transition-all flex items-center justify-center space-x-2"
                >
                  <BookOpen className="w-4 h-4" />
                  <span>Generate Full Recipe From This Combination</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Save Combination Modal */}
      {showSaveModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/80 backdrop-blur-sm">
          <div className="relative w-full max-w-md bg-ivory-50 dark:bg-[#18201d] rounded-2xl shadow-2xl border border-ivory-300 dark:border-forest-900 p-6 space-y-4">
            <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-100">Save Combination to Library</h3>
            {savedSuccess ? (
              <div className="p-4 bg-sage-100 dark:bg-forest-900 text-forest-800 dark:text-sage-200 text-xs rounded-xl font-semibold text-center">
                Saved successfully to your dashboard!
              </div>
            ) : (
              <div className="space-y-3 text-xs">
                <div>
                  <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Custom Title</label>
                  <input
                    type="text"
                    value={customTitle}
                    onChange={(e) => setCustomTitle(e.target.value)}
                    placeholder={analysis?.title}
                    className="w-full px-3 py-2 rounded-xl bg-white dark:bg-[#121815] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-sm focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Personal Notes</label>
                  <textarea
                    value={notes}
                    onChange={(e) => setNotes(e.target.value)}
                    placeholder="e.g. Try with less lime next time, pairs wonderfully with morning tea..."
                    className="w-full px-3 py-2 rounded-xl bg-white dark:bg-[#121815] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs h-20 focus:outline-none"
                  />
                </div>
                <div className="pt-2 flex justify-end space-x-2">
                  <button
                    onClick={() => setShowSaveModal(false)}
                    className="px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900 text-stone-700 dark:text-stone-300 text-xs font-semibold"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleSaveCombination}
                    className="px-5 py-2 rounded-xl bg-forest-600 text-white text-xs font-semibold hover:bg-forest-500"
                  >
                    Save Combination
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Rate Combination Modal */}
      {showRateModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/80 backdrop-blur-sm">
          <div className="relative w-full max-w-md bg-ivory-50 dark:bg-[#18201d] rounded-2xl shadow-2xl border border-ivory-300 dark:border-forest-900 p-6 space-y-4">
            <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-100">Rate This Flavor Pairing</h3>
            {ratedSuccess ? (
              <div className="p-4 bg-sage-100 dark:bg-forest-900 text-forest-800 dark:text-sage-200 text-xs rounded-xl font-semibold text-center">
                Rating recorded! Your taste preferences have been updated.
              </div>
            ) : (
              <div className="space-y-4 text-xs">
                <div>
                  <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-2">How did you enjoy this pairing?</label>
                  <div className="flex items-center space-x-2">
                    {[1, 2, 3, 4, 5].map((star) => (
                      <button
                        key={star}
                        type="button"
                        onClick={() => setRatingScore(star)}
                        className={`p-2 rounded-xl transition-all ${
                          ratingScore >= star ? 'text-amber-500 bg-amber-50 dark:bg-amber-950/40' : 'text-stone-300 dark:text-stone-600 hover:text-stone-400'
                        }`}
                      >
                        <Star className="w-6 h-6 fill-current" />
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Feedback Comment</label>
                  <textarea
                    value={ratingComment}
                    onChange={(e) => setRatingComment(e.target.value)}
                    placeholder="What did you like or dislike about the balance?"
                    className="w-full px-3 py-2 rounded-xl bg-white dark:bg-[#121815] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs h-20 focus:outline-none"
                  />
                </div>

                <div className="pt-2 flex justify-end space-x-2">
                  <button
                    onClick={() => setShowRateModal(false)}
                    className="px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900 text-stone-700 dark:text-stone-300 text-xs font-semibold"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleRateCombination}
                    className="px-5 py-2 rounded-xl bg-forest-600 text-white text-xs font-semibold hover:bg-forest-500"
                  >
                    Submit Rating
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
