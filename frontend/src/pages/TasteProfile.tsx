import React, { useState, useEffect } from 'react';
import {
  User,
  Save,
  CheckCircle,
  AlertCircle,
  ShieldAlert,
  Sparkles,
  Heart,
  ThumbsDown,
} from 'lucide-react';
import { api } from '../services/api';
import { UserPreferences } from '../types';

export const TasteProfile: React.FC = () => {
  const [preferences, setPreferences] = useState<UserPreferences>({
    preferred_cuisines: ['Indian', 'Mediterranean'],
    favorite_ingredients: ['Mango', 'Cardamom', 'Garlic'],
    disliked_ingredients: ['Bitter Gourd'],
    texture_preferences: ['Creamy', 'Crispy'],
    aroma_preferences: ['Citrus', 'Warm Spice'],
    spice_tolerance: 3,
    sweet_affinity: 4,
    sour_affinity: 3,
    bitter_affinity: 2,
    umami_affinity: 4,
    salty_affinity: 3,
    dietary_preferences: ['Vegetarian'],
    allergies: [],
    budget_preference: 'Moderate',
    prep_time_preference: 30,
    adventurousness: 4,
  });

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // New ingredient chip inputs
  const [favInput, setFavInput] = useState('');
  const [dislikeInput, setDislikeInput] = useState('');
  const [allergyInput, setAllergyInput] = useState('');

  const allergyOptions = [
    'Dairy / Lactose',
    'Peanuts',
    'Tree Nuts (Cashew, Almond, Walnut)',
    'Gluten / Wheat',
    'Shellfish & Crustaceans',
    'Fish & Marine',
    'Soy & Soybeans',
    'Eggs',
    'Mustard & Mustard Seeds',
    'Sesame Seeds',
    'Nightshades (Tomato, Eggplant)',
    'Alliums (Garlic, Onion)',
    'Mushrooms / Fungi',
    'Sulfites',
  ];

  const cuisineOptions = [
    'Indian',
    'Mediterranean',
    'Italian',
    'Mexican',
    'Japanese',
    'French',
    'Thai',
    'Middle Eastern',
  ];

  const dietaryOptions = [
    'Vegetarian',
    'Vegan',
    'Gluten-Free',
    'Dairy-Free',
    'Keto',
    'Paleo',
    'Halal',
    'Kosher',
  ];

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    setLoading(true);
    try {
      const data = await api.users.getPreferences();
      setPreferences(data);
    } catch (err: any) {
      console.warn('Preferences fetch fallback:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);
    setError(null);
    setSuccess(false);

    try {
      await api.users.updatePreferences(preferences);
      setSuccess(true);
      setTimeout(() => setSuccess(false), 4000);
    } catch (err: any) {
      setError(err.message || 'Failed to save taste profile.');
    } finally {
      setSaving(false);
    }
  };

  const toggleArrayItem = (key: 'allergies' | 'preferred_cuisines' | 'dietary_preferences', item: string) => {
    const list = [...preferences[key]];
    const index = list.indexOf(item);
    if (index > -1) {
      list.splice(index, 1);
    } else {
      list.push(item);
    }
    setPreferences({ ...preferences, [key]: list });
  };

  const addFavorite = () => {
    if (!favInput.trim()) return;
    const clean = favInput.trim();
    if (!preferences.favorite_ingredients.includes(clean)) {
      setPreferences({
        ...preferences,
        favorite_ingredients: [...preferences.favorite_ingredients, clean],
      });
    }
    setFavInput('');
  };

  const removeFavorite = (name: string) => {
    setPreferences({
      ...preferences,
      favorite_ingredients: preferences.favorite_ingredients.filter((i: string) => i !== name),
    });
  };

  const addDisliked = () => {
    if (!dislikeInput.trim()) return;
    const clean = dislikeInput.trim();
    if (!preferences.disliked_ingredients.includes(clean)) {
      setPreferences({
        ...preferences,
        disliked_ingredients: [...preferences.disliked_ingredients, clean],
      });
    }
    setDislikeInput('');
  };

  const removeDisliked = (name: string) => {
    setPreferences({
      ...preferences,
      disliked_ingredients: preferences.disliked_ingredients.filter((i: string) => i !== name),
    });
  };

  const addAllergyFood = () => {
    if (!allergyInput.trim()) return;
    const clean = allergyInput.trim();
    if (!preferences.allergies.includes(clean)) {
      setPreferences({
        ...preferences,
        allergies: [...preferences.allergies, clean],
      });
    }
    setAllergyInput('');
  };

  const removeAllergyFood = (name: string) => {
    setPreferences({
      ...preferences,
      allergies: preferences.allergies.filter((i: string) => i !== name),
    });
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header */}
      <div className="space-y-2">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-forest-600/10 dark:bg-forest-900/60 text-forest-700 dark:text-sage-300 text-xs font-semibold border border-forest-600/20 dark:border-forest-800">
          <Sparkles className="w-3.5 h-3.5 text-forest-600 dark:text-sage-400" />
          <span>Flavor Identity Engine</span>
        </div>
        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
          My Taste Profile
        </h1>
        <p className="text-sm text-stone-600 dark:text-stone-300">
          Calibrate your personal palate parameters. The recommendation engine weights your favorite spices, hard exclusions, and flavor affinities to surface personalized matches.
        </p>
      </div>

      {success && (
        <div className="p-4 rounded-2xl bg-sage-50 dark:bg-forest-950/60 border border-sage-300 dark:border-forest-800 text-forest-800 dark:text-sage-200 text-xs flex items-center space-x-2">
          <CheckCircle className="w-4 h-4 text-forest-600 dark:text-sage-300 shrink-0" />
          <span>Taste profile saved! Flavor Lab and Discover recommendations updated.</span>
        </div>
      )}

      {error && (
        <div className="p-4 rounded-2xl bg-terracotta-50 dark:bg-terracotta-950/60 border border-terracotta-300 dark:border-terracotta-800 text-terracotta-800 dark:text-terracotta-200 text-xs flex items-center space-x-2">
          <AlertCircle className="w-4 h-4 text-terracotta-600 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      <form onSubmit={handleSave} className="space-y-8">
        {/* Hard Allergy Foods & Exclusions Card */}
        <div className="bg-terracotta-50/70 dark:bg-terracotta-950/40 p-6 rounded-3xl border border-terracotta-200 dark:border-terracotta-900/60 shadow-xs space-y-4">
          <div className="flex items-center space-x-2 text-terracotta-800 dark:text-terracotta-300">
            <ShieldAlert className="w-5 h-5 text-terracotta-600" />
            <h3 className="font-serif text-lg font-bold">Allergic Foods & Hard Exclusions</h3>
          </div>
          <p className="text-xs text-stone-600 dark:text-stone-300 leading-relaxed">
            Specify foods or allergens you are allergic to. Any recipe or combination containing these ingredients will trigger a <strong className="text-terracotta-700 dark:text-terracotta-300">strict safety alert and 0% match score</strong>.
          </p>

          {/* Quick Category Buttons */}
          <div>
            <span className="text-[11px] font-semibold text-terracotta-800/80 dark:text-terracotta-300/80 uppercase tracking-wider block mb-2">
              Common Allergy Groups:
            </span>
            <div className="flex flex-wrap gap-2">
              {allergyOptions.map((allergen) => {
                const isChecked = preferences.allergies.includes(allergen);
                return (
                  <button
                    type="button"
                    key={allergen}
                    onClick={() => toggleArrayItem('allergies', allergen)}
                    className={`px-3 py-1.5 rounded-xl text-xs font-semibold border transition-all cursor-pointer ${
                      isChecked
                        ? 'bg-terracotta-600 text-white border-terracotta-600 shadow-xs'
                        : 'bg-white dark:bg-[#1b2320] text-stone-700 dark:text-stone-300 border-terracotta-200 dark:border-terracotta-900/60 hover:bg-terracotta-100 dark:hover:bg-terracotta-900/30'
                    }`}
                  >
                    {isChecked ? `✕ ${allergen} (Excluded)` : `+ ${allergen}`}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Custom Allergy Food Input */}
          <div className="pt-2 border-t border-terracotta-200/60 dark:border-terracotta-900/40">
            <span className="text-[11px] font-semibold text-terracotta-800/80 dark:text-terracotta-300/80 uppercase tracking-wider block mb-2">
              Add Specific Allergic Food:
            </span>
            <div className="flex space-x-2">
              <input
                type="text"
                value={allergyInput}
                onChange={(e) => setAllergyInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && (e.preventDefault(), addAllergyFood())}
                placeholder="e.g. Cashews, Brinjal, Mustard, Crab, Sesame..."
                className="w-full px-3.5 py-2 rounded-xl border border-terracotta-200 dark:border-terracotta-900 bg-white dark:bg-[#1b2320] text-stone-900 dark:text-ivory-100 placeholder-stone-400 text-xs focus:outline-none focus:ring-2 focus:ring-terracotta-500"
              />
              <button
                type="button"
                onClick={addAllergyFood}
                className="px-4 py-2 rounded-xl bg-terracotta-700 hover:bg-terracotta-600 text-white font-semibold text-xs transition-colors shrink-0 cursor-pointer shadow-xs"
              >
                + Add Food
              </button>
            </div>

            {/* Active Allergic Foods List */}
            {preferences.allergies.length > 0 && (
              <div className="mt-3">
                <span className="text-[11px] text-stone-500 dark:text-stone-400 mb-1.5 block">
                  Active Excluded Allergic Foods ({preferences.allergies.length}):
                </span>
                <div className="flex flex-wrap gap-1.5">
                  {preferences.allergies.map((allergy) => (
                    <span
                      key={allergy}
                      onClick={() => removeAllergyFood(allergy)}
                      className="cursor-pointer px-2.5 py-1 rounded-xl bg-terracotta-100 dark:bg-terracotta-900/60 text-terracotta-800 dark:text-terracotta-200 text-xs font-semibold border border-terracotta-300 dark:border-terracotta-800 hover:bg-rose-100 dark:hover:bg-rose-950 transition-colors flex items-center gap-1.5"
                      title="Click to remove exclusion"
                    >
                      <span>{allergy}</span>
                      <span className="text-terracotta-600 dark:text-terracotta-400 font-bold">✕</span>
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Basic Taste Affinities */}
        <div className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-xs space-y-6">
          <div>
            <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">Basic Taste Affinities</h3>
            <p className="text-xs text-stone-500 dark:text-stone-400 mt-0.5">Rate your preference for each primary taste spectrum (1: Low, 5: Love it).</p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 text-xs">
            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Sweet Affinity</span>
                <span className="font-mono text-forest-700 dark:text-sage-400">{preferences.sweet_affinity} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.sweet_affinity}
                onChange={(e) => setPreferences({ ...preferences, sweet_affinity: Number(e.target.value) })}
                className="w-full accent-forest-600"
              />
            </div>

            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Sour / Tangy Affinity</span>
                <span className="font-mono text-forest-700 dark:text-sage-400">{preferences.sour_affinity} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.sour_affinity}
                onChange={(e) => setPreferences({ ...preferences, sour_affinity: Number(e.target.value) })}
                className="w-full accent-forest-600"
              />
            </div>

            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Umami / Savory Affinity</span>
                <span className="font-mono text-forest-700 dark:text-sage-400">{preferences.umami_affinity} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.umami_affinity}
                onChange={(e) => setPreferences({ ...preferences, umami_affinity: Number(e.target.value) })}
                className="w-full accent-forest-600"
              />
            </div>

            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Bitter Tolerance</span>
                <span className="font-mono text-forest-700 dark:text-sage-400">{preferences.bitter_affinity} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.bitter_affinity}
                onChange={(e) => setPreferences({ ...preferences, bitter_affinity: Number(e.target.value) })}
                className="w-full accent-forest-600"
              />
            </div>

            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Spice & Heat Tolerance</span>
                <span className="font-mono text-terracotta-600 dark:text-terracotta-400">{preferences.spice_tolerance} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.spice_tolerance}
                onChange={(e) => setPreferences({ ...preferences, spice_tolerance: Number(e.target.value) })}
                className="w-full accent-terracotta-600"
              />
            </div>

            <div>
              <div className="flex justify-between font-semibold text-stone-800 dark:text-stone-200 mb-1">
                <span>Culinary Adventurousness</span>
                <span className="font-mono text-forest-700 dark:text-sage-400">{preferences.adventurousness} / 5</span>
              </div>
              <input
                type="range"
                min="1"
                max="5"
                value={preferences.adventurousness}
                onChange={(e) => setPreferences({ ...preferences, adventurousness: Number(e.target.value) })}
                className="w-full accent-forest-600"
              />
            </div>
          </div>
        </div>

        {/* Favorite & Disliked Ingredients */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {/* Favorites */}
          <div className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-xs space-y-4 text-xs">
            <div className="flex items-center space-x-2 text-forest-800 dark:text-sage-300 font-serif text-base font-bold">
              <Heart className="w-4 h-4 text-terracotta-500 fill-terracotta-500" />
              <span>Favorite Ingredients</span>
            </div>
            <div className="flex space-x-2">
              <input
                type="text"
                value={favInput}
                onChange={(e) => setFavInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && (e.preventDefault(), addFavorite())}
                placeholder="e.g. Cardamom, Mango"
                className="w-full px-3 py-1.5 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#1b2320] text-stone-900 dark:text-ivory-100 placeholder-stone-400"
              />
              <button
                type="button"
                onClick={addFavorite}
                className="px-3 py-1.5 rounded-xl bg-forest-600 text-white font-semibold cursor-pointer"
              >
                Add
              </button>
            </div>
            <div className="flex flex-wrap gap-1.5 pt-1">
              {preferences.favorite_ingredients.map((item: string) => (
                <span
                  key={item}
                  onClick={() => removeFavorite(item)}
                  className="cursor-pointer px-2.5 py-1 rounded-xl bg-sage-100 dark:bg-forest-900/60 text-forest-700 dark:text-sage-300 font-semibold border border-sage-200 dark:border-forest-800 hover:bg-terracotta-50 dark:hover:bg-terracotta-900/40 hover:text-terracotta-700 dark:hover:text-terracotta-300 transition-colors"
                >
                  {item} ✕
                </span>
              ))}
            </div>
          </div>

          {/* Disliked */}
          <div className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-xs space-y-4 text-xs">
            <div className="flex items-center space-x-2 text-stone-800 dark:text-stone-200 font-serif text-base font-bold">
              <ThumbsDown className="w-4 h-4 text-stone-500" />
              <span>Disliked Ingredients</span>
            </div>
            <div className="flex space-x-2">
              <input
                type="text"
                value={dislikeInput}
                onChange={(e) => setDislikeInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && (e.preventDefault(), addDisliked())}
                placeholder="e.g. Bitter Gourd, Cilantro"
                className="w-full px-3 py-1.5 rounded-xl border border-ivory-300 dark:border-forest-800 bg-white dark:bg-[#1b2320] text-stone-900 dark:text-ivory-100 placeholder-stone-400"
              />
              <button
                type="button"
                onClick={addDisliked}
                className="px-3 py-1.5 rounded-xl bg-stone-700 dark:bg-forest-800 text-white font-semibold cursor-pointer"
              >
                Add
              </button>
            </div>
            <div className="flex flex-wrap gap-1.5 pt-1">
              {preferences.disliked_ingredients.map((item: string) => (
                <span
                  key={item}
                  onClick={() => removeDisliked(item)}
                  className="cursor-pointer px-2.5 py-1 rounded-xl bg-ivory-200 dark:bg-[#1b2320] text-stone-700 dark:text-stone-300 font-semibold border border-ivory-300 dark:border-forest-800 hover:bg-terracotta-50 dark:hover:bg-terracotta-900/40 hover:text-terracotta-700 dark:hover:text-terracotta-300 transition-colors"
                >
                  {item} ✕
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Preferred Cuisines & Dietary */}
        <div className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-xs space-y-6">
          <div className="space-y-3">
            <h3 className="font-serif text-base font-bold text-stone-900 dark:text-ivory-50">Preferred Cuisines</h3>
            <div className="flex flex-wrap gap-2 text-xs">
              {cuisineOptions.map((c) => {
                const isSelected = preferences.preferred_cuisines.includes(c);
                return (
                  <button
                    type="button"
                    key={c}
                    onClick={() => toggleArrayItem('preferred_cuisines', c)}
                    className={`px-3 py-1.5 rounded-xl font-semibold border transition-all cursor-pointer ${
                      isSelected
                        ? 'bg-forest-600 text-white border-forest-600 shadow-xs'
                        : 'bg-white dark:bg-[#1b2320] text-stone-700 dark:text-stone-300 border-ivory-300 dark:border-forest-800 hover:bg-ivory-200 dark:hover:bg-forest-900/60'
                    }`}
                  >
                    {c}
                  </button>
                );
              })}
            </div>
          </div>

          <div className="space-y-3 pt-4 border-t border-ivory-200 dark:border-forest-900">
            <h3 className="font-serif text-base font-bold text-stone-900 dark:text-ivory-50">Dietary Style</h3>
            <div className="flex flex-wrap gap-2 text-xs">
              {dietaryOptions.map((d) => {
                const isSelected = preferences.dietary_preferences.includes(d);
                return (
                  <button
                    type="button"
                    key={d}
                    onClick={() => toggleArrayItem('dietary_preferences', d)}
                    className={`px-3 py-1.5 rounded-xl font-semibold border transition-all cursor-pointer ${
                      isSelected
                        ? 'bg-sage-600 dark:bg-forest-600 text-white border-sage-600 dark:border-forest-600 shadow-xs'
                        : 'bg-white dark:bg-[#1b2320] text-stone-700 dark:text-stone-300 border-ivory-300 dark:border-forest-800 hover:bg-ivory-200 dark:hover:bg-forest-900/60'
                    }`}
                  >
                    {d}
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Submit */}
        <div className="flex justify-end pt-2">
          <button
            type="submit"
            disabled={saving}
            className="flex items-center space-x-2 px-8 py-3 rounded-2xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-md transition-all disabled:opacity-50 cursor-pointer"
          >
            <Save className="w-4 h-4 text-sage-200" />
            <span>{saving ? 'Updating Palate Parameters...' : 'Save Taste Profile'}</span>
          </button>
        </div>
      </form>
    </div>
  );
};
