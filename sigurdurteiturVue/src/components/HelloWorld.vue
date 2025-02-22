<template>
  <!-- Container uses either "light" or "dark" class -->
  <div :class="{ dark: isDark, light: !isDark }" class="container">
    <!-- We use a transition with custom events to handle the timing -->
    <transition
      name="expand"
      @before-leave="beforeLeave"
      @after-leave="afterLeave"
    >
      <!-- The button is shown if showButton is true -->
      <button v-if="showButton" @click="toggleTheme" class="press-button">
        Sigurður Teitur.
      </button>
    </transition>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      isDark: false,
      showButton: true
    }
  },
  methods: {
    // Called when the user clicks the button
    toggleTheme() {
      // This will trigger the leaving transition on the old button
      this.showButton = false
    },
    // Called just before the leaving transition starts
    beforeLeave() {
      // You could do something here if needed,
      // but typically no action is required.
    },
    // Called right after the leaving transition finishes
    afterLeave() {
      // The old button is now removed from the DOM
      // Toggle the background theme instantly (no flash)
      this.isDark = !this.isDark
      // Show the new button, triggering the entering transition
      this.showButton = true
    }
  }
}
</script>

<style scoped>
/* Make sure there are no default margins/padding interfering */
.container {
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Light vs Dark background colors */
.light {
  background-color: white;
}
.dark {
  background-color: black;
}

/* Example button styling (tweak to suit your design) */
.press-button {
  border-radius: 8px;
  padding: 0.75rem 1.5rem;
  font-size: 1.2rem;
  cursor: pointer;
  border: 2px solid;
  /* Light mode button: black with white text/border */
}
.light .press-button {
  background-color: black;
  color: white;
  border-color: white;
}
/* Dark mode button: white with black text/border */
.dark .press-button {
  background-color: white;
  color: black;
  border-color: black;
}

/* -----------------------------
   EXPAND TRANSITION ANIMATION
   ----------------------------- */

/* 
  By default, Vue applies:
    - expand-leave-active when removing the element
    - expand-enter-active when inserting the element
*/

/* We set a common transform origin. Center is typical. */
.expand-leave-active,
.expand-enter-active {
  transform-origin: center center;
}

/* The old button scales from 1 to ~20, covering the screen */
.expand-leave-active {
  animation: expand-out 0.5s forwards;
}

/* The new button scales from 0 to 1 */
.expand-enter-active {
  animation: expand-in 0.5s forwards;
}

/* Keyframes for expanding out (cover the screen) */
@keyframes expand-out {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(700); /* Adjust if needed to fully cover */
  }
}

/* Keyframes for expanding in (appear from nothing) */
@keyframes expand-in {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
</style>
