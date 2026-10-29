import React from 'react';
import { useTheme } from '../context/ThemeContext';

interface CompatibilityGaugeProps {
  score: number;
  label: string;
  sublabel?: string;
  size?: 'sm' | 'md' | 'lg';
  highlightColor?: string;
}

export const CompatibilityGauge: React.FC<CompatibilityGaugeProps> = ({
  score,
  label,
  sublabel,
  size = 'md',
  highlightColor,
}) => {
  const { resolvedTheme } = useTheme();
  const isDark = resolvedTheme === 'dark';

  // Determine vibrant, high-contrast color based on score and theme
  const getColor = () => {
    if (highlightColor) return highlightColor;
    if (isDark) {
      if (score >= 85) return '#52B788'; // Vibrant Luminous Sage Green
      if (score >= 70) return '#74C69D'; // Soft Luminous Green
      if (score >= 50) return '#F4A261'; // Warm Terracotta Orange
      return '#E76F51'; // Coral Terracotta
    } else {
      if (score >= 85) return '#2D6A4F'; // Forest Green
      if (score >= 70) return '#52B788'; // Sage Green
      if (score >= 50) return '#D96543'; // Terracotta Warm
      return '#A84523'; // Deep Terracotta
    }
  };

  const getStatusText = () => {
    if (score >= 88) return 'Exceptional Synergy';
    if (score >= 75) return 'Harmonious Balance';
    if (score >= 60) return 'Pleasant Contrast';
    if (score >= 40) return 'Experimental Match';
    return 'Challenging Palette';
  };

  const dimensions = {
    sm: { size: 100, strokeWidth: 8, fontSize: 'text-xl' },
    md: { size: 140, strokeWidth: 10, fontSize: 'text-3xl' },
    lg: { size: 180, strokeWidth: 14, fontSize: 'text-5xl' },
  }[size];

  const radius = (dimensions.size - dimensions.strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (Math.min(score, 100) / 100) * circumference;

  // Background track color tailored for theme
  const trackColor = isDark ? '#233229' : '#ECE4DC';

  return (
    <div className="flex flex-col items-center text-center">
      <div
        className="relative flex items-center justify-center"
        style={{ width: dimensions.size, height: dimensions.size }}
      >
        <svg
          className="transform -rotate-90"
          width={dimensions.size}
          height={dimensions.size}
        >
          {/* Background Track */}
          <circle
            cx={dimensions.size / 2}
            cy={dimensions.size / 2}
            r={radius}
            stroke={trackColor}
            strokeWidth={dimensions.strokeWidth}
            fill="transparent"
          />
          {/* Animated Value Arc */}
          <circle
            cx={dimensions.size / 2}
            cy={dimensions.size / 2}
            r={radius}
            stroke={getColor()}
            strokeWidth={dimensions.strokeWidth}
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            fill="transparent"
            className="transition-all duration-1000 ease-out"
          />
        </svg>

        {/* Center Text with High Contrast in Dark & Light Modes */}
        <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
          <span
            className={`font-serif font-bold tracking-tight text-forest-800 dark:text-ivory-50 ${dimensions.fontSize}`}
          >
            {Math.round(score)}%
          </span>
          <span className="text-[10px] uppercase font-bold tracking-wider text-stone-500 dark:text-stone-300">
            Score
          </span>
        </div>
      </div>

      <div className="mt-3">
        <h4 className="font-semibold text-stone-900 dark:text-ivory-100 text-sm">{label}</h4>
        <p className="text-xs text-forest-600 dark:text-sage-300 font-semibold">{getStatusText()}</p>
        {sublabel && (
          <p className="text-[11px] text-stone-500 dark:text-stone-300 mt-0.5">{sublabel}</p>
        )}
      </div>
    </div>
  );
};
