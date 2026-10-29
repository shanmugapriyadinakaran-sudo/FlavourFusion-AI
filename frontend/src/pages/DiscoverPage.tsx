import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Sparkles,
  Compass,
  FlaskConical,
  BookOpen,
  ArrowRight,
  Filter,
  CheckCircle,
  AlertTriangle,
  Flame,
  ThumbsUp,
  ThumbsDown,
  Info
} from 'lucide-react';
import { api } from '../services/api';
import { RecommendationItem } from '../types';

interface DiscoverPageProps {
  onAddIngredientToLab: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const DiscoverPage: React.FC<DiscoverPageProps> = ({ onAddIngredientToLab }) => {
  const navigate = useNavigate();
  const [recommendations, setRecommendations] = useState<RecommendationItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filters
  const [selectedCuisine, setSelectedCuisine] = useState('All');
  const [selectedNovelty, setSelectedNovelty] = useState('All');
  const [feedbackSent, setFeedbackSent] = useState<Record<string, boolean>>({});

  const cuisines = ['All', 'Indian', 'Mediterranean', 'Italian', 'Mexican', 'South Indian', 'Fusion'];
  const novelties = ['All', 'Classic', 'Balanced', 'Adventurous'];

  useEffect(() => {
    loadRecommendations();
  }, [selectedCuisine, selectedNovelty]);

  const loadRecommendations = async () => {
    setLoading(true);
    try {
      const data = await api.recommendations.getPersonalized({
        cuisine: selectedCuisine !== 'All' ? selectedCuisine : undefined,
        novelty: selectedNovelty !== 'All' ? selectedNovelty : undefined,
        limit: 12,
      });
      setRecommendations(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleFeedback = async (item: RecommendationItem, liked: boolean) => {
    try {
      await api.recommendations.submitFeedback({
        combination_name: item.combination_name,
        ingredients: item.ingredients,
        score: liked ? 5 : 2,
        liked,
      });
      setFeedbackSent((prev) => ({ ...prev, [item.combination_name]: true }));
    } catch {
      // ignore
    }
  };

  const handleLoadInLab = (item: RecommendationItem) => {
    item.ingredients.forEach((name) => {
      onAddIngredientToLab(name, 100, 'g', 'Raw');
    });
    navigate('/lab');
  };

  const handleGenerateRecipe = (item: RecommendationItem) => {
    navigate('/recipes', {
      state: {
        ingredients: item.ingredients.map((name) => ({
          name,
          quantity: 100,
          unit: 'g',
          preparation_method: 'Raw',
        })),
        title: item.combination_name,
      },
    });
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <div className="flex items-center space-x-1.5 text-forest-700 dark:text-sage-300 text-xs font-semibold uppercase tracking-wider mb-1">
            <Sparkles className="w-4 h-4 text-forest-600 dark:text-sage-400" />
            <span>Personalized Food Discovery</span>
          </div>
          <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
            Flavor Pairings & Synergy
          </h1>
          <p className="text-sm text-stone-600 dark:text-stone-300 mt-1">
            Discover classic pairings and daring avant-garde combinations tailored to your palate and safety preferences.
          </p>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-4">
        {/* Novelty Selector */}
        <div className="flex items-center space-x-2 overflow-x-auto pb-1">
          <span className="text-xs font-semibold text-stone-500 dark:text-stone-400 uppercase tracking-wider mr-2">
            Novelty Style:
          </span>
          {novelties.map((nov) => (
            <button
              key={nov}
              onClick={() => setSelectedNovelty(nov)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                selectedNovelty === nov
                  ? 'bg-forest-600 text-white shadow-sm'
                  : 'bg-ivory-200 dark:bg-forest-900/60 text-stone-700 dark:text-stone-300 hover:bg-ivory-300 dark:hover:bg-forest-800'
              }`}
            >
              {nov === 'All' ? 'All Novelties' : nov}
            </button>
          ))}
        </div>

        {/* Cuisine Selector */}
        <div className="flex items-center space-x-2 overflow-x-auto pt-2 border-t border-ivory-200 dark:border-forest-900">
          <span className="text-xs font-semibold text-stone-500 dark:text-stone-400 uppercase tracking-wider mr-2">
            Cuisine:
          </span>
          {cuisines.map((c) => (
            <button
              key={c}
              onClick={() => setSelectedCuisine(c)}
              className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${
                selectedCuisine === c
                  ? 'bg-sage-600 text-white font-semibold'
                  : 'bg-white dark:bg-[#1b2420] text-stone-600 dark:text-stone-300 border border-ivory-300 dark:border-forest-800 hover:bg-ivory-100 dark:hover:bg-forest-900'
              }`}
            >
              {c}
            </button>
          ))}
        </div>
      </div>

      {/* Recommendations Cards Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="h-72 rounded-2xl bg-ivory-200 dark:bg-[#151c19] animate-pulse border border-ivory-300 dark:border-forest-900" />
          ))}
        </div>
      ) : recommendations.length === 0 ? (
        <div className="text-center py-16 bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-3">
          <Info className="w-10 h-10 text-stone-400 mx-auto" />
          <h3 className="font-serif text-lg font-bold text-stone-800 dark:text-ivory-100">No pairings matched your current filters</h3>
          <p className="text-xs text-stone-500 dark:text-stone-400 max-w-sm mx-auto">
            Try switching novelty styles or cuisine filters, or ensure your allergy preferences are not overly restrictive.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recommendations.map((item) => {
            const hasFeedback = feedbackSent[item.combination_name];
            return (
              <div
                key={item.combination_name}
                className="bg-white dark:bg-[#151c19] rounded-3xl p-6 border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:shadow-md hover:border-forest-400 dark:hover:border-forest-600 transition-all group"
              >
                <div className="space-y-4">
                  {/* Top Badges */}
                  <div className="flex items-center justify-between">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2.5 py-1 rounded-md border border-sage-200 dark:border-forest-800">
                      {item.cuisine_style} • {item.novelty}
                    </span>
                    <div className="text-right">
                      <span className="text-xs font-bold text-forest-700 dark:text-sage-300 block">
                        {Math.round(item.personalized_match)}% Match
                      </span>
                      <span className="text-[10px] text-stone-400">
                        {Math.round(item.overall_compatibility)}% general
                      </span>
                    </div>
                  </div>

                  <div>
                    <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-50 group-hover:text-forest-700 dark:group-hover:text-sage-300 transition-colors">
                      {item.combination_name}
                    </h3>
                    <p className="text-xs text-stone-500 dark:text-stone-400 mt-0.5">
                      {item.evidence_quality}
                    </p>
                  </div>

                  {/* Ingredient pills */}
                  <div className="flex flex-wrap gap-1.5">
                    {item.ingredients.map((ing) => (
                      <span
                        key={ing}
                        className="px-2.5 py-1 rounded-xl bg-ivory-100 dark:bg-[#1d2622] text-stone-800 dark:text-stone-200 text-xs font-medium border border-ivory-200 dark:border-forest-800"
                      >
                        {ing}
                      </span>
                    ))}
                  </div>

                  {/* Explanation */}
                  <p className="text-xs text-stone-600 dark:text-stone-300 leading-relaxed">
                    {item.explanation}
                  </p>

                  {/* Preparation suggestion */}
                  <div className="p-3 bg-ivory-50 dark:bg-[#1d2622] rounded-xl border border-ivory-200 dark:border-forest-800 text-[11px] text-stone-600 dark:text-stone-300 space-y-1">
                    <span className="font-semibold text-stone-800 dark:text-ivory-100 block">Chef's Technique:</span>
                    <p className="italic">{item.suggested_preparation}</p>
                  </div>
                </div>

                {/* Footer Actions */}
                <div className="pt-4 border-t border-ivory-200 dark:border-forest-900 mt-5 space-y-3">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-1">
                      <span className="text-[11px] text-stone-400 mr-1">Feedback:</span>
                      {hasFeedback ? (
                        <span className="text-xs font-semibold text-sage-600 dark:text-sage-400 flex items-center space-x-1">
                          <CheckCircle className="w-3.5 h-3.5" />
                          <span>Recorded</span>
                        </span>
                      ) : (
                        <>
                          <button
                            onClick={() => handleFeedback(item, true)}
                            className="p-1 rounded text-stone-400 hover:text-forest-600 dark:hover:text-sage-400 hover:bg-forest-50 dark:hover:bg-forest-900"
                            title="Love this pairing"
                          >
                            <ThumbsUp className="w-3.5 h-3.5" />
                          </button>
                          <button
                            onClick={() => handleFeedback(item, false)}
                            className="p-1 rounded text-stone-400 hover:text-terracotta-600 dark:hover:text-terracotta-400 hover:bg-terracotta-50 dark:hover:bg-terracotta-900/30"
                            title="Dislike this pairing"
                          >
                            <ThumbsDown className="w-3.5 h-3.5" />
                          </button>
                        </>
                      )}
                    </div>

                    <button
                      onClick={() => handleGenerateRecipe(item)}
                      className="text-xs font-semibold text-stone-700 dark:text-stone-300 hover:text-stone-900 dark:hover:text-ivory-100 flex items-center space-x-1"
                    >
                      <BookOpen className="w-3.5 h-3.5 text-forest-600 dark:text-sage-400" />
                      <span>Recipe</span>
                    </button>
                  </div>

                  <button
                    onClick={() => handleLoadInLab(item)}
                    className="w-full py-2.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-xs font-semibold shadow-sm transition-all flex items-center justify-center space-x-1.5"
                  >
                    <FlaskConical className="w-3.5 h-3.5 text-sage-200" />
                    <span>Open in Flavor Lab</span>
                    <ArrowRight className="w-3 h-3" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
