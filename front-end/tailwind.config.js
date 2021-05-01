// const { keyframes } = require("styled-components");
const plugin = require('tailwindcss/plugin')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': ['ui-sans-serif', 'system-ui'],
      'serif': ['ui-serif', 'Georgia'],
      'mono': ['ui-monospace', 'SFMono-Regular'],
      'base': ['poppins'],
      // 'base_semibold': ['poppins-semibold']
    },
    fontSize: {
      'xss': '.6rem',
      'xs': '.75rem',
      'sm': '.875rem',
      'base': '1rem',
      'lg': '1.125rem',
      'xl': '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
      '7xl': '5rem',
    },
    extend: {
      gridTemplateRows: {
       'even-4': 'repeat(4, 25%)',
      },
      colors: {
        green: '#1ded00',
        cyan: '#17e8e8',
        blue: '#001ded',
        violet: '#7532a8',
        orange: '#fe6230',
        red: '#fd0000',
        grey: '#b8bfbf'
      },
      animation: {
        ico_fill: 'ico_fill_k .2s normal forwards ease-in',
        ico_unfill: 'ico_unfill_k .2s normal forwards ease-in'
      },
      keyframes: {
        ico_fill_k: {
          '0%': { fill: "transparent" },// filter: 'drop-shadow( 0px 0px 1px currentColor)'  },
          '100%': { fill: "currentColor" }//, filter: 'drop-shadow( 0px 0px 5px currentColor)' }
        },
        ico_unfill_k: {
          '0%': { fill: "currentColor" },
          '100%': { fill: "transparent" }
        }
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    plugin(function({ addUtilities }) {
      const newUtilities = {
        'cursor-pointer': {
          cursor: 'pointer',
        },
        'button': {
          'background': 'red',
          'color': 'white'
        },
      }

      addUtilities(newUtilities)
    })
  ]
}
