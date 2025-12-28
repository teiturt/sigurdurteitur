<template>
  <div class="console-page">
    <div class="back-nav">
      <router-link to="/games">← Back to Playroom</router-link>
    </div>
    <GameConsole />
  </div>
</template>

<script>
import GameConsole from "../components/console/GameConsole.vue";

export default {
  name: "ConsoleView",
  components: { GameConsole },
};
</script>

<style scoped>
.console-page {
  min-height: 100vh;
  background: #222; /* Dark background to make the console pop */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.back-nav {
  position: absolute;
  top: 40px;
  left: 40px;
}

.back-nav a {
  color: #fff;
  text-decoration: none;
  font-family: "Courier New", monospace;
  font-weight: bold;
  opacity: 0.5;
  transition: opacity 0.2s;
}

.back-nav a:hover {
  opacity: 1;
}
</style>
