import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  Compass,
  FlaskConical,
  Camera,
  BookOpen,
  User,
  ShieldCheck,
  LogOut,
  LogIn,
  Menu,
  ChefHat,
  Sun,
  Moon,
  Laptop,
  PanelLeft,
  Sparkles
} from 'lucide-react';
import { api } from '../services/api';
import { User as UserType } from '../types';
import { useTheme } from '../context/ThemeContext';

interface NavbarProps {
  labCount?: number;
  onToggleSidebar?: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ labCount = 0, onToggleSidebar }) => {
  const location = useLocation();
  const navigate = useNavigate();
  const { theme, setTheme, resolvedTheme } = useTheme();
  const [currentUser, setCurrentUser] = useState<UserType | null>(null);
  const [themeDropdownOpen, setThemeDropdownOpen] = useState(false);

  useEffect(() => {
    const user = api.auth.getCurrentUser();
    setCurrentUser(user);
  }, [location.pathname]);

  const handleLogout = () => {
    api.auth.logout();
    setCurrentUser(null);
    navigate('/');
  };

  const navLinks = [
    { name: 'Explorer', path: '/ingredients', icon: Compass },
    {
      name: 'Flavor Lab',
      path: '/lab',
      icon: FlaskConical,
      badge: labCount > 0 ? labCount : undefined,
    },
    { name: 'Identify Food', path: '/vision', icon: Camera },
    { name: 'Discover', path: '/discover', icon: Sparkles },
    { name: 'Catalog', path: '/recipe-library', icon: BookOpen },
    { name: 'Recipes', path: '/recipes', icon: ChefHat },
  ];

  return (
    <header className="sticky top-0 z-30 bg-ivory-50/90 dark:bg-[#121815]/90 backdrop-blur-md border-b border-ivory-300 dark:border-forest-900 transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Left: Sidebar Toggle + Brand */}
          <div className="flex items-center space-x-3 sm:space-x-4">
            {/* Sidebar toggle button (Mobile & Desktop) */}
            <button
              onClick={onToggleSidebar}
              className="p-2 rounded-xl text-stone-600 dark:text-stone-300 hover:text-forest-700 dark:hover:text-sage-300 hover:bg-ivory-200 dark:hover:bg-forest-900/60 border border-ivory-300 dark:border-forest-800 transition-all cursor-pointer"
              title="Toggle Sidebar Navigation"
              aria-label="Toggle Sidebar"
            >
              <PanelLeft className="w-5 h-5" />
            </button>

            {/* Logo & Brand */}
            <Link to="/" className="flex items-center space-x-3 group">
              <div className="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-forest-600 dark:bg-forest-500 text-ivory-50 flex items-center justify-center shadow-xs group-hover:bg-forest-500 transition-all duration-200 shrink-0">
                <ChefHat className="w-5 h-5 sm:w-6 sm:h-6 text-sage-200" />
              </div>
              <div className="hidden xs:block">
                <div className="flex items-center space-x-1.5">
                  <span className="font-serif text-xl sm:text-2xl font-bold tracking-tight text-forest-800 dark:text-ivory-50">
                    FlavorFusion
                  </span>
                  <span className="text-[10px] sm:text-xs font-semibold uppercase tracking-wider px-1.5 py-0.5 rounded bg-sage-100 dark:bg-forest-900 text-forest-700 dark:text-sage-300 border border-sage-200 dark:border-forest-700">
                    AI
                  </span>
                </div>
                <p className="text-[10px] sm:text-[11px] text-stone-500 dark:text-stone-400 font-medium tracking-wide hidden sm:block">
                  Culinary Chemistry & Taste Intelligence
                </p>
              </div>
            </Link>
          </div>

          {/* Desktop Navigation Links */}
          <nav className="hidden lg:flex items-center space-x-1 xl:space-x-2">
            {navLinks.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  className={`relative flex items-center space-x-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition-all ${
                    isActive
                      ? 'bg-forest-600 text-ivory-50 shadow-xs'
                      : 'text-stone-700 dark:text-stone-300 hover:text-forest-700 dark:hover:text-ivory-100 hover:bg-ivory-200 dark:hover:bg-forest-900/60'
                  }`}
                >
                  <Icon
                    className={`w-4 h-4 ${
                      isActive ? 'text-sage-200' : 'text-stone-500 dark:text-stone-400'
                    }`}
                  />
                  <span>{item.name}</span>
                  {item.badge !== undefined && (
                    <span
                      className={`text-[10px] font-bold px-1.5 py-0.2 rounded-full ${
                        isActive ? 'bg-terracotta-500 text-white' : 'bg-forest-600 text-white'
                      }`}
                    >
                      {item.badge}
                    </span>
                  )}
                </Link>
              );
            })}
          </nav>

          {/* Right Controls: Theme Selector & User Actions */}
          <div className="flex items-center space-x-2 sm:space-x-3">
            {/* Theme Selector Dropdown */}
            <div className="relative">
              <button
                onClick={() => setThemeDropdownOpen(!themeDropdownOpen)}
                className="p-2 rounded-xl text-stone-600 dark:text-stone-300 hover:bg-ivory-200 dark:hover:bg-forest-900/60 border border-ivory-300 dark:border-forest-800 transition-all cursor-pointer"
                title={`Theme: ${theme}`}
                aria-label="Change theme"
              >
                {resolvedTheme === 'dark' ? (
                  <Moon className="w-4 h-4 text-sage-300" />
                ) : (
                  <Sun className="w-4 h-4 text-amber-600" />
                )}
              </button>

              {themeDropdownOpen && (
                <div className="absolute right-0 mt-2 w-36 rounded-xl bg-white dark:bg-[#1a2320] border border-ivory-300 dark:border-forest-800 shadow-xl py-1.5 z-50 text-xs font-medium">
                  <button
                    onClick={() => {
                      setTheme('light');
                      setThemeDropdownOpen(false);
                    }}
                    className={`w-full flex items-center space-x-2 px-3 py-2 text-left hover:bg-ivory-100 dark:hover:bg-forest-900 transition-colors ${
                      theme === 'light'
                        ? 'text-forest-700 dark:text-sage-300 font-bold bg-ivory-50 dark:bg-forest-900/40'
                        : 'text-stone-700 dark:text-stone-300'
                    }`}
                  >
                    <Sun className="w-4 h-4 text-amber-500" />
                    <span>Light</span>
                  </button>
                  <button
                    onClick={() => {
                      setTheme('dark');
                      setThemeDropdownOpen(false);
                    }}
                    className={`w-full flex items-center space-x-2 px-3 py-2 text-left hover:bg-ivory-100 dark:hover:bg-forest-900 transition-colors ${
                      theme === 'dark'
                        ? 'text-forest-700 dark:text-sage-300 font-bold bg-ivory-50 dark:bg-forest-900/40'
                        : 'text-stone-700 dark:text-stone-300'
                    }`}
                  >
                    <Moon className="w-4 h-4 text-sage-400" />
                    <span>Dark</span>
                  </button>
                  <button
                    onClick={() => {
                      setTheme('system');
                      setThemeDropdownOpen(false);
                    }}
                    className={`w-full flex items-center space-x-2 px-3 py-2 text-left hover:bg-ivory-100 dark:hover:bg-forest-900 transition-colors ${
                      theme === 'system'
                        ? 'text-forest-700 dark:text-sage-300 font-bold bg-ivory-50 dark:bg-forest-900/40'
                        : 'text-stone-700 dark:text-stone-300'
                    }`}
                  >
                    <Laptop className="w-4 h-4 text-stone-500" />
                    <span>System</span>
                  </button>
                </div>
              )}
            </div>

            {/* Admin shortcut badge if admin */}
            {currentUser?.is_admin && (
              <Link
                to="/admin"
                className={`hidden sm:flex items-center space-x-1 px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                  location.pathname === '/admin'
                    ? 'bg-terracotta-600 text-white border-terracotta-600'
                    : 'bg-terracotta-50 dark:bg-terracotta-900/30 text-terracotta-700 dark:text-terracotta-300 border-terracotta-200 dark:border-terracotta-800 hover:bg-terracotta-100'
                }`}
              >
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>Admin</span>
              </Link>
            )}

            {/* User Profile / Auth buttons */}
            {currentUser ? (
              <div className="flex items-center space-x-2 pl-2 border-l border-ivory-300 dark:border-forest-900">
                <Link
                  to="/profile"
                  className="flex items-center space-x-2 px-2.5 py-1.5 rounded-xl text-xs font-semibold text-stone-700 dark:text-stone-200 hover:bg-ivory-200 dark:hover:bg-forest-900 transition-all"
                  title="My Taste Profile"
                >
                  <div className="w-7 h-7 rounded-full bg-sage-200 dark:bg-forest-800 text-forest-700 dark:text-sage-200 flex items-center justify-center font-bold text-xs">
                    {currentUser.full_name ? currentUser.full_name.charAt(0) : 'U'}
                  </div>
                  <span className="max-w-[90px] truncate hidden md:inline">
                    {currentUser.full_name || 'Chef'}
                  </span>
                </Link>
                <button
                  onClick={handleLogout}
                  className="p-1.5 rounded-lg text-stone-500 hover:text-terracotta-600 hover:bg-ivory-200 dark:hover:bg-forest-900 transition-all cursor-pointer"
                  title="Log out"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-1.5">
                <Link
                  to="/login"
                  className="flex items-center space-x-1 px-3 py-1.5 rounded-xl text-xs font-semibold text-forest-700 dark:text-sage-300 hover:bg-ivory-200 dark:hover:bg-forest-900 border border-ivory-300 dark:border-forest-800 transition-all"
                >
                  <LogIn className="w-3.5 h-3.5" />
                  <span>Sign In</span>
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};
