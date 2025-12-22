<!-- src/App.vue -->
<template>
  <div id="main-container">
    <!-- If the user is not logged in, show the login button -->
    <div v-if="!isLoggedIn" class="login-container">
      <h2>Welcome to Your Life Logger</h2>
      <p>Please sign in with Google to continue.</p>
      
      <!-- 
        THIS IS THE KEY CHANGE: The button is disabled until the Google Script is fully loaded.
        This prevents the "is not a function" error.
      -->
      <button @click="handleSignIn" :disabled="!isReady">
        {{ isReady ? 'Sign in with Google' : 'Loading...' }}
      </button>

    </div>

    <!-- If the user IS logged in, show the AppMenu component -->
    <div v-else>
      <AppMenu @logAction="logActionToSheet" @goBack="handleSignOut" />
      <button class="sign-out-button" @click="handleSignOut">Sign Out</button>
    </div>
  </div>
</template>

<script>
import { toRefs, reactive } from 'vue';
import AppMenu from './components/AppMenu.vue';

// THIS IS THE KEY CHANGE: We import 'useGsiScript' to manage loading.
import { useGsiScript, useTokenClient, revokeAccessToken } from 'vue3-google-signin';

export default {
  name: 'App',
  components: { AppMenu },
  setup() {
    // --- CONFIGURATION ---
    const GOOGLE_SHEET_ID = '1vMvbuGXBQxpUD7T-LxehWseh0rjt31b99adgSyfH1Hs';
    const GOOGLE_SHEET_TAB_NAME = 'Log';

    // This loads the Google script and gives us a reactive 'isReady' flag.
    const { isReady } = useGsiScript();

    // We can still get the token client function here.
    const { requestAccessToken } = useTokenClient();
    
    const state = reactive({
      isLoggedIn: false,
      accessToken: null,
    });

    const handleSignIn = () => {
      // Because the button is disabled until isReady=true, we know that
      // requestAccessToken will exist when this function is called.
      requestAccessToken({ scope: 'https://www.googleapis.com/auth/spreadsheets' })
        .then((response) => {
          state.isLoggedIn = true;
          state.accessToken = response.access_token;
          console.log("Successfully logged in!", response);
        })
        .catch((error) => {
          console.error("Login failed:", error);
        });
    };

    const handleSignOut = async () => {
      if (state.accessToken) {
        await revokeAccessToken(state.accessToken);
      }
      state.isLoggedIn = false;
      state.accessToken = null;
    };

    const logActionToSheet = async (actionData) => {
      if (!state.accessToken) {
        alert("Your session has expired. Please sign in again.");
        handleSignOut();
        return;
      }
      
      const today_date = new Date().toISOString().split('T')[0];
      const values = [[ today_date, actionData.category, actionData.action, actionData.points, actionData.note ]];
      const body = { values: values };

      try {
        const response = await fetch(
          `https://sheets.googleapis.com/v4/spreadsheets/${GOOGLE_SHEET_ID}/values/${GOOGLE_SHEET_TAB_NAME}!A1:append?valueInputOption=USER_ENTERED`, 
          {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${state.accessToken}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
          }
        );

        const result = await response.json();
        if (!response.ok) {
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
      isReady, // We must return 'isReady' so the template can use it.
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