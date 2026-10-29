import React, { useState, useEffect } from 'react';
import {
  ShieldCheck,
  Users,
  Database,
  FlaskConical,
  BookOpen,
  Star,
  Trash2,
  AlertCircle,
  RefreshCw,
  Server,
} from 'lucide-react';
import { api } from '../services/api';
import { Ingredient } from '../types';

export const AdminDashboard: React.FC = () => {
  const [stats, setStats] = useState<any>(null);
  const [feedbackList, setFeedbackList] = useState<any[]>([]);
  const [ingredients, setIngredients] = useState<Ingredient[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadAdminData();
  }, []);

  const loadAdminData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [statsData, feedbackData, ingData] = await Promise.all([
        api.admin.getStats(),
        api.admin.getFeedback(),
        api.ingredients.getAll(),
      ]);
      setStats(statsData);
      setFeedbackList(feedbackData);
      setIngredients(ingData);
    } catch (err: any) {
      setError(err.message || 'Access restricted. Please log in as an administrator.');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteIngredient = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this ingredient?')) return;
    try {
      await api.admin.deleteIngredient(id);
      setIngredients((prev) => prev.filter((i) => i.id !== id));
    } catch (err: any) {
      alert(err.message || 'Error deleting ingredient');
    }
  };

  if (error) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-20 text-center space-y-4">
        <div className="w-12 h-12 rounded-2xl bg-terracotta-100 dark:bg-terracotta-900/40 text-terracotta-700 dark:text-terracotta-300 flex items-center justify-center mx-auto">
          <AlertCircle className="w-6 h-6" />
        </div>
        <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">Admin Access Restricted</h2>
        <p className="text-sm text-stone-600 dark:text-stone-300 leading-relaxed">{error}</p>
        <p className="text-xs text-stone-500 dark:text-stone-400">
          Tip: You can log in with demo admin credentials: <code className="bg-ivory-200 dark:bg-forest-900 px-2 py-0.5 rounded text-forest-800 dark:text-sage-300 font-mono">admin@flavorfusion.ai</code> / <code className="bg-ivory-200 dark:bg-forest-900 px-2 py-0.5 rounded text-forest-800 dark:text-sage-300 font-mono">AdminPass123!</code>
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <div className="flex items-center space-x-2 text-terracotta-700 dark:text-terracotta-400 text-xs font-bold uppercase tracking-wider mb-1">
            <ShieldCheck className="w-4 h-4" />
            <span>Administrative Controls & Governance</span>
          </div>
          <h1 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50">Platform Admin Panel</h1>
        </div>
        <button
          onClick={loadAdminData}
          className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-xl bg-ivory-200 dark:bg-forest-900 hover:bg-ivory-300 dark:hover:bg-forest-800 text-stone-800 dark:text-stone-200 text-xs font-semibold cursor-pointer transition-colors"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span>Refresh Metrics</span>
        </button>
      </div>

      {/* Metrics Row */}
      {stats && (
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-1">
            <span className="text-stone-500 dark:text-stone-400 text-xs font-medium">Ingredients</span>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stats.total_ingredients}</p>
          </div>
          <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-1">
            <span className="text-stone-500 dark:text-stone-400 text-xs font-medium">Predictions</span>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stats.total_predictions}</p>
          </div>
          <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-1">
            <span className="text-stone-500 dark:text-stone-400 text-xs font-medium">Pairing Evidence</span>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stats.total_pairing_evidence}</p>
          </div>
          <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-1">
            <span className="text-stone-500 dark:text-stone-400 text-xs font-medium">Formulated Recipes</span>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stats.total_recipes}</p>
          </div>
          <div className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-1">
            <span className="text-stone-500 dark:text-stone-400 text-xs font-medium">User Ratings</span>
            <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stats.total_ratings}</p>
          </div>
        </div>
      )}

      {/* Two columns: Ingredient Catalog & User Feedback */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Ingredient Catalog Manager (7 cols) */}
        <div className="lg:col-span-7 bg-white dark:bg-[#151c19] rounded-3xl p-6 border border-ivory-300 dark:border-forest-900 shadow-xs space-y-4">
          <div className="flex items-center justify-between border-b border-ivory-200 dark:border-forest-900 pb-3">
            <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">
              Ingredient Catalog ({ingredients.length})
            </h3>
            <span className="text-xs text-stone-500 dark:text-stone-400">Live Database Records</span>
          </div>

          <div className="max-h-96 overflow-y-auto divide-y divide-ivory-100 dark:divide-forest-900/60 text-xs">
            {ingredients.map((ing) => (
              <div key={ing.id} className="py-2.5 flex items-center justify-between hover:bg-ivory-50 dark:hover:bg-forest-900/50 px-2 rounded-lg transition-colors">
                <div>
                  <span className="font-semibold text-stone-900 dark:text-ivory-100">{ing.name}</span>
                  <span className="text-stone-400 dark:text-stone-400 ml-2">({ing.category} • {ing.cuisines.join(', ') || 'Global'})</span>
                  {ing.allergens.length > 0 && (
                    <span className="text-[10px] text-terracotta-700 dark:text-terracotta-400 ml-2">Allergens: {ing.allergens.join(', ')}</span>
                  )}
                </div>
                {!ing.is_curated && (
                  <button
                    onClick={() => handleDeleteIngredient(ing.id)}
                    className="p-1 rounded text-stone-400 hover:text-terracotta-600 transition-colors cursor-pointer"
                    title="Delete custom ingredient"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* User Submitted Feedback & Ratings (5 cols) */}
        <div className="lg:col-span-5 bg-white dark:bg-[#151c19] rounded-3xl p-6 border border-ivory-300 dark:border-forest-900 shadow-xs space-y-4">
          <div className="flex items-center justify-between border-b border-ivory-200 dark:border-forest-900 pb-3">
            <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">
              User Ratings & Feedback ({feedbackList.length})
            </h3>
          </div>

          <div className="max-h-96 overflow-y-auto divide-y divide-ivory-100 dark:divide-forest-900/60 text-xs">
            {feedbackList.length === 0 ? (
              <p className="text-stone-400 text-center py-8">No feedback records submitted yet.</p>
            ) : (
              feedbackList.map((f) => (
                <div key={f.id} className="py-3 space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-stone-800 dark:text-stone-200">Score: {f.score} / 5</span>
                    <span className="text-stone-400 text-[10px]">
                      {f.created_at ? new Date(f.created_at).toLocaleDateString() : ''}
                    </span>
                  </div>
                  {f.comment && <p className="text-stone-600 dark:text-stone-300 text-[11px] italic">"{f.comment}"</p>}
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
