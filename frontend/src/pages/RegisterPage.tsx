import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ChefHat, UserPlus, AlertCircle } from 'lucide-react';
import { api } from '../services/api';

export const RegisterPage: React.FC = () => {
  const navigate = useNavigate();
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      await api.auth.register({ email, password, full_name: fullName });
      navigate('/profile'); // Guide new user to setup taste profile
    } catch (err: any) {
      setError(err.message || 'Registration failed');
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
        <h1 className="font-serif text-3xl font-bold text-stone-900 dark:text-ivory-50">Create an Account</h1>
        <p className="text-xs text-stone-500 dark:text-stone-400">Save your taste profiles, wishlisted dishes, and formulas to your personal database.</p>
      </div>

      {error && (
        <div className="p-3.5 rounded-xl bg-terracotta-50 dark:bg-terracotta-950/40 border border-terracotta-200 dark:border-terracotta-800 text-terracotta-800 dark:text-terracotta-200 text-xs flex items-center space-x-2">
          <AlertCircle className="w-4 h-4 shrink-0 text-terracotta-600" />
          <span>{error}</span>
        </div>
      )}

      <form onSubmit={handleRegister} className="bg-white dark:bg-[#151c19] p-6 rounded-3xl border border-ivory-300 dark:border-forest-900 shadow-sm space-y-4 text-xs">
        <div>
          <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Full Name</label>
          <input
            type="text"
            required
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            placeholder="Chef Priya Sharma"
            className="w-full px-3 py-2.5 rounded-xl bg-ivory-50 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-900 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
          />
        </div>

        <div>
          <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Email Address</label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="priya@example.com"
            className="w-full px-3 py-2.5 rounded-xl bg-ivory-50 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-900 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
          />
        </div>

        <div>
          <label className="block font-semibold text-stone-700 dark:text-stone-300 mb-1">Password</label>
          <input
            type="password"
            required
            minLength={6}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="At least 6 characters"
            className="w-full px-3 py-2.5 rounded-xl bg-ivory-50 dark:bg-[#1d2622] border border-ivory-300 dark:border-forest-800 text-stone-900 dark:text-ivory-100 text-sm focus:outline-none focus:ring-1 focus:ring-forest-500"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full py-3 rounded-xl bg-forest-600 hover:bg-forest-500 text-white font-semibold text-sm shadow-md transition-all flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          <UserPlus className="w-4 h-4" />
          <span>{loading ? 'Creating Account...' : 'Get Started'}</span>
        </button>
      </form>

      <p className="text-center text-xs text-stone-500 dark:text-stone-400">
        Already have an account?{' '}
        <Link to="/login" className="font-semibold text-forest-700 dark:text-sage-300 hover:underline">
          Sign in here
        </Link>
      </p>
    </div>
  );
};
