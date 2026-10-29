import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Sparkles,
  FlaskConical,
  Camera,
  Compass,
  ArrowRight,
  CheckCircle2,
  Flame,
  Search,
  BookOpen,
  Atom,
  Eye,
  Sliders,
  ChefHat,
  Zap
} from 'lucide-react';
import { api } from '../services/api';
import { Ingredient, RecommendationItem } from '../types';
import { CompatibilityGauge } from '../components/CompatibilityGauge';

interface HomePageProps {
  onAddIngredientToLab: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const HomePage: React.FC<HomePageProps> = ({ onAddIngredientToLab }) => {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Ingredient[]>([]);
  const [featuredPairings, setFeaturedPairings] = useState<RecommendationItem[]>([]);
  const [loadingPairings, setLoadingPairings] = useState(true);

  useEffect(() => {
    loadFeatured();
  }, []);

  const loadFeatured = async () => {
    try {
      const data = await api.recommendations.getPersonalized({ limit: 3 });
      setFeaturedPairings(data);
    } catch {
      // fallback silent
    } finally {
      setLoadingPairings(false);
    }
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    try {
      const results = await api.ingredients.search(searchQuery);
      setSearchResults(results);
    } catch {
      setSearchResults([]);
    }
  };

  const loadExampleToLab = () => {
    const sample = [
      { name: 'Mango', quantity: 150, unit: 'g', prep: 'Raw' },
      { name: 'Curd', quantity: 100, unit: 'g', prep: 'Raw' },
      { name: 'Cardamom', quantity: 2, unit: 'g', prep: 'Raw' },
      { name: 'Mint', quantity: 5, unit: 'g', prep: 'Raw' },
      { name: 'Lime', quantity: 10, unit: 'ml', prep: 'Raw' },
      { name: 'Roasted Cumin', quantity: 2, unit: 'g', prep: 'Roasted' },
      { name: 'Honey', quantity: 20, unit: 'g', prep: 'Raw' },
    ];
    sample.forEach((item) => onAddIngredientToLab(item.name, item.quantity, item.unit, item.prep));
    navigate('/lab');
  };

  const loadIllusionToLab = (ingredients: { name: string; quantity: number; unit: string; prep: string }[]) => {
    ingredients.forEach((item) => onAddIngredientToLab(item.name, item.quantity, item.unit, item.prep));
    navigate('/lab');
  };

  const flavorIllusions = [
    {
      title: 'Vanilla Ice Cream + Soy Sauce',
      tastesLike: 'Rich Salted Caramel & Toasted Toffee',
      vibe: 'Certified Banger 🔥',
      why: 'Sodium suppresses perceived bitterness, while glutamates supercharge vanillin into decadent, butterscotch-caramel illusion.',
      ingredients: [
        { name: 'Vanilla', quantity: 100, unit: 'g', prep: 'Raw' },
        { name: 'Soy Sauce', quantity: 15, unit: 'ml', prep: 'Raw' }
      ]
    },
    {
      title: 'Strawberries + Balsamic Vinegar',
      tastesLike: 'Deep Macerated Blackberry Jam',
      vibe: 'Mindblown 🤯',
      why: 'Acetic acid unlocks volatile fruity esters in strawberry flesh, transforming fresh berries into rich wine-macerated preserve.',
      ingredients: [
        { name: 'Strawberry', quantity: 150, unit: 'g', prep: 'Raw' },
        { name: 'Balsamic Vinegar', quantity: 20, unit: 'ml', prep: 'Raw' },
        { name: 'Black Pepper', quantity: 1, unit: 'g', prep: 'Raw' }
      ]
    },
    {
      title: 'Watermelon + Feta + Mint',
      tastesLike: 'Crisp Saline Mediterranean Cloud',
      vibe: 'Chef Kiss ✨',
      why: 'High-moisture citrulline sweet water buffered by briny sheep-milk curds and cold menthol leaves.',
      ingredients: [
        { name: 'Watermelon', quantity: 200, unit: 'g', prep: 'Raw' },
        { name: 'Feta', quantity: 50, unit: 'g', prep: 'Raw' },
        { name: 'Mint', quantity: 5, unit: 'g', prep: 'Raw' }
      ]
    },
    {
      title: 'Dark Chocolate + Chili Flakes',
      tastesLike: 'Aztec Molten Fire & Roasted Ganache',
      vibe: 'Dopamine Hit 🌶️',
      why: 'Capsaicin stimulates tongue endorphins, heightening perception of theobromine and roasted cacao nibs.',
      ingredients: [
        { name: 'Dark Chocolate', quantity: 60, unit: 'g', prep: 'Raw' },
        { name: 'Chili Pepper', quantity: 3, unit: 'g', prep: 'Roasted' },
        { name: 'Olive Oil', quantity: 10, unit: 'ml', prep: 'Raw' }
      ]
    }
  ];

  return (
    <div className="space-y-24 pb-20">
      {/* Hero Section */}
      <section className="relative pt-12 pb-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
        <div className="text-center max-w-3xl mx-auto space-y-6">
          <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-sage-100 dark:bg-forest-900/60 text-forest-700 dark:text-sage-300 text-xs font-semibold border border-sage-200 dark:border-forest-800 shadow-sm">
            <Sparkles className="w-4 h-4 text-forest-600 dark:text-sage-400" />
            <span>AI Food Chemistry & Personalized Palate Matching</span>
          </div>

          <h1 className="font-serif text-4xl sm:text-5xl lg:text-6xl font-extrabold text-stone-900 dark:text-ivory-50 tracking-tight leading-[1.15]">
            Discover how your favorite foods <span className="text-forest-700 dark:text-sage-400 italic">taste together</span>
          </h1>

          <p className="text-base sm:text-lg text-stone-600 dark:text-stone-300 leading-relaxed font-normal">
            FlavorFusion AI analyzes multi-ingredient culinary compatibility, sensory flavor illusions (like Vanilla + Soy Sauce tasting like Salted Caramel!), volatile aroma overlap, and your unique palate.
          </p>

          {/* Primary CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
            <Link
              to="/lab"
              className="w-full sm:w-auto flex items-center justify-center space-x-2 px-7 py-3.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-base shadow-md transition-all group"
            >
              <FlaskConical className="w-5 h-5 text-sage-200 group-hover:rotate-12 transition-transform" />
              <span>Launch Flavor Lab</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
            <Link
              to="/vision"
              className="w-full sm:w-auto flex items-center justify-center space-x-2 px-6 py-3.5 rounded-xl bg-ivory-50 dark:bg-[#18201d] hover:bg-ivory-200 dark:hover:bg-forest-900 text-stone-800 dark:text-stone-200 font-semibold text-base border border-ivory-300 dark:border-forest-800 shadow-sm transition-all"
            >
              <Camera className="w-5 h-5 text-terracotta-600 dark:text-terracotta-400" />
              <span>Scan Food Photo</span>
            </Link>
          </div>

          {/* Search bar inside hero */}
          <form onSubmit={handleSearch} className="pt-4 max-w-xl mx-auto relative">
            <div className="relative flex items-center">
              <Search className="w-5 h-5 text-stone-400 absolute left-4 pointer-events-none" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search ingredients (e.g. Cardamom, Mango, Soy Sauce, Vanilla)..."
                className="w-full pl-11 pr-24 py-3 rounded-2xl bg-white dark:bg-[#18201d] border border-ivory-300 dark:border-forest-800 shadow-sm focus:outline-none focus:ring-2 focus:ring-forest-500 text-sm text-stone-800 dark:text-ivory-100 placeholder-stone-400"
              />
              <button
                type="submit"
                className="absolute right-2 px-4 py-1.5 rounded-xl bg-forest-600 text-white text-xs font-semibold hover:bg-forest-500 transition-colors"
              >
                Search
              </button>
            </div>

            {/* Quick search drop results */}
            {searchResults.length > 0 && (
              <div className="absolute left-0 right-0 top-full mt-2 bg-white dark:bg-[#18201d] rounded-2xl shadow-xl border border-ivory-300 dark:border-forest-800 z-30 p-2 text-left max-h-60 overflow-y-auto">
                <p className="text-[11px] font-semibold text-stone-400 uppercase tracking-wider px-3 py-1">
                  Matching Ingredients ({searchResults.length})
                </p>
                {searchResults.map((ing) => (
                  <div
                    key={ing.id}
                    className="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-ivory-100 dark:hover:bg-forest-900 transition-colors"
                  >
                    <div>
                      <p className="font-semibold text-stone-900 dark:text-ivory-100 text-sm">{ing.name}</p>
                      <p className="text-xs text-stone-500 dark:text-stone-400">{ing.category} • {ing.cuisines.slice(0, 2).join(', ')}</p>
                    </div>
                    <button
                      type="button"
                      onClick={() => {
                        onAddIngredientToLab(ing.name, 100, ing.default_unit, 'Raw');
                        navigate('/lab');
                      }}
                      className="px-3 py-1 rounded-lg bg-sage-100 dark:bg-forest-900 hover:bg-sage-200 text-forest-700 dark:text-sage-300 text-xs font-semibold transition-colors"
                    >
                      + Add to Lab
                    </button>
                  </div>
                ))}
              </div>
            )}
          </form>
        </div>
      </section>

      {/* Showcase: Unexpected Flavor Illusions & Sensory Alchemy */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-linear-to-br from-amber-50/70 via-ivory-50 to-orange-50/60 dark:from-[#1b221e] dark:to-[#171c19] rounded-3xl p-6 sm:p-10 border-2 border-amber-300/80 dark:border-forest-800 shadow-sm space-y-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div>
              <div className="inline-flex items-center space-x-1.5 text-xs font-extrabold uppercase tracking-wider text-amber-900 dark:text-amber-300 bg-amber-100 dark:bg-amber-950/60 px-3 py-1 rounded-full border border-amber-300 dark:border-amber-800">
                <Sparkles className="w-3.5 h-3.5 text-amber-600 animate-spin" />
                <span>Sensory Alchemy • Modern Food Science</span>
              </div>
              <h2 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50 mt-2">
                Unhinged Flavor Illusions That Actually Slap
              </h2>
              <p className="text-sm text-stone-600 dark:text-stone-300 mt-1 max-w-2xl">
                When two ingredients share chemical bridges or trick your tongue's receptors, they create completely unexpected third flavors. Try them directly in your lab:
              </p>
            </div>
            <Link
              to="/lab"
              className="text-xs font-bold text-forest-700 dark:text-sage-300 hover:underline flex items-center space-x-1 self-start md:self-auto"
            >
              <span>Open Flavor Lab Workspace</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {flavorIllusions.map((item, idx) => (
              <div
                key={idx}
                className="p-5 rounded-2xl bg-white dark:bg-[#151c19] border border-ivory-200 dark:border-forest-900 shadow-xs flex flex-col justify-between hover:border-amber-400 dark:hover:border-amber-600 transition-all group"
              >
                <div className="space-y-2.5">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 dark:bg-amber-950/80 text-amber-900 dark:text-amber-200 border border-amber-200 dark:border-amber-800">
                      {item.vibe}
                    </span>
                    <Sparkles className="w-4 h-4 text-amber-500 opacity-60 group-hover:opacity-100 transition-opacity" />
                  </div>
                  <h3 className="font-bold text-stone-900 dark:text-ivory-100 text-sm">
                    {item.title}
                  </h3>
                  <div className="p-2.5 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-900/60">
                    <div className="text-[11px] font-bold text-amber-900 dark:text-amber-300">
                      ✨ Tastes Like:
                    </div>
                    <div className="text-xs font-extrabold text-amber-950 dark:text-amber-100">
                      {item.tastesLike}
                    </div>
                  </div>
                  <p className="text-[11px] text-stone-600 dark:text-stone-400 leading-relaxed">
                    {item.why}
                  </p>
                </div>

                <div className="pt-4 mt-3 border-t border-ivory-200 dark:border-forest-900">
                  <button
                    onClick={() => loadIllusionToLab(item.ingredients)}
                    className="w-full flex items-center justify-center space-x-1.5 py-2 px-3 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-xs shadow-2xs transition-all"
                  >
                    <FlaskConical className="w-3.5 h-3.5" />
                    <span>Try in Flavor Lab 🧪</span>
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Showcase: 7-Ingredient Culinary Combination */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-ivory-50 dark:bg-[#151c19] rounded-3xl p-6 sm:p-10 border border-ivory-300 dark:border-forest-900 shadow-sm">
          <div className="flex flex-col lg:flex-row items-center justify-between gap-8">
            <div className="space-y-4 max-w-xl">
              <div className="inline-flex items-center space-x-1.5 text-xs font-bold uppercase tracking-wider text-terracotta-700 dark:text-terracotta-400 bg-terracotta-50 dark:bg-terracotta-900/30 px-3 py-1 rounded-full border border-terracotta-200 dark:border-terracotta-800">
                <Flame className="w-3.5 h-3.5" />
                <span>Featured Multi-Ingredient Medley</span>
              </div>
              <h2 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50 leading-tight">
                Royal Mango Shrikhand & Spice Fusion
              </h2>
              <p className="text-sm text-stone-600 dark:text-stone-300 leading-relaxed">
                Notice how high-order interactions work: lactic acid in curd softens tropical mango fructose; cineole in cardamom bridges menthol in mint; while roasted cumin pyrazines ground the sweetness with smoky umami depth.
              </p>

              {/* Ingredient Badges */}
              <div className="flex flex-wrap gap-2 pt-2">
                {[
                  { name: 'Mango', prep: 'Raw' },
                  { name: 'Curd', prep: 'Raw' },
                  { name: 'Honey', prep: 'Raw' },
                  { name: 'Cardamom', prep: 'Raw' },
                  { name: 'Mint', prep: 'Raw' },
                  { name: 'Lime', prep: 'Raw' },
                  { name: 'Roasted Cumin', prep: 'Roasted' },
                ].map((item) => (
                  <span
                    key={item.name}
                    className="inline-flex items-center space-x-1 px-3 py-1.5 rounded-xl bg-ivory-200 dark:bg-[#1d2622] text-stone-800 dark:text-stone-200 text-xs font-semibold border border-ivory-300 dark:border-forest-800"
                  >
                    <span>{item.name}</span>
                    <span className="text-[10px] text-stone-500 dark:text-stone-400 font-normal">({item.prep})</span>
                  </span>
                ))}
              </div>

              <div className="pt-4">
                <button
                  onClick={loadExampleToLab}
                  className="flex items-center space-x-2 px-6 py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-sm font-semibold shadow-sm transition-all"
                >
                  <FlaskConical className="w-4 h-4 text-sage-200" />
                  <span>Analyze This 7-Ingredient Combo in Flavor Lab</span>
                </button>
              </div>
            </div>

            {/* Gauge Preview Card */}
            <div className="bg-white dark:bg-[#1b2420] p-6 rounded-2xl border border-ivory-300 dark:border-forest-800 shadow-sm flex flex-col sm:flex-row items-center gap-6">
              <CompatibilityGauge score={94} label="Culinary Synergy" sublabel="Evidence-backed pairing" size="md" />
              <div className="space-y-2 border-t sm:border-t-0 sm:border-l border-ivory-200 dark:border-forest-900 pt-3 sm:pt-0 sm:pl-6 text-xs text-stone-600 dark:text-stone-400">
                <div className="flex items-center justify-between space-x-6">
                  <span className="font-medium text-stone-800 dark:text-ivory-100">Sweetness Balance</span>
                  <span className="font-mono font-bold text-forest-700 dark:text-sage-300">7.8 / 10</span>
                </div>
                <div className="flex items-center justify-between space-x-6">
                  <span className="font-medium text-stone-800 dark:text-ivory-100">Acid-Base Buffer</span>
                  <span className="font-mono font-bold text-forest-700 dark:text-sage-300">6.4 / 10</span>
                </div>
                <div className="flex items-center justify-between space-x-6">
                  <span className="font-medium text-stone-800 dark:text-ivory-100">Aromatic Depth</span>
                  <span className="font-mono font-bold text-forest-700 dark:text-sage-300">8.9 / 10</span>
                </div>
                <div className="flex items-center justify-between space-x-6">
                  <span className="font-medium text-stone-800 dark:text-ivory-100">Allergen Safety</span>
                  <span className="font-semibold text-sage-600 dark:text-sage-400">Verified Dairy</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-14 space-y-3">
          <h2 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50">
            How FlavorFusion AI Works
          </h2>
          <p className="text-sm text-stone-600 dark:text-stone-300">
            A transparent culinary pipeline combining sensory science, computer vision, and personalized preference modeling.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {[
            {
              icon: Search,
              step: '01',
              title: 'Select or Photograph',
              desc: 'Add ingredients manually from our 65+ food database or capture a photo with real computer vision identification.'
            },
            {
              icon: Sliders,
              step: '02',
              title: 'Customize Prep & Ratio',
              desc: 'Adjust weights and cooking methods (Raw, Roasted, Sautéed) to account for Maillard reactions and acidity changes.'
            },
            {
              icon: Atom,
              step: '03',
              title: 'Explainable Taste Analysis',
              desc: 'Evaluate 6 basic tastes, aroma volatile overlap, culinary contrast, and hard allergy safety rules.'
            },
            {
              icon: BookOpen,
              step: '04',
              title: 'Generate Recipes & Save',
              desc: 'Turn your validated flavor harmony into step-by-step custom recipes with scaled servings and smart substitutions.'
            }
          ].map((card) => {
            const Icon = card.icon;
            return (
              <div
                key={card.step}
                className="bg-ivory-50 dark:bg-[#151c19] p-6 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-4 hover:border-forest-500 transition-all group"
              >
                <div className="flex items-center justify-between">
                  <div className="w-10 h-10 rounded-xl bg-forest-600/10 text-forest-700 dark:text-sage-300 flex items-center justify-center font-bold text-sm">
                    <Icon className="w-5 h-5 text-forest-600 dark:text-sage-400" />
                  </div>
                  <span className="font-mono text-xs font-bold text-stone-400">{card.step}</span>
                </div>
                <h3 className="font-semibold text-stone-900 dark:text-ivory-100 text-base">{card.title}</h3>
                <p className="text-xs text-stone-600 dark:text-stone-400 leading-relaxed">{card.desc}</p>
              </div>
            );
          })}
        </div>
      </section>

      {/* Featured Pairings from Discovery */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold text-stone-900 dark:text-ivory-50">
              Curated Flavor Discoveries
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400 mt-1">
              Scientifically grounded combinations curated from global gastronomy.
            </p>
          </div>
          <Link
            to="/discover"
            className="flex items-center space-x-1 text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600"
          >
            <span>Explore All Pairings</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        {loadingPairings ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[1, 2, 3].map((n) => (
              <div key={n} className="h-64 rounded-2xl bg-ivory-200 dark:bg-[#151c19] animate-pulse border border-ivory-300 dark:border-forest-900" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {featuredPairings.map((item) => (
              <div
                key={item.combination_name}
                className="bg-white dark:bg-[#151c19] rounded-2xl p-6 border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2.5 py-1 rounded-md border border-sage-200 dark:border-forest-800">
                      {item.cuisine_style} • {item.novelty}
                    </span>
                    <span className="text-xs font-bold text-forest-700 dark:text-sage-300">
                      {Math.round(item.overall_compatibility)}% Synergy
                    </span>
                  </div>
                  <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">{item.combination_name}</h3>
                  <div className="flex flex-wrap gap-1.5">
                    {item.ingredients.map((ing) => (
                      <span
                        key={ing}
                        className="px-2 py-0.5 rounded-md bg-ivory-100 dark:bg-[#1d2622] text-stone-700 dark:text-stone-300 text-xs font-medium border border-ivory-200 dark:border-forest-800"
                      >
                        {ing}
                      </span>
                    ))}
                  </div>
                  <p className="text-xs text-stone-600 dark:text-stone-300 line-clamp-3 leading-relaxed">{item.explanation}</p>
                </div>

                <div className="pt-5 border-t border-ivory-200 dark:border-forest-900 mt-4 flex items-center justify-between">
                  <button
                    onClick={() => {
                      item.ingredients.forEach((name) => onAddIngredientToLab(name, 100, 'g', 'Raw'));
                      navigate('/lab');
                    }}
                    className="text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600 flex items-center space-x-1"
                  >
                    <span>Load in Lab</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                  <Link
                    to="/recipes"
                    className="text-xs font-medium text-stone-500 dark:text-stone-400 hover:text-stone-800 dark:hover:text-stone-200"
                  >
                    View Recipe
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};
