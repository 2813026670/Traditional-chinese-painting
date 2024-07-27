import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: { // 添加server配置项
    proxy: {
      '/get_palette': {  
        target: 'http://127.0.0.1:5001',  
        changeOrigin: true,  
        // 使用 pathRewrite 而不是 rewrite  
        pathRewrite: {  
          '^/get_palette': ''  
        }  
      },  
      '/get_latest_images': {  
        target: 'http://127.0.0.1:5000',  
        changeOrigin: true,  
        pathRewrite: {  
          '^/get_latest_images': ''  
        }  
      } 

    },
  },
})
