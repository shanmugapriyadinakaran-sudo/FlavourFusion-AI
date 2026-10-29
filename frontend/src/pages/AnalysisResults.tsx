import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  ArrowLeft,
  CheckCircle,
  FlaskConical,
  BookOpen,
  Bookmark,
  Share2,
  AlertTriangle,
  RefreshCw,
  Sparkles,
  UtensilsCrossed,
  ChefHat,
  Zap,
  Dna,
} from 'lucide-react';
import { api } from '../services/api';
import { CombinationAnalysis } from '../types';
import { RadarTasteChart } from '../components/RadarTasteChart';
import { CompatibilityGauge } from '../components/CompatibilityGauge';

interface AnalysisResultsProps {
  onAddIngredientToLab: (name: string, quantity?: number, unit?: string, prep?: string) => void;
}

export const AnalysisResults: React.FC<AnalysisResultsProps> = ({ onAddIngredientToLab }) => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [analysis, setAnalysis] = useState<CombinationAnalysis | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (id) {
      loadAnalysis(parseInt(id, 10));
    }
  }, [id]);

  const loadAnalysis = async (predictionId: number) => {
    setLoading(true);
    setError(null);
    try {
      const data = await api.combinations.getById(predictionId);
      setAnalysis(data);
    } catch (err: any) {
      setError(err.message || 'Error loading combination analysis record.');
    } finally {
      setLoading(false);
    }
  };

  const handleOpenInLab = () => {
    if (!analysis) return;
    analysis.suggested_ratios.forEach((r) => {
      onAddIngredientToLab(r.ingredient, r.recommended_grams || 100, 'g', 'Raw');
    });
    navigate('/lab');
  };

  const handleGenerateRecipe = (dishName?: string) => {
    if (!analysis) return;
    navigate('/recipes', {
      state: {
        prediction_id: analysis.id,
        title: dishName || analysis.title,
        ingredients: analysis.suggested_ratios.map((r) => ({
          name: r.ingredient,
          quantity: r.recommended_grams || 100,
          unit: 'g',
          preparation_method: 'Raw',
        })),
      },
    });
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center space-y-4">
        <RefreshCw className="w-8 h-8 animate-spin text-forest-600 dark:text-sage-400 mx-auto" />
        <p className="text-sm text-stone-600 dark:text-stone-300">Retrieving flavor profile records...</p>
      </div>
    );
  }

  if (error || !analysis) {
    return (
      <div className="max-w-md mx-auto px-4 py-20 text-center space-y-4">
        <AlertTriangle className="w-10 h-10 text-terracotta-500 mx-auto" />
        <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-50">Analysis Not Found</h3>
        <p className="text-xs text-stone-600 dark:text-stone-400">{error || 'Unable to locate this combination.'}</p>
        <button
          onClick={() => navigate('/lab')}
          className="px-4 py-2 rounded-xl bg-forest-600 text-white text-xs font-semibold hover:bg-forest-500 cursor-pointer"
        >
          Go to Flavor Lab
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Top Bar */}
      <div className="flex items-center justify-between border-b border-ivory-300 dark:border-forest-900 pb-4">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center space-x-1.5 text-xs font-semibold text-stone-600 dark:text-stone-300 hover:text-stone-900 dark:hover:text-ivory-100 cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back</span>
        </button>
        <div className="flex items-center space-x-2">
          <button
            onClick={handleOpenInLab}
            className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-xs font-semibold shadow-xs cursor-pointer transition-all"
          >
            <FlaskConical className="w-3.5 h-3.5" />
            <span>Open in Lab</span>
          </button>
          <button
            onClick={() => handleGenerateRecipe()}
            className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl bg-terracotta-600 hover:bg-terracotta-500 text-white text-xs font-semibold shadow-xs cursor-pointer transition-all"
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>Recipe</span>
          </button>
        </div>
      </div>

      {/* Main Analysis Card */}
      <div className="bg-white dark:bg-[#151c19] rounded-3xl p-6 sm:p-10 border border-ivory-300 dark:border-forest-900 shadow-sm space-y-8">
        <div>
          <div className="flex flex-wrap items-center gap-2 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2.5 py-1 rounded-md border border-sage-200 dark:border-forest-800">
              {analysis.evidence_quality}
            </span>
            {analysis.vibe_check && (
              <span className="text-xs font-bold uppercase tracking-wider text-amber-800 dark:text-amber-300 bg-amber-50 dark:bg-amber-950/60 px-2.5 py-1 rounded-md border border-amber-200 dark:border-amber-800">
                {analysis.vibe_check}
              </span>
            )}
          </div>
          <h1 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50 mt-1">
            {analysis.title}
          </h1>
        </div>

        {/* Tastes Like Sensory Illusion Highlight */}
        {analysis.tastes_like && (
          <div className="bg-linear-to-r from-amber-50 via-orange-50/50 to-amber-50/30 dark:from-[#1e241f] dark:to-[#171f1b] p-5 rounded-2xl border-2 border-amber-300/80 dark:border-amber-800/80 space-y-2 shadow-xs">
            <div className="flex items-center space-x-2 text-amber-900 dark:text-amber-300">
              <Zap className="w-5 h-5 text-amber-600 dark:text-amber-400 fill-amber-500" />
              <span className="text-xs font-extrabold uppercase tracking-wider">
                Sensory Synergy Perception:
              </span>
            </div>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-amber-100">
              "{analysis.tastes_like}"
            </p>
            {analysis.tastes_like_explanation && (
              <p className="text-xs text-stone-600 dark:text-stone-300 leading-relaxed pt-1">
                {analysis.tastes_like_explanation}
              </p>
            )}
          </div>
        )}

        {/* Molecular Volatiles & Receptor Synthesis Card */}
        {((analysis.shared_molecules && analysis.shared_molecules.length > 0) || analysis.molecular_taste_synthesis) && (
          <div className="bg-sage-50/80 dark:bg-[#141d19] p-5 rounded-2xl border border-sage-200 dark:border-forest-800 space-y-3 shadow-xs">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center space-x-2 text-forest-800 dark:text-sage-300">
                <Dna className="w-4 h-4 text-forest-600 dark:text-sage-400" />
                <span className="text-xs font-bold uppercase tracking-wider">
                  Molecular Volatiles & Receptor Synthesis
                </span>
              </div>
              {analysis.shared_molecule_count !== undefined && analysis.shared_molecule_count > 0 && (
                <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-forest-100 dark:bg-forest-900/80 text-forest-800 dark:text-sage-300 border border-forest-300 dark:border-forest-700">
                  🧬 {analysis.shared_molecule_count} Shared Aroma Molecule{analysis.shared_molecule_count > 1 ? 's' : ''}
                </span>
              )}
            </div>

            {analysis.shared_molecules && analysis.shared_molecules.length > 0 && (
              <div className="flex flex-wrap gap-1.5 pt-1">
                {analysis.shared_molecules.map((mol, idx) => (
                  <span
                    key={idx}
                    className="px-2.5 py-1 rounded-xl bg-white dark:bg-[#1c2420] border border-sage-300 dark:border-forest-700 text-stone-800 dark:text-ivory-100 text-xs font-medium flex items-center space-x-1.5 shadow-xs"
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-sage-500"></span>
                    <span>{mol}</span>
                  </span>
                ))}
              </div>
            )}

            {analysis.molecular_taste_synthesis && (
              <p className="text-xs text-stone-600 dark:text-stone-300 leading-relaxed">
                {analysis.molecular_taste_synthesis}
              </p>
            )}
          </div>
        )}

        {/* Dual Gauges */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-ivory-50 dark:bg-[#1b2320] p-6 rounded-2xl border border-ivory-200 dark:border-forest-800">
          <CompatibilityGauge
            score={analysis.overall_compatibility}
            label="General Compatibility"
            sublabel="Food science & aromatic synergy"
            size="md"
          />
          <CompatibilityGauge
            score={analysis.personalized_match || analysis.overall_compatibility}
            label="Personalized Match"
            sublabel="Aligned with your taste preferences"
            size="md"
          />
        </div>

        {/* Palate Profile Chart */}
        <div className="space-y-3">
          <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-50">Palate Profile</h3>
          <div className="bg-ivory-50 dark:bg-[#1b2320] p-4 rounded-2xl border border-ivory-200 dark:border-forest-800">
            <RadarTasteChart tasteProfile={analysis.taste_profile} />
          </div>
        </div>

        {/* Possible Dishes you can make with these ingredients */}
        {analysis.possible_dishes && analysis.possible_dishes.length > 0 && (
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <UtensilsCrossed className="w-5 h-5 text-forest-600 dark:text-sage-400" />
                <h3 className="font-serif text-xl font-bold text-stone-900 dark:text-ivory-50">
                  Dishes You Can Make
                </h3>
              </div>
              <span className="text-xs text-stone-500 dark:text-stone-400">
                {analysis.possible_dishes.length} gourmet suggestions
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {analysis.possible_dishes.map((dish) => (
                <div
                  key={dish.name}
                  className="bg-ivory-50 dark:bg-[#1b2320] p-4 rounded-2xl border border-ivory-200 dark:border-forest-800 flex flex-col justify-between hover:border-forest-500 transition-all space-y-3"
                >
                  <div>
                    <div className="flex items-center justify-between">
                      <h4 className="font-serif font-bold text-stone-900 dark:text-ivory-100 text-sm">
                        {dish.name}
                      </h4>
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-forest-100 dark:bg-forest-900 text-forest-800 dark:text-sage-300">
                        {dish.vibe_tag || dish.difficulty || 'Fusion'}
                      </span>
                    </div>
                    <p className="text-xs text-stone-600 dark:text-stone-300 mt-1 leading-relaxed">
                      {dish.description}
                    </p>
                  </div>
                  <div className="pt-2 border-t border-ivory-200 dark:border-forest-800 flex items-center justify-between">
                    <span className="text-[11px] text-stone-500 dark:text-stone-400">
                      ⏱ ~{dish.cook_time_mins || dish.estimated_time_mins || 15} mins
                    </span>
                    <button
                      onClick={() => handleGenerateRecipe(dish.name)}
                      className="text-xs font-semibold text-terracotta-600 dark:text-terracotta-400 hover:text-terracotta-500 flex items-center space-x-1 cursor-pointer"
                    >
                      <span>Create Recipe</span>
                      <BookOpen className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Suggested Ratios */}
        {analysis.suggested_ratios.length > 0 && (
          <div className="space-y-3">
            <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">
              Ingredients & Recommended Ratios
            </h3>
            <div className="divide-y divide-ivory-200 dark:divide-forest-800 bg-ivory-50 dark:bg-[#1b2320] rounded-2xl border border-ivory-200 dark:border-forest-800 overflow-hidden text-xs">
              {analysis.suggested_ratios.map((item) => (
                <div key={item.ingredient} className="flex items-center justify-between px-4 py-2.5">
                  <span className="font-semibold text-stone-800 dark:text-stone-200">{item.ingredient}</span>
                  <span className="text-forest-700 dark:text-sage-400 font-mono font-bold">{item.ratio}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
