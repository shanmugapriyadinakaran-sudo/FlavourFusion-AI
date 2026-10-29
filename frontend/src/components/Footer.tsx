import React from 'react';
import { Link } from 'react-router-dom';
import { ChefHat, ShieldAlert, Heart, ExternalLink } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-ivory-200 dark:bg-[#0c110f] border-t border-ivory-300 dark:border-forest-900 mt-20 pt-16 pb-12 text-stone-600 dark:text-stone-300 text-sm transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-ivory-300 dark:border-forest-900">
          {/* Brand info */}
          <div className="md:col-span-1 space-y-4">
            <div className="flex items-center space-x-2.5">
              <div className="w-9 h-9 rounded-xl bg-forest-600 dark:bg-forest-500 text-ivory-50 flex items-center justify-center shadow-sm">
                <ChefHat className="w-5 h-5 text-sage-200" />
              </div>
              <span className="font-serif text-xl font-bold tracking-tight text-forest-800 dark:text-ivory-50">
                FlavorFusion AI
              </span>
            </div>
            <p className="text-stone-500 dark:text-stone-400 leading-relaxed text-xs">
              Scientific food pairing engine computing multi-ingredient synergy, aroma compound overlap, and personalized palate matching for curious cooks and professional chefs.
            </p>
          </div>

          {/* Core Tools */}
          <div>
            <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-xs uppercase tracking-wider mb-4">
              Culinary Tools
            </h4>
            <ul className="space-y-2.5 text-xs text-stone-600 dark:text-stone-300">
              <li>
                <Link to="/lab" className="hover:text-forest-700 dark:hover:text-sage-300 transition-colors">
                  Flavor Lab (Multi-Ingredient Workspace)
                </Link>
              </li>
              <li>
                <Link to="/ingredients" className="hover:text-forest-700 dark:hover:text-sage-300 transition-colors">
                  Ingredient Taste Database
                </Link>
              </li>
              <li>
                <Link to="/vision" className="hover:text-forest-700 dark:hover:text-sage-300 transition-colors">
                  Computer Vision Food Identifier
                </Link>
              </li>
              <li>
                <Link to="/recipes" className="hover:text-forest-700 dark:hover:text-sage-300 transition-colors">
                  Formulated Recipe Generator
                </Link>
              </li>
              <li>
                <Link to="/discover" className="hover:text-forest-700 dark:hover:text-sage-300 transition-colors">
                  Curated Culinary Pairings
                </Link>
              </li>
            </ul>
          </div>

          {/* Knowledge & Science */}
          <div>
            <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-xs uppercase tracking-wider mb-4">
              Flavor Science
            </h4>
            <ul className="space-y-2.5 text-xs text-stone-600 dark:text-stone-300">
              <li className="flex items-center space-x-1.5 text-stone-500 dark:text-stone-400">
                <span>GC-MS Aroma Chemistry</span>
              </li>
              <li className="flex items-center space-x-1.5 text-stone-500 dark:text-stone-400">
                <span>Lactic Acid & Acid-Base Buffering</span>
              </li>
              <li className="flex items-center space-x-1.5 text-stone-500 dark:text-stone-400">
                <span>Pyrazine & Terpene Affinity</span>
              </li>
              <li className="flex items-center space-x-1.5 text-stone-500 dark:text-stone-400">
                <span>Hard Allergy Constraint Engine</span>
              </li>
            </ul>
          </div>

          {/* Food Safety & Scientific Disclaimer */}
          <div className="bg-ivory-50 dark:bg-[#141b18] p-4 rounded-2xl border border-ivory-300 dark:border-forest-800 shadow-2xs">
            <div className="flex items-center space-x-2 text-terracotta-700 dark:text-terracotta-400 font-semibold text-xs mb-2">
              <ShieldAlert className="w-4 h-4 shrink-0" />
              <span>Culinary & Safety Disclaimer</span>
            </div>
            <p className="text-[11px] text-stone-500 dark:text-stone-400 leading-normal">
              Flavor compatibility estimates are algorithmic hypotheses based on culinary evidence and volatile compound matching. They do not infer microbial safety, ingredient freshness, or replace official medical allergen verification. Always inspect food for safety before cooking or consuming.
            </p>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-stone-500 dark:text-stone-400 gap-4">
          <p>© 2026 FlavorFusion AI Platform. Built with React, Vite, TypeScript & FastAPI.</p>
          <div className="flex items-center space-x-4">
            <span className="flex items-center space-x-1 text-forest-700 dark:text-sage-300 font-medium">
              <span>Engineered with care for gastronomy</span>
              <Heart className="w-3.5 h-3.5 text-terracotta-500 fill-terracotta-500" />
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
};
