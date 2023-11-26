import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  build:{
    manifest: true,
    rollupOptions: {
      input: './src/main.js',
    },
    outDir: './build'
  },
  plugins: [svelte()],
  server: {
    proxy: {
      '/api': {
           target: 'http://127.0.0.1:5000',
           changeOrigin: true,
           secure: false,
       }
    }
  }
})
