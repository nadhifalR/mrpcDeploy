module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors:{
        aqua: '#00ffff',
        green1: '#02F39B',
        green2: '#00B570',
        green3: '#1A2223',
        loginB: '#151515',
      },
      backgroundImage: theme => ({
        'home': "url('./src/assets/HomeBG.png')",
     })
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
