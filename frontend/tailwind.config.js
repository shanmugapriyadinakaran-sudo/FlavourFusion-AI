/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ivory: {
          50: '#FDFCFB',
          100: '#FAF7F2',
          200: '#F4EFEA',
          300: '#ECE4DC',
          400: '#DFD3C6',
          800: '#1a1f1d',
          900: '#121715',
          950: '#0b0f0d',
        },
        forest: {
          50: '#E8F5E9',
          100: '#C8E6C9',
          200: '#A1D9A5',
          400: '#40916C',
          500: '#2D6A4F',
          600: '#1B4332',
          700: '#143628',
          800: '#0E271D',
          900: '#081812',
          950: '#040d0a',
        },
        sage: {
          50: '#F2F8F5',
          100: '#D8F3DC',
          200: '#B7E4C7',
          300: '#95D5B2',
          400: '#74C69D',
          500: '#52B788',
          600: '#40916C',
        },
        terracotta: {
          50: '#FDF6F0',
          100: '#FAECE1',
          200: '#F5D3BF',
          300: '#EEB197',
          400: '#E6896C',
          500: '#D96543',
          600: '#C85A32',
          700: '#A84523',
          800: '#7A2E14',
          900: '#4D1A0A',
          950: '#2A0E05',
        },
        darkcard: {
          50: '#232b28',
          100: '#1c2320',
          200: '#161d1a',
          300: '#121715',
          400: '#0d110f',
        }
      },
      fontFamily: {
        serif: ['Playfair Display', 'Merriweather', 'Georgia', 'serif'],
        sans: ['Plus Jakarta Sans', 'Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
