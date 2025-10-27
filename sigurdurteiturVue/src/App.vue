<!-- src/App.vue -->
<template>
  <div id="main-container">
    <!-- If the user is not logged in, show the login button -->
    <div v-if="!isLoggedIn" class="login-container">
      <h2>Welcome to Your Life Logger</h2>
      <p>Please sign in with Google to continue.</p>
      <button @click="handleSignIn">Sign in with Google</button>
    </div>

    <!-- If the user IS logged in, show the AppMenu component -->
    <div v-else>
      <AppMenu @logAction="logActionToSheet" @goBack="handleSignOut" />
      <button class="sign-out-button" @click="handleSignOut">Sign Out</button>
    </div>
  </div>
</template>

<script>
import { inject, toRefs, reactive } from 'vue';
import AppMenu from './components/AppMenu.vue';

export default {
  name: 'App',
  components: { AppMenu },
  setup() {
    // --- CONFIGURATION ---
    const GOOGLE_SHEET_ID = '1vMvbuGXBQxpUD7T-LxehWseh0rjt31b99adgSyfH1Hs'; // <-- Your Sheet ID
    const GOOGLE_SHEET_TAB_NAME = 'Log'; // <-- The name of the tab/worksheet

    // Inject the Google login functions provided by the plugin in main.js
    const { googleTokenLogin, googleLogout } = inject('Vue3GoogleOauth');
    
    // Reactive state to track login status
    const state = reactive({
      isLoggedIn: false,
      accessToken: null, // This will hold the temporary key to talk to Google Sheets
    });

    const handleSignIn = async () => {
      try {
        // This opens the Google login pop-up
        const response = await googleTokenLogin();
        state.isLoggedIn = true;
        state.accessToken = response.access_token; // Store the access token
        console.log("Successfully logged in!");
      } catch (error) {
        console.error("Login failed:", error);
      }
    };

    const handleSignOut = () => {
      googleLogout();
      state.isLoggedIn = false;
      state.accessToken = null;
    };

    const logActionToSheet = async (actionData) => {
      if (!state.accessToken) {
        alert("Your session has expired. Please sign in again.");
        handleSignOut();
        return;
      }

      const today_date = new Date().toISOString().split('T')[0]; // Format: YYYY-MM-DD
      
      const values = [[
        today_date,
        actionData.category,
        actionData.action,
        actionData.points,
        actionData.note
      ]];

      const body = { values: values };

      try {
        const response = await fetch(
          `https://sheets.googleapis.com/v4/spreadsheets/${GOOGLE_SHEET_ID}/values/${GOOGLE_SHEET_TAB_NAME}!A1:append?valueInputOption=USER_ENTERED`, 
          {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${state.accessToken}`, // Use the access token for permission
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
          }
        );

        const result = await response.json();

        if (!response.ok) {
          // Handle cases where the token might have expired
          if (result.error?.code === 401) {
            alert("Your login has expired. Please sign out and sign back in.");
            handleSignOut();
          }
          throw new Error(result.error?.message || 'Failed to write to sheet.');
        }
        
        console.log('Successfully wrote to sheet:', result);
        alert(`Logged: '${actionData.action}'`);

      } catch (error) {
        console.error('Error writing to Google Sheet:', error);
        alert(`Error: ${error.message}`);
      }
    };

    return {
      ...toRefs(state),
      handleSignIn,
      handleSignOut,
      logActionToSheet,
    };
  },
};
</script>

<style scoped>
#main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
}

.login-container {
  text-align: center;
}

.sign-out-button {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 10;
}
</style>