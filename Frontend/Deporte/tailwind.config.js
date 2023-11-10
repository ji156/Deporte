/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "custom-purple": "#0f001d",
      },
      backgroundColor: {
        "custom-black": "rgba(15, 0, 29, 0.7)", // Define tu color personalizado con opacidad
      },
    },
  },
  plugins: [],
};
