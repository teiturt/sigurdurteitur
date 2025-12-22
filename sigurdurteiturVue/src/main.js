// src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import '@/assets/global.css'
import GoogleSignInPlugin from 'vue3-google-signin'

const app = createApp(App)

// Initialize the Google OAuth plugin
app.use(GoogleSignInPlugin, {
  clientId: '182347241497-dfh8l73tvbs60iaj4qp6lk2iabde3ahd.apps.googleusercontent.com',
})

app.mount('#app')