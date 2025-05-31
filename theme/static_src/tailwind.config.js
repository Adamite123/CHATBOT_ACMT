/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // <== penting kalau mau pakai mode gelap
  content: [
    "./templates/**/*.{html,js}", // untuk Django template
    "./static/**/*.{html,js}",    // kalau kamu punya folder static juga
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
