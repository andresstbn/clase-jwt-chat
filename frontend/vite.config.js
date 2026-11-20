import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  // Puerto fijo: es el que el backend tiene permitido en CORS.
  server: { port: 5173, strictPort: true },
})
