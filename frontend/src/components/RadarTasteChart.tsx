import React from 'react';
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
  Tooltip
} from 'recharts';
import { useTheme } from '../context/ThemeContext';

interface RadarTasteChartProps {
  tasteProfile: {
    sweet: number;
    salty: number;
    sour: number;
    bitter: number;
    umami: number;
    spicy: number;
  };
  className?: string;
}

export const RadarTasteChart: React.FC<RadarTasteChartProps> = ({ tasteProfile, className = '' }) => {
  const { resolvedTheme } = useTheme();
  const isDark = resolvedTheme === 'dark';

  const chartData = [
    { taste: 'Sweet', value: tasteProfile.sweet || 0, fullMark: 10 },
    { taste: 'Umami', value: tasteProfile.umami || 0, fullMark: 10 },
    { taste: 'Salty', value: tasteProfile.salty || 0, fullMark: 10 },
    { taste: 'Sour', value: tasteProfile.sour || 0, fullMark: 10 },
    { taste: 'Bitter', value: tasteProfile.bitter || 0, fullMark: 10 },
    { taste: 'Spicy', value: tasteProfile.spicy || 0, fullMark: 10 },
  ];

  const gridColor = isDark ? '#273830' : '#DFD3C6';
  const labelColor = isDark ? '#E8EFEA' : '#143628';
  const radiusColor = isDark ? '#8A9991' : '#78716C';
  const radarStroke = isDark ? '#52B788' : '#2D6A4F';
  const radarFill = isDark ? '#40916C' : '#52B788';

  return (
    <div className={`w-full h-72 flex flex-col items-center justify-center ${className}`}>
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart cx="50%" cy="50%" outerRadius="75%" data={chartData}>
          <PolarGrid stroke={gridColor} />
          <PolarAngleAxis
            dataKey="taste"
            tick={{ fill: labelColor, fontSize: 12, fontWeight: 600 }}
          />
          <PolarRadiusAxis
            angle={30}
            domain={[0, 10]}
            tick={{ fill: radiusColor, fontSize: 10 }}
          />
          <Tooltip
            content={({ active, payload }) => {
              if (active && payload && payload.length) {
                const data = payload[0].payload;
                return (
                  <div className="bg-stone-900 dark:bg-[#1a2320] text-ivory-50 px-3 py-1.5 rounded-xl text-xs shadow-lg border border-transparent dark:border-forest-700">
                    <p className="font-semibold text-sage-300">{data.taste}</p>
                    <p className="font-mono text-sm">{data.value} / 10</p>
                  </div>
                );
              }
              return null;
            }}
          />
          <Radar
            name="Palate Intensity"
            dataKey="value"
            stroke={radarStroke}
            fill={radarFill}
            fillOpacity={isDark ? 0.55 : 0.45}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
};
