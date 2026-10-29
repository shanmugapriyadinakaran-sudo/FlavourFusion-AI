import React, { useState, useEffect } from 'react';
import {
  Search,
  Filter,
  Plus,
  SlidersHorizontal,
  Sparkles,
  Info,
  Check,
  AlertTriangle,
  X
} from 'lucide-react';
import { api } from '../services/api';
import { Ingredient } from '../types';

interface IngredientExplorerProps {
  onAddIngredientToLab: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const IngredientExplorer: React.FC<IngredientExplorerProps> = ({ onAddIngredientToLab }) => {
  const [ingredients, setIngredients] = useState<Ingredient[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedCuisine, setSelectedCuisine] = useState('All');
  const [excludeAllergen, setExcludeAllergen] = useState('');
  
  // Custom Ingredient Modal State
  const [showCustomModal, setShowCustomModal] = useState(false);
  const [customName, setCustomName] = useState('');
  const [customCategory, setCustomCategory] = useState('Produce');
  const [customDescription, setCustomDescription] = useState('');
  const [customUnit, setCustomUnit] = useState('g');
  const [customSweet, setCustomSweet] = useState(3);
  const [customSour, setCustomSour] = useState(1);
  const [customSalty, setCustomSalty] = useState(1);
  const [customBitter, setCustomBitter] = useState(1);
  const [customUmami, setCustomUmami] = useState(2);
  const [customSpicy, setCustomSpicy] = useState(0);
  const [customCreating, setCustomCreating] = useState(false);
  const [modalError, setModalError] = useState('');

  // Added notification feedback
  const [recentlyAdded, setRecentlyAdded] = useState<string | null>(null);

  const categories = ['All', 'Produce', 'Spice', 'Herb', 'Dairy', 'Pantry', 'Grain', 'Legume'];
  const cuisines = ['All', 'Indian', 'Mediterranean', 'Italian', 'Mexican', 'Southeast Asian', 'Global'];
  const allergenOptions = ['Dairy', 'Nuts', 'Soy', 'Gluten', 'Sesame'];

  useEffect(() => {
    loadIngredients();
  }, [selectedCategory, selectedCuisine, excludeAllergen]);

  const loadIngredients = async () => {
    setLoading(true);
    try {
      const data = await api.ingredients.getAll({
        category: selectedCategory !== 'All' ? selectedCategory : undefined,
        cuisine: selectedCuisine !== 'All' ? selectedCuisine : undefined,
        exclude_allergen: excludeAllergen || undefined,
      });
      setIngredients(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const filteredIngredients = ingredients.filter((ing) => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      ing.name.toLowerCase().includes(q) ||
      ing.category.toLowerCase().includes(q) ||
      (ing.description && ing.description.toLowerCase().includes(q)) ||
      (ing.flavor_profile?.primary_aromas || []).some((a) => a.toLowerCase().includes(q))
    );
  });

  const handleAddToLab = (name: string, unit: string) => {
    onAddIngredientToLab(name, 100, unit, 'Raw');
    setRecentlyAdded(name);
    setTimeout(() => setRecentlyAdded(null), 2500);
  };

  const handleCreateCustom = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!customName.trim()) {
      setModalError('Please enter an ingredient name.');
      return;
    }
    setCustomCreating(true);
    setModalError('');
    try {
      const created = await api.ingredients.create({
        name: customName.trim(),
        category: customCategory,
        description: customDescription,
        default_unit: customUnit,
        allergens: [],
        cuisines: ['Custom'],
        flavor_profile: {
          sweet: customSweet,
          sour: customSour,
          salty: customSalty,
          bitter: customBitter,
          umami: customUmami,
          spicy: customSpicy,
          intensity: 5.0,
          primary_aromas: ['Custom'],
          texture_profile: ['Custom'],
          dominant_compounds: [],
        },
      });
      setShowCustomModal(false);
      setCustomName('');
      setCustomDescription('');
      loadIngredients();
      handleAddToLab(created.name, created.default_unit);
    } catch (err: any) {
      setModalError(err.message || 'Error creating custom ingredient');
    } finally {
      setCustomCreating(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Toast Alert */}
      {recentlyAdded && (
        <div className="fixed bottom-6 right-6 z-50 bg-forest-700 text-ivory-50 px-5 py-3 rounded-2xl shadow-xl flex items-center space-x-2 border border-forest-500 animate-fade-in">
          <Check className="w-4 h-4 text-sage-300" />
          <span className="text-sm font-semibold">Added "{recentlyAdded}" to Flavor Lab</span>
        </div>
      )}

      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
            Ingredient Explorer
          </h1>
          <p className="text-sm text-stone-600 dark:text-stone-300 mt-1">
            Browse 65+ curated culinary ingredients with basic taste metrics and aroma compound profiles.
          </p>
        </div>

        <button
          onClick={() => setShowCustomModal(true)}
          className="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-sm transition-all self-start md:self-auto"
        >
          <Plus className="w-4 h-4" />
          <span>Add Custom Ingredient</span>
        </button>
      </div>

      {/* Filter and Search Bar */}
      <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-4">
        {/* Search input */}
        <div className="relative">
          <Search className="w-5 h-5 text-stone-400 absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by ingredient name, aroma (e.g. Cineole, Fruity, Woody), or description..."
            className="w-full pl-11 pr-4 py-2.5 rounded-xl bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 text-sm text-stone-900 dark:text-ivory-100 focus:outline-none focus:ring-2 focus:ring-forest-500"
          />
        </div>

        {/* Categories Bar */}
        <div className="flex items-center space-x-2 overflow-x-auto pb-1 scrollbar-thin">
          <span className="text-xs font-semibold text-stone-500 dark:text-stone-400 uppercase tracking-wider whitespace-nowrap mr-1">
            Category:
          </span>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap transition-all ${
                selectedCategory === cat
                  ? 'bg-forest-600 text-white shadow-sm'
                  : 'bg-ivory-200 dark:bg-forest-900/60 text-stone-700 dark:text-stone-300 hover:bg-ivory-300 dark:hover:bg-forest-800'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Cuisine & Allergen Filter Line */}
        <div className="flex flex-wrap items-center gap-4 pt-2 border-t border-ivory-200 dark:border-forest-900 text-xs">
          <div className="flex items-center space-x-2">
            <span className="font-semibold text-stone-500 dark:text-stone-400">Cuisine:</span>
            <select
              value={selectedCuisine}
              onChange={(e) => setSelectedCuisine(e.target.value)}
              className="px-2.5 py-1 rounded-lg bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs focus:outline-none focus:ring-1 focus:ring-forest-500"
            >
              {cuisines.map((c) => (
                <option key={c} value={c}>{c}</option>
              ))}
            </select>
          </div>

          <div className="flex items-center space-x-2">
            <span className="font-semibold text-stone-500 dark:text-stone-400">Exclude Allergen:</span>
            <select
              value={excludeAllergen}
              onChange={(e) => setExcludeAllergen(e.target.value)}
              className="px-2.5 py-1 rounded-lg bg-white dark:bg-[#1b2420] border border-ivory-300 dark:border-forest-800 text-stone-800 dark:text-ivory-100 text-xs focus:outline-none focus:ring-1 focus:ring-forest-500"
            >
              <option value="">None (Show All)</option>
              {allergenOptions.map((a) => (
                <option key={a} value={a}>{a}</option>
              ))}
            </select>
          </div>

          <div className="ml-auto text-stone-400 font-mono text-xs">
            Showing {filteredIngredients.length} ingredients
          </div>
        </div>
      </div>

      {/* Grid of Ingredients */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="h-64 rounded-2xl bg-ivory-200 dark:bg-[#151c19] animate-pulse border border-ivory-300 dark:border-forest-900" />
          ))}
        </div>
      ) : filteredIngredients.length === 0 ? (
        <div className="text-center py-16 bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-3">
          <Info className="w-10 h-10 text-stone-400 mx-auto" />
          <h3 className="font-serif text-lg font-bold text-stone-800 dark:text-ivory-100">No ingredients found</h3>
          <p className="text-xs text-stone-500 dark:text-stone-400 max-w-sm mx-auto">
            Try adjusting your search query, clearing your filters, or create a custom ingredient.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredIngredients.map((ing) => {
            const fp = ing.flavor_profile;
            return (
              <div
                key={ing.id}
                className="bg-white dark:bg-[#151c19] rounded-2xl p-5 border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:border-forest-400 dark:hover:border-forest-600 hover:shadow-md transition-all group"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2 py-0.5 rounded border border-sage-200 dark:border-forest-800">
                      {ing.category}
                    </span>
                    {ing.allergens.length > 0 && (
                      <span className="text-[10px] font-semibold text-terracotta-700 dark:text-terracotta-300 bg-terracotta-50 dark:bg-terracotta-900/30 px-2 py-0.5 rounded border border-terracotta-200 dark:border-terracotta-800">
                        Allergen: {ing.allergens.join(', ')}
                      </span>
                    )}
                  </div>

                  <div>
                    <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50 group-hover:text-forest-700 dark:group-hover:text-sage-300 transition-colors">
                      {ing.name}
                    </h3>
                    <p className="text-xs text-stone-500 dark:text-stone-400 line-clamp-2 mt-1 leading-relaxed">
                      {ing.description || 'Rich culinary ingredient.'}
                    </p>
                  </div>

                  {/* Basic Taste Mini Bars */}
                  {fp && (
                    <div className="space-y-1.5 pt-2 border-t border-ivory-200 dark:border-forest-900">
                      <div className="grid grid-cols-3 gap-2 text-[10px] text-stone-600 dark:text-stone-400 font-medium">
                        <div className="space-y-0.5">
                          <div className="flex justify-between">
                            <span>Sweet</span>
                            <span className="font-mono">{fp.sweet}</span>
                          </div>
                          <div className="h-1 bg-ivory-200 dark:bg-[#1b2420] rounded-full overflow-hidden">
                            <div className="h-full bg-forest-600 rounded-full" style={{ width: `${fp.sweet * 10}%` }} />
                          </div>
                        </div>
                        <div className="space-y-0.5">
                          <div className="flex justify-between">
                            <span>Sour</span>
                            <span className="font-mono">{fp.sour}</span>
                          </div>
                          <div className="h-1 bg-ivory-200 dark:bg-[#1b2420] rounded-full overflow-hidden">
                            <div className="h-full bg-sage-500 rounded-full" style={{ width: `${fp.sour * 10}%` }} />
                          </div>
                        </div>
                        <div className="space-y-0.5">
                          <div className="flex justify-between">
                            <span>Umami</span>
                            <span className="font-mono">{fp.umami}</span>
                          </div>
                          <div className="h-1 bg-ivory-200 dark:bg-[#1b2420] rounded-full overflow-hidden">
                            <div className="h-full bg-terracotta-500 rounded-full" style={{ width: `${fp.umami * 10}%` }} />
                          </div>
                        </div>
                      </div>

                      {/* Aroma Tags */}
                      {fp.primary_aromas.length > 0 && (
                        <div className="flex flex-wrap gap-1 pt-1">
                          {fp.primary_aromas.slice(0, 3).map((a) => (
                            <span key={a} className="text-[10px] bg-ivory-100 dark:bg-[#1d2622] text-stone-600 dark:text-stone-300 px-1.5 py-0.5 rounded">
                              #{a}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>

                {/* Add to Lab action */}
                <div className="pt-4 border-t border-ivory-200 dark:border-forest-900 mt-4 flex items-center justify-between">
                  <span className="text-[11px] text-stone-400 font-medium">Default: 100{ing.default_unit}</span>
                  <button
                    onClick={() => handleAddToLab(ing.name, ing.default_unit)}
                    className="flex items-center space-x-1 px-3.5 py-1.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-xs font-semibold shadow-sm transition-all"
                  >
                    <Plus className="w-3.5 h-3.5" />
                    <span>Add to Lab</span>
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Custom Ingredient Creation Modal */}
      {showCustomModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/80 backdrop-blur-sm">
          <div className="relative w-full max-w-lg bg-ivory-50 dark:bg-[#18201d] rounded-2xl shadow-2xl border border-ivory-300 dark:border-forest-900 p-6 space-y-5 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-3 border-b border-ivory-200 dark:border-forest-900">
              <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-100">Add Custom Ingredient</h3>
              <button
                onClick={() => setShowCustomModal(false)}
                className="p-1 rounded-lg text-stone-400 hover:text-stone-700 dark:hover:text-stone-200"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {modalError && (
              <div className="p-3 bg-terracotta-50 dark:bg-terracotta-950/40 border border-terracotta-200 dark:border-terracotta-800 text-terracotta-700 dark:text-terracotta-300 text-xs rounded-xl flex items-center space-x-2">
                <AlertTriangle className="w-4 h-4 shrink-0" />
                <span>{modalError}</span>
              </div>
            )}

            <form onSubmit={handleCreateCustom} className="space-y-4 text-xs">
              <div>
                <label className="block font-semibold text-stone-800 dark:text-stone-200 mb-1">Ingredient Name</label>
                <input
                  type="text"
                  required
                  value={customName}
                  onChange={(e) => setCustomName(e.target.value)}
                  placeholder="e.g. Saffron Rose Syrup, Dragonfruit Powder"
                  className="w-full px-3 py-2 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#121815] text-stone-800 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-semibold text-stone-800 dark:text-stone-200 mb-1">Category</label>
                  <select
                    value={customCategory}
                    onChange={(e) => setCustomCategory(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#121815] text-stone-800 dark:text-ivory-100 text-xs"
                  >
                    {categories.filter((c) => c !== 'All').map((c) => (
                      <option key={c} value={c}>{c}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block font-semibold text-stone-800 dark:text-stone-200 mb-1">Default Unit</label>
                  <select
                    value={customUnit}
                    onChange={(e) => setCustomUnit(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#121815] text-stone-800 dark:text-ivory-100 text-xs"
                  >
                    <option value="g">Grams (g)</option>
                    <option value="ml">Milliliters (ml)</option>
                    <option value="piece">Piece (pc)</option>
                    <option value="pinch">Pinch</option>
                    <option value="tbsp">Tablespoon</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block font-semibold text-stone-800 dark:text-stone-200 mb-1">Description</label>
                <textarea
                  value={customDescription}
                  onChange={(e) => setCustomDescription(e.target.value)}
                  placeholder="Describe its culinary origin, volatile aromatics, or flavor nuances..."
                  className="w-full px-3 py-2 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#121815] text-stone-800 dark:text-ivory-100 text-xs h-16 focus:outline-none"
                />
              </div>

              {/* Basic Taste Sliders (0 - 10) */}
              <div className="space-y-3 pt-2 border-t border-ivory-200 dark:border-forest-900">
                <span className="font-semibold text-stone-800 dark:text-stone-200 block text-xs">Estimated Taste Profile (0 - 10 scale):</span>
                <div className="grid grid-cols-2 gap-x-4 gap-y-2">
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Sweet</span>
                      <span className="font-mono">{customSweet}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customSweet}
                      onChange={(e) => setCustomSweet(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Sour</span>
                      <span className="font-mono">{customSour}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customSour}
                      onChange={(e) => setCustomSour(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Salty</span>
                      <span className="font-mono">{customSalty}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customSalty}
                      onChange={(e) => setCustomSalty(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Bitter</span>
                      <span className="font-mono">{customBitter}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customBitter}
                      onChange={(e) => setCustomBitter(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Umami</span>
                      <span className="font-mono">{customUmami}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customUmami}
                      onChange={(e) => setCustomUmami(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                  <div>
                    <div className="flex justify-between text-[11px] mb-0.5 text-stone-600 dark:text-stone-400">
                      <span>Spicy</span>
                      <span className="font-mono">{customSpicy}/10</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={customSpicy}
                      onChange={(e) => setCustomSpicy(Number(e.target.value))}
                      className="w-full accent-forest-600"
                    />
                  </div>
                </div>
              </div>

              <div className="pt-4 border-t border-ivory-200 dark:border-forest-900 flex justify-end space-x-2">
                <button
                  type="button"
                  onClick={() => setShowCustomModal(false)}
                  className="px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900 text-stone-700 dark:text-stone-300 hover:bg-ivory-300 dark:hover:bg-forest-800 font-semibold text-xs"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={customCreating}
                  className="px-5 py-2 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-xs shadow-sm disabled:opacity-50"
                >
                  {customCreating ? 'Saving...' : 'Save & Add to Lab'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
