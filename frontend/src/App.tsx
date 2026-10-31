import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { Footer } from './components/Footer';
import { AiAssistantDrawer } from './components/AiAssistantDrawer';
import { HomePage } from './pages/HomePage';
import { IngredientExplorer } from './pages/IngredientExplorer';
import { FlavorLab } from './pages/FlavorLab';
import { VisionIdentification } from './pages/VisionIdentification';
import { DiscoverPage } from './pages/DiscoverPage';
import { RecipeGenerator } from './pages/RecipeGenerator';
import { RecipeLibrary } from './pages/RecipeLibrary';
import { AnalysisResults } from './pages/AnalysisResults';
import { TasteProfile } from './pages/TasteProfile';
import { UserDashboard } from './pages/UserDashboard';
import { AdminDashboard } from './pages/AdminDashboard';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { SelectedIngredient } from './types';

export const AppContent: React.FC = () => {
  // Global active combination state for Flavor Lab (initialized empty)
  const [selectedIngredients, setSelectedIngredients] = useState<SelectedIngredient[]>([]);

  const [isAssistantOpen, setIsAssistantOpen] = useState(false);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState(false);
  const [isDesktopSidebarCollapsed, setIsDesktopSidebarCollapsed] = useState(false);

  const handleAddIngredient = (
    name: string,
    quantity: number = 100,
    unit: string = 'g',
    prep: string = 'Raw'
  ) => {
    setSelectedIngredients((prev) => {
      const clean = name.trim();
      const existing = prev.find((i) => i.name.toLowerCase() === clean.toLowerCase());
      if (existing) {
        return prev.map((i) =>
          i.name.toLowerCase() === clean.toLowerCase()
            ? { ...i, quantity: i.quantity + quantity }
            : i
        );
      }
      return [...prev, { name: clean, quantity, unit, preparation_method: prep }];
    });
  };

  const handleLoadMultipleIngredients = (ingredients: string[]) => {
    setSelectedIngredients(
      ingredients.map((name) => ({
        name: name.trim(),
        quantity: 100,
        unit: 'g',
        preparation_method: 'Raw'
      }))
    );
  };

  const handleRemoveIngredient = (index: number) => {
    setSelectedIngredients((prev) => prev.filter((_, i) => i !== index));
  };

  const handleClearAll = () => {
    setSelectedIngredients([]);
  };

  const handleUpdateQuantity = (index: number, quantity: number) => {
    setSelectedIngredients((prev) =>
      prev.map((item, i) => (i === index ? { ...item, quantity: Math.max(1, quantity) } : item))
    );
  };

  const handleUpdateUnit = (index: number, unit: string) => {
    setSelectedIngredients((prev) =>
      prev.map((item, i) => (i === index ? { ...item, unit } : item))
    );
  };

  const handleUpdatePrep = (index: number, prep: string) => {
    setSelectedIngredients((prev) =>
      prev.map((item, i) => (i === index ? { ...item, preparation_method: prep } : item))
    );
  };

  const handleToggleSidebar = () => {
    // If on mobile screen, toggle mobile drawer; if on desktop, toggle collapsed state
    if (window.innerWidth < 1024) {
      setIsMobileSidebarOpen(!isMobileSidebarOpen);
    } else {
      setIsDesktopSidebarCollapsed(!isDesktopSidebarCollapsed);
    }
  };

  return (
    <Router>
      <div className="min-h-screen flex flex-col bg-ivory-100 dark:bg-[#0c110f] text-stone-900 dark:text-ivory-100 font-sans selection:bg-sage-200 selection:text-forest-800 transition-colors duration-200">
        {/* Modern Sidebar Navigation */}
        <Sidebar
          labCount={selectedIngredients.length}
          isOpenMobile={isMobileSidebarOpen}
          onCloseMobile={() => setIsMobileSidebarOpen(false)}
          isCollapsedDesktop={isDesktopSidebarCollapsed}
          onToggleCollapseDesktop={() => setIsDesktopSidebarCollapsed(!isDesktopSidebarCollapsed)}
        />

        {/* Main Content Area (offset by sidebar on desktop) */}
        <div
          className={`flex-1 flex flex-col transition-all duration-300 ease-in-out ${
            isDesktopSidebarCollapsed ? 'lg:pl-20' : 'lg:pl-64'
          }`}
        >
          <Navbar
            labCount={selectedIngredients.length}
            onToggleSidebar={handleToggleSidebar}
          />

          <main className="flex-1">
            <Routes>
              <Route
                path="/"
                element={<HomePage onAddIngredientToLab={handleAddIngredient} />}
              />
              <Route
                path="/ingredients"
                element={<IngredientExplorer onAddIngredientToLab={handleAddIngredient} />}
              />
              <Route
                path="/lab"
                element={
                  <FlavorLab
                    selectedIngredients={selectedIngredients}
                    onRemoveIngredient={handleRemoveIngredient}
                    onClearAll={handleClearAll}
                    onUpdateQuantity={handleUpdateQuantity}
                    onUpdateUnit={handleUpdateUnit}
                    onUpdatePrep={handleUpdatePrep}
                    onAddIngredient={handleAddIngredient}
                  />
                }
              />
              <Route
                path="/vision"
                element={<VisionIdentification onAddIngredientToLab={handleAddIngredient} />}
              />
              <Route
                path="/discover"
                element={<DiscoverPage onAddIngredientToLab={handleAddIngredient} />}
              />
              <Route
                path="/recipe-library"
                element={<RecipeLibrary onAddIngredientsToLab={(items) => setSelectedIngredients(items)} />}
              />
              <Route
                path="/recipes/library"
                element={<RecipeLibrary onAddIngredientsToLab={(items) => setSelectedIngredients(items)} />}
              />
              <Route path="/recipes" element={<RecipeGenerator />} />
              <Route
                path="/analysis/:id"
                element={<AnalysisResults onAddIngredientToLab={handleAddIngredient} />}
              />
              <Route path="/profile" element={<TasteProfile />} />
              <Route path="/dashboard" element={<UserDashboard />} />
              <Route path="/admin" element={<AdminDashboard />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
            </Routes>
          </main>

          <Footer />
        </div>

        {/* Global AI Assistant Floating Button & Drawer (strictly in bottom-right corner) */}
        <AiAssistantDrawer
          isOpen={isAssistantOpen}
          onToggle={() => setIsAssistantOpen(!isAssistantOpen)}
          currentIngredients={selectedIngredients.map((i) => i.name)}
          onAddIngredients={handleLoadMultipleIngredients}
        />
      </div>
    </Router>
  );
};

export const App: React.FC = () => {
  return (
    <ThemeProvider>
      <AppContent />
    </ThemeProvider>
  );
};

export default App;
