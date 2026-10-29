import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  User,
  Bookmark,
  BookOpen,
  FlaskConical,
  Star,
  Trash2,
  ArrowRight,
  Clock,
  Sparkles,
  Settings,
  ShieldCheck,
  Calendar,
  Heart
} from 'lucide-react';
import { api } from '../services/api';
import { Recipe } from '../types';

export const UserDashboard: React.FC = () => {
  const navigate = useNavigate();
  const [dashboardData, setDashboardData] = useState<any>(null);
  const [savedCombos, setSavedCombos] = useState<any[]>([]);
  const [savedRecipes, setSavedRecipes] = useState<Recipe[]>([]);
  const [wishlistRecipes, setWishlistRecipes] = useState<Recipe[]>([]);
  const [ratings, setRatings] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const [dash, combos, recipes, wishlist, userRatings] = await Promise.all([
        api.users.getDashboard(),
        api.combinations.getSaved(),
        api.recipes.getSaved(),
        api.recipes.getWishlist(),
        api.ratings.getAll(),
      ]);
      setDashboardData(dash);
      setSavedCombos(combos);
      setSavedRecipes(recipes);
      setWishlistRecipes(wishlist);
      setRatings(userRatings);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteCombo = async (id: number) => {
    try {
      await api.combinations.deleteSaved(id);
      setSavedCombos((prev) => prev.filter((c) => c.id !== id));
    } catch {
      alert('Failed to remove saved combination');
    }
  };

  const handleToggleWishlist = async (id: number) => {
    try {
      await api.recipes.toggleWishlist(id);
      setWishlistRecipes((prev) => prev.filter((r) => r.id !== id));
    } catch {
      alert('Failed to update wishlist');
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-ivory-300 dark:border-forest-900 pb-6">
        <div>
          <h1 className="font-serif text-3xl sm:text-4xl font-bold text-stone-900 dark:text-ivory-50">
            Culinary Dashboard
          </h1>
          <p className="text-sm text-stone-600 dark:text-stone-300 mt-1">
            Review your saved formulas, wishlisted dishes, crafted recipes, and rating history.
          </p>
        </div>

        <Link
          to="/profile"
          className="flex items-center space-x-2 px-4 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900/60 hover:bg-ivory-300 dark:hover:bg-forest-800 text-stone-800 dark:text-ivory-100 text-xs font-semibold self-start sm:self-auto transition-colors"
        >
          <Settings className="w-4 h-4" />
          <span>Edit Taste Preferences</span>
        </Link>
      </div>

      {/* Metric Counters */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {[
          { label: 'Wishlist Dishes', val: wishlistRecipes.length, icon: Heart, color: 'text-terracotta-700 bg-terracotta-100 dark:bg-terracotta-950/40 dark:text-terracotta-300' },
          { label: 'Saved Formulas', val: savedCombos.length, icon: Bookmark, color: 'text-forest-700 bg-sage-100 dark:bg-forest-900/40 dark:text-sage-300' },
          { label: 'Saved Recipes', val: savedRecipes.length, icon: BookOpen, color: 'text-terracotta-700 bg-terracotta-100 dark:bg-terracotta-950/40 dark:text-terracotta-300' },
          { label: 'Taste Ratings', val: ratings.length, icon: Star, color: 'text-amber-700 bg-amber-100 dark:bg-amber-950/40 dark:text-amber-300' },
        ].map((stat) => {
          const Icon = stat.icon;
          return (
            <div key={stat.label} className="bg-ivory-50 dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-2">
              <div className={`w-8 h-8 rounded-lg flex items-center justify-center ${stat.color}`}>
                <Icon className="w-4 h-4" />
              </div>
              <p className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">{stat.val}</p>
              <p className="text-xs text-stone-500 dark:text-stone-400 font-medium">{stat.label}</p>
            </div>
          );
        })}
      </div>

      {/* Wishlist Dishes Section */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Heart className="w-5 h-5 text-terracotta-600 fill-current" />
            <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">
              Wishlist & Liked Dishes
            </h2>
          </div>
          <span className="text-xs text-stone-500 dark:text-stone-400 font-medium">
            {wishlistRecipes.length} dishes bookmarked
          </span>
        </div>

        {wishlistRecipes.length === 0 ? (
          <div className="p-8 text-center bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 text-xs text-stone-500 dark:text-stone-400">
            You haven't added any dishes to your wishlist yet. In the Flavor Lab, click "Wishlist" on any recommended dish!
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {wishlistRecipes.map((r) => (
              <div
                key={r.id}
                className="bg-white dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow"
              >
                <div className="space-y-2">
                  <div className="flex items-center justify-between text-[11px] font-semibold text-stone-500 dark:text-stone-400">
                    <span className="px-2 py-0.5 rounded bg-terracotta-50 dark:bg-terracotta-950/40 text-terracotta-700 dark:text-terracotta-300 border border-terracotta-200 dark:border-terracotta-800">
                      Wishlist Item
                    </span>
                    <button
                      onClick={() => r.id && handleToggleWishlist(r.id)}
                      className="text-stone-400 hover:text-terracotta-600 p-1"
                      title="Remove from Wishlist"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">{r.title}</h3>
                  <p className="text-xs text-stone-600 dark:text-stone-400 line-clamp-2">{r.summary}</p>
                </div>

                <div className="pt-4 mt-3 border-t border-ivory-200 dark:border-forest-900 flex items-center justify-between">
                  <span className="text-[11px] text-stone-400">Prep: {r.prep_time_mins}m</span>
                  <button
                    onClick={() => navigate('/recipes', { state: { recipe: r } })}
                    className="text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600 flex items-center space-x-1"
                  >
                    <span>Cook Dish</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Saved Combinations Section */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">Saved Combinations</h2>
          <Link to="/lab" className="text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600">
            Open Flavor Lab →
          </Link>
        </div>

        {savedCombos.length === 0 ? (
          <div className="p-8 text-center bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 text-xs text-stone-500 dark:text-stone-400">
            You haven't saved any flavor combinations yet. Analyze a pairing in the Flavor Lab and click "Save"!
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {savedCombos.map((combo) => (
              <div
                key={combo.id}
                className="bg-white dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow"
              >
                <div className="space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-forest-700 dark:text-sage-300 bg-sage-50 dark:bg-forest-900/60 px-2 py-0.5 rounded">
                      Saved Formula
                    </span>
                    <button
                      onClick={() => handleDeleteCombo(combo.id)}
                      className="text-stone-400 hover:text-terracotta-600 p-1"
                      title="Remove"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <h3 className="font-serif text-base font-bold text-stone-900 dark:text-ivory-50">
                    {combo.custom_title || 'Flavor Medley'}
                  </h3>
                  {combo.notes && (
                    <p className="text-xs text-stone-600 dark:text-stone-300 line-clamp-2 italic bg-ivory-50 dark:bg-[#1d2622] p-2 rounded-lg">
                      "{combo.notes}"
                    </p>
                  )}
                </div>

                <div className="pt-4 mt-3 border-t border-ivory-200 dark:border-forest-900">
                  <Link
                    to={`/analysis/${combo.prediction_id}`}
                    className="text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600 flex items-center space-x-1"
                  >
                    <span>View Chemical Breakdown</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Saved Recipes Section */}
      <section className="space-y-4">
        <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">Saved Culinary Recipes</h2>
        {savedRecipes.length === 0 ? (
          <div className="p-8 text-center bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 text-xs text-stone-500 dark:text-stone-400">
            No recipes saved yet. Generate recipes from your favorite combinations and bookmark them!
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {savedRecipes.map((r) => (
              <div
                key={r.id}
                className="bg-white dark:bg-[#151c19] p-5 rounded-2xl border border-ivory-300 dark:border-forest-900 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow"
              >
                <div className="space-y-2">
                  <div className="flex items-center justify-between text-[11px] text-stone-500 dark:text-stone-400 font-semibold">
                    <span>{r.cuisine}</span>
                    <span>{r.servings} Servings</span>
                  </div>
                  <h3 className="font-serif text-lg font-bold text-stone-900 dark:text-ivory-50">{r.title}</h3>
                  <p className="text-xs text-stone-600 dark:text-stone-400 line-clamp-2">{r.summary}</p>
                </div>

                <div className="pt-4 mt-3 border-t border-ivory-200 dark:border-forest-900 flex items-center justify-between">
                  <span className="text-[11px] text-stone-400">Prep: {r.prep_time_mins}m</span>
                  <button
                    onClick={() => navigate('/recipes', { state: { recipe: r } })}
                    className="text-xs font-semibold text-forest-700 dark:text-sage-300 hover:text-forest-600"
                  >
                    Open Recipe →
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Rating & Feedback History */}
      <section className="space-y-4">
        <h2 className="font-serif text-2xl font-bold text-stone-900 dark:text-ivory-50">Feedback & Rating History</h2>
        {ratings.length === 0 ? (
          <div className="p-8 text-center bg-ivory-50 dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 text-xs text-stone-500 dark:text-stone-400">
            No ratings recorded yet. Rate combinations to teach FlavorFusion AI what works best for your palate.
          </div>
        ) : (
          <div className="bg-white dark:bg-[#151c19] rounded-2xl border border-ivory-300 dark:border-forest-900 overflow-hidden divide-y divide-ivory-200 dark:divide-forest-900">
            {ratings.map((rating) => (
              <div key={rating.id} className="p-4 flex items-center justify-between text-xs">
                <div className="space-y-1">
                  <div className="flex items-center space-x-1.5">
                    {[1, 2, 3, 4, 5].map((s) => (
                      <Star
                        key={s}
                        className={`w-3.5 h-3.5 ${
                          rating.score >= s ? 'text-amber-500 fill-amber-500' : 'text-stone-300 dark:text-stone-600'
                        }`}
                      />
                    ))}
                    <span className="font-bold text-stone-800 dark:text-ivory-100 ml-2">{rating.score} / 5 Stars</span>
                  </div>
                  {rating.comment && <p className="text-stone-600 dark:text-stone-400">{rating.comment}</p>}
                </div>
                <span className="text-[11px] text-stone-400">
                  {rating.created_at ? new Date(rating.created_at).toLocaleDateString() : ''}
                </span>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};
