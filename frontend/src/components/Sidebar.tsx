import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  Sparkles,
  Compass,
  FlaskConical,
  Camera,
  BookOpen,
  User,
  ShieldCheck,
  LogOut,
  LogIn,
  UserPlus,
  ChefHat,
  ChevronLeft,
  ChevronRight,
  Sun,
  Moon,
  Laptop,
  Home,
  Bookmark,
  X
} from 'lucide-react';
import { api } from '../services/api';
import { User as UserType } from '../types';
import { useTheme } from '../context/ThemeContext';

interface SidebarProps {
  labCount?: number;
  isOpenMobile: boolean;
  onCloseMobile: () => void;
  isCollapsedDesktop: boolean;
  onToggleCollapseDesktop: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({
  labCount = 0,
  isOpenMobile,
  onCloseMobile,
  isCollapsedDesktop,
  onToggleCollapseDesktop,
}) => {
  const location = useLocation();
  const navigate = useNavigate();
  const { theme, setTheme, resolvedTheme } = useTheme();
  const [currentUser, setCurrentUser] = useState<UserType | null>(null);

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
    { name: 'Home', path: '/', icon: Home },
    { name: 'Explorer', path: '/ingredients', icon: Compass },
    {
      name: 'Flavor Lab',
      path: '/lab',
      icon: FlaskConical,
      badge: labCount > 0 ? labCount : undefined,
    },
    { name: 'Identify Food', path: '/vision', icon: Camera },
    { name: 'Discover', path: '/discover', icon: Sparkles },
    { name: 'Recipe Catalog', path: '/recipe-library', icon: BookOpen },
    { name: 'Recipe Generator', path: '/recipes', icon: ChefHat },
    { name: 'My Profile', path: '/profile', icon: User },
    { name: 'Dashboard', path: '/dashboard', icon: Bookmark },
  ];

  return (
    <>
      {/* Mobile Backdrop Overlay */}
      {isOpenMobile && (
        <div
          onClick={onCloseMobile}
          className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs lg:hidden transition-opacity"
        />
      )}

      {/* Sidebar Container */}
      <aside
        className={`fixed top-0 bottom-0 left-0 z-50 flex flex-col bg-ivory-50/95 dark:bg-[#121815]/95 backdrop-blur-md border-r border-ivory-300 dark:border-forest-900 transition-all duration-300 ease-in-out lg:z-30 ${
          // Mobile visibility
          isOpenMobile ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        } ${
          // Desktop width
          isCollapsedDesktop ? 'lg:w-20' : 'lg:w-64'
        } w-72`}
      >
        {/* Brand Header */}
        <div className="h-20 flex items-center justify-between px-4 border-b border-ivory-300 dark:border-forest-900 shrink-0">
          <Link
            to="/"
            onClick={onCloseMobile}
            className="flex items-center space-x-3 group overflow-hidden"
          >
            <div className="w-10 h-10 rounded-xl bg-forest-600 dark:bg-forest-500 text-ivory-50 flex items-center justify-center shadow-xs group-hover:bg-forest-500 transition-all shrink-0">
              <ChefHat className="w-5 h-5 text-sage-200" />
            </div>
            {!isCollapsedDesktop && (
              <div className="truncate">
                <div className="flex items-center space-x-1.5">
                  <span className="font-serif text-lg font-bold tracking-tight text-forest-800 dark:text-ivory-50">
                    FlavorFusion
                  </span>
                  <span className="text-[10px] font-bold uppercase tracking-wider px-1.5 py-0.2 rounded bg-sage-100 dark:bg-forest-900 text-forest-700 dark:text-sage-300 border border-sage-200 dark:border-forest-700">
                    AI
                  </span>
                </div>
                <p className="text-[10px] text-stone-500 dark:text-stone-400 font-medium truncate">
                  Taste Intelligence
                </p>
              </div>
            )}
          </Link>

          {/* Mobile close button */}
          <button
            onClick={onCloseMobile}
            className="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:text-stone-400 dark:hover:text-ivory-100 lg:hidden"
          >
            <X className="w-5 h-5" />
          </button>

          {/* Desktop collapse / expand button */}
          <button
            onClick={onToggleCollapseDesktop}
            className="hidden lg:flex p-1.5 rounded-lg text-stone-400 hover:text-forest-700 dark:hover:text-sage-300 hover:bg-ivory-200 dark:hover:bg-forest-900/60 transition-colors"
            title={isCollapsedDesktop ? 'Expand sidebar' : 'Collapse sidebar'}
          >
            {isCollapsedDesktop ? (
              <ChevronRight className="w-4 h-4" />
            ) : (
              <ChevronLeft className="w-4 h-4" />
            )}
          </button>
        </div>

        {/* Navigation Items */}
        <div className="flex-1 overflow-y-auto px-3 py-4 space-y-1.5">
          {navLinks.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;

            return (
              <Link
                key={item.name}
                to={item.path}
                onClick={onCloseMobile}
                title={isCollapsedDesktop ? item.name : undefined}
                className={`relative flex items-center rounded-xl text-xs font-semibold transition-all ${
                  isCollapsedDesktop ? 'justify-center p-3' : 'space-x-3 px-3.5 py-2.5'
                } ${
                  isActive
                    ? 'bg-forest-600 text-ivory-50 shadow-sm'
                    : 'text-stone-700 dark:text-stone-300 hover:text-forest-700 dark:hover:text-ivory-100 hover:bg-ivory-200 dark:hover:bg-forest-900/60'
                }`}
              >
                <Icon
                  className={`shrink-0 ${
                    isCollapsedDesktop ? 'w-5 h-5' : 'w-4 h-4'
                  } ${isActive ? 'text-sage-200' : 'text-stone-500 dark:text-stone-400'}`}
                />
                {!isCollapsedDesktop && <span className="truncate">{item.name}</span>}

                {/* Badge for Flavor Lab items count */}
                {item.badge !== undefined && (
                  <span
                    className={`text-[10px] font-bold px-1.5 py-0.2 rounded-full ${
                      isCollapsedDesktop
                        ? 'absolute top-1 right-1 bg-terracotta-500 text-white text-[9px] w-4 h-4 flex items-center justify-center p-0'
                        : isActive
                        ? 'bg-terracotta-500 text-white ml-auto'
                        : 'bg-forest-600 text-white ml-auto'
                    }`}
                  >
                    {item.badge}
                  </span>
                )}
              </Link>
            );
          })}

          {/* Admin link if user is admin */}
          {currentUser?.is_admin && (
            <Link
              to="/admin"
              onClick={onCloseMobile}
              title={isCollapsedDesktop ? 'Admin' : undefined}
              className={`flex items-center rounded-xl text-xs font-semibold border transition-all ${
                isCollapsedDesktop ? 'justify-center p-3' : 'space-x-3 px-3.5 py-2.5'
              } ${
                location.pathname === '/admin'
                  ? 'bg-terracotta-600 text-white border-terracotta-600 shadow-sm'
                  : 'bg-terracotta-50 dark:bg-terracotta-900/30 text-terracotta-700 dark:text-terracotta-300 border-terracotta-200 dark:border-terracotta-800 hover:bg-terracotta-100'
              }`}
            >
              <ShieldCheck className="w-4 h-4 shrink-0" />
              {!isCollapsedDesktop && <span>Admin Portal</span>}
            </Link>
          )}
        </div>

        {/* Footer Area: Theme Switcher & User Profile */}
        <div className="p-3 border-t border-ivory-300 dark:border-forest-900 space-y-3 shrink-0">
          {/* Theme Mode Segmented Controller */}
          {!isCollapsedDesktop ? (
            <div className="p-1 rounded-xl bg-ivory-200 dark:bg-[#1a2320] border border-ivory-300 dark:border-forest-800 flex items-center justify-between text-[11px] font-medium">
              <button
                onClick={() => setTheme('light')}
                className={`flex-1 flex items-center justify-center space-x-1 py-1 rounded-lg transition-colors ${
                  theme === 'light'
                    ? 'bg-white text-forest-800 shadow-2xs font-bold'
                    : 'text-stone-600 dark:text-stone-400 hover:text-stone-900'
                }`}
                title="Light Theme"
              >
                <Sun className="w-3.5 h-3.5 text-amber-500" />
                <span>Light</span>
              </button>
              <button
                onClick={() => setTheme('dark')}
                className={`flex-1 flex items-center justify-center space-x-1 py-1 rounded-lg transition-colors ${
                  theme === 'dark'
                    ? 'bg-forest-900 text-sage-200 shadow-2xs font-bold'
                    : 'text-stone-600 dark:text-stone-400 hover:text-stone-900'
                }`}
                title="Dark Theme"
              >
                <Moon className="w-3.5 h-3.5 text-sage-300" />
                <span>Dark</span>
              </button>
              <button
                onClick={() => setTheme('system')}
                className={`flex-1 flex items-center justify-center space-x-1 py-1 rounded-lg transition-colors ${
                  theme === 'system'
                    ? 'bg-white dark:bg-forest-900 text-forest-800 dark:text-sage-200 shadow-2xs font-bold'
                    : 'text-stone-600 dark:text-stone-400 hover:text-stone-900'
                }`}
                title="System Default"
              >
                <Laptop className="w-3.5 h-3.5 text-stone-500" />
                <span>Auto</span>
              </button>
            </div>
          ) : (
            <button
              onClick={() => setTheme(resolvedTheme === 'dark' ? 'light' : 'dark')}
              className="w-full flex items-center justify-center p-2 rounded-xl bg-ivory-200 dark:bg-forest-900 text-stone-700 dark:text-sage-300 hover:bg-ivory-300 dark:hover:bg-forest-800 transition-colors"
              title={`Switch theme (currently ${theme})`}
            >
              {resolvedTheme === 'dark' ? (
                <Moon className="w-4 h-4 text-sage-300" />
              ) : (
                <Sun className="w-4 h-4 text-amber-500" />
              )}
            </button>
          )}

          {/* User Status / Login Buttons */}
          {currentUser ? (
            <div
              className={`flex items-center rounded-xl bg-ivory-100 dark:bg-[#1a2320] border border-ivory-200 dark:border-forest-800 p-2 ${
                isCollapsedDesktop ? 'justify-center' : 'justify-between'
              }`}
            >
              <Link
                to="/profile"
                onClick={onCloseMobile}
                className="flex items-center space-x-2 truncate hover:opacity-80 transition-opacity"
                title={currentUser.full_name || currentUser.email}
              >
                <div className="w-7 h-7 rounded-full bg-sage-200 dark:bg-forest-800 text-forest-700 dark:text-sage-200 flex items-center justify-center font-bold text-xs shrink-0">
                  {currentUser.full_name ? currentUser.full_name.charAt(0) : 'U'}
                </div>
                {!isCollapsedDesktop && (
                  <div className="truncate">
                    <p className="text-xs font-semibold text-stone-800 dark:text-ivory-100 truncate">
                      {currentUser.full_name || 'Chef'}
                    </p>
                    <p className="text-[10px] text-stone-500 dark:text-stone-400 truncate">
                      {currentUser.email}
                    </p>
                  </div>
                )}
              </Link>
              {!isCollapsedDesktop && (
                <button
                  onClick={handleLogout}
                  className="p-1.5 rounded-lg text-stone-400 hover:text-terracotta-600 hover:bg-ivory-200 dark:hover:bg-forest-900 transition-all shrink-0"
                  title="Sign out"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              )}
            </div>
          ) : !isCollapsedDesktop ? (
            <div className="grid grid-cols-2 gap-2">
              <Link
                to="/login"
                onClick={onCloseMobile}
                className="flex items-center justify-center space-x-1 px-3 py-2 rounded-xl bg-forest-600 hover:bg-forest-500 text-white text-xs font-semibold shadow-2xs transition-all"
              >
                <LogIn className="w-3.5 h-3.5" />
                <span>Sign In</span>
              </Link>
              <Link
                to="/register"
                onClick={onCloseMobile}
                className="flex items-center justify-center space-x-1 px-3 py-2 rounded-xl bg-ivory-200 dark:bg-forest-900 hover:bg-ivory-300 dark:hover:bg-forest-800 text-stone-800 dark:text-stone-200 text-xs font-semibold border border-ivory-300 dark:border-forest-800 transition-all"
              >
                <UserPlus className="w-3.5 h-3.5" />
                <span>Join</span>
              </Link>
            </div>
          ) : (
            <Link
              to="/login"
              onClick={onCloseMobile}
              className="flex items-center justify-center p-2 rounded-xl bg-forest-600 hover:bg-forest-500 text-white"
              title="Sign in"
            >
              <LogIn className="w-4 h-4" />
            </Link>
          )}
        </div>
      </aside>
    </>
  );
};
