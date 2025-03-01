import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Proxy API requests to your backend server
      '/videos': {
        target: 'http://localhost:4000',
        changeOrigin: true,
        secure: false
      },
      // Proxy static video file requests to your backend server
      '/backend': {
        target: 'http://localhost:4000',
        changeOrigin: true,
        secure: false
      }
    }
  }
})