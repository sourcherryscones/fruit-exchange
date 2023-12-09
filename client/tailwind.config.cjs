/** @type {import('tailwindcss').Config} */
module.exports= {
  content: ['./src/**/*.{svelte,js,ts}'],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("@tailwindcss/forms"), require("daisyui")],
  daisyui: {
    themes: ["emerald", "light"],
    darkTheme: "luxury",
    base:true,
    styled:true,
    utils: true,
    prefix: "",
    logs:true,
    themeRoot: ":root",
  }
}

