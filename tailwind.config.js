/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./flaskr/templates/**/*.html", // Include all HTML files in templates
    "./flaskr/static/dist/**/*.js",  // Include any JavaScript files in static
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
