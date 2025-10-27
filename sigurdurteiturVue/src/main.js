// src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import '@/assets/global.css'
import vue3GoogleOauth2 from 'vue3-google-oauth2'

const app = createApp(App)

// Initialize the Google OAuth plugin
app.use(vue3GoogleOauth2, {
  clientId: 'YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com', // <-- REPLACE WITH YOUR CLIENT ID
  scope: 'https://www.googleapis.com/auth/spreadsheets', // <-- This scope asks for permission to edit sheets
  prompt: 'consent'
})

app.mount('#app')