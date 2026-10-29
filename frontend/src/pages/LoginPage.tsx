import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ChefHat, LogIn, AlertCircle, Sparkles, ShieldCheck } from 'lucide-react';
import { api } from '../services/api';

export const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      await api.auth.login({ email, password });
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Invalid email or password.');
    } finally {
      setLoading(false);
    }
  };

  const loginAsDemo = async (role: 'gourmet' | 'admin') => {
    const creds =
      role === 'admin'
        ? { email: 'admin@flavorfusion.ai', password: 'AdminPass123!' }
        : { email: 'gourmet@flavorfusion.ai', password: 'Gourmet123!' };

    setLoading(true);
    setError(null);
    try {
      await api.auth.login(creds);
      navigate(role === 'admin' ? '/admin' : '/dashboard');
    } catch (err: any) {
      setError(err.message || 'Demo login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto px-4 py-16 space-y-8">
      <div className="text-center space-y-2">
        <div className="w-12 h-12 rounded-2xl bg-forest-600 dark:bg-forest-500 text-ivory-50 flex items-center justify-center mx-auto shadow-sm">
          <ChefHat className="w-6 h-6 text-sage-200" />
        </div>
        <h1 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50">Sign in to FlavorFusion</h1>
        <p className="text-xs text-stone-500 dark:text-stone-400">Access saved recipes, wishlist dishes, and personalized taste profiles.</p>
      </div>

      {error && (
        <div className="p-3.5 rounded-xl bg-terracotta-50 dark:bg-terracotta-950/40 border border-terracotta-200 dark:border-terracotta-800 text-terracotta-800 dark:text-terracotta-200 text-xs flex items-center space-x-2">
          <AlertCircle className="w-4 h-4 shrink-0 text-terracotta-600" />
          <span>{error}</span>
        </div>
      )}

      {/* Quick Demo Login Buttons */}
      <div className="bg-ivory-50 dark:bg-[#151c19] p-4 rounded-2xl border border-ivory-300 dark:border-forest-900 space-y-2.5">
        <span className="text-[11px] font-bold uppercase tracking-wider text-stone-400 dark:text-stone-400 block text-center">
          Instant Demo Logins (Stored in DB)
        </span>
        <div className="grid grid-cols-2 gap-2">
          <button
            type="button"
            onClick={() => loginAsDemo('gourmet')}
            className="flex items-center justify-center space-x-1.5 py-2 px-3 rounded-xl bg-white dark:bg-[#1d2622] hover:bg-ivory-100 dark:hover:bg-forest-900 text-stone-800 dark:text-stone-200 text-xs font-semibold border border-ivory-300 dark:border-forest-800 shadow-sm transition-all"
          >
            <Sparkles className="w-3.5 h-3.5 text-forest-600 dark:text-sage-300" />
            <span>Demo Gourmet</span>
          </button>
          <button
            type="button"
            onClick={() => loginAsDemo('admin')}
            className="flex items-center justify-center space-x-1.5 py-2 px-3 rounded-xl bg-white dark:bg-[#1d2622] hover:bg-ivory-100 dark:hover:bg-forest-900 text-stone-800 dark:text-stone-200 text-xs font-semibold border border-ivory-300 dark:border-forest-800 shadow-sm transition-all"
          >
            <ShieldCheck className="w-3.5 h-3.5 text-terracotta-600 dark:text-terracotta-400" />
            <span>Admin Chef</span>
          </button>
        </div>
      </div>

      {/* Main Form */}
      <form onSubmit={handleLogin} className="bg-white dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-4 text-xs">
        <div>
          <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Email Address</label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="chef@example.com"
            className="w-full px-3 py-2.5 rounded-xl bg-ivory-50 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-900 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
          />
        </div>

        <div>
          <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Password</label>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
            className="w-full px-3 py-2.5 rounded-xl bg-ivory-50 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-900 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full py-3 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-md transition-all flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          <LogIn className="w-4 h-4" />
          <span>{loading ? 'Signing in...' : 'Sign In'}</span>
        </button>
      </form>

      <p className="text-center text-xs text-stone-500 dark:text-stone-400">
        Don't have an account yet?{' '}
        <Link to="/register" className="font-semibold text-forest-700 dark:text-sage-300 hover:underline">
          Join free now
        </Link>
      </p>
    </div>
  );
};
