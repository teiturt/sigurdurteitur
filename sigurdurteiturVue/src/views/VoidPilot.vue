<template>
  <div class="game-page">
    <AppMenu @goBack="exitGame" />
  </div>
</template>

<script>
// We go up one level (..) then into components
import AppMenu from "../components/AppMenu.vue";

export default {
  name: "VoidPilotView",
  components: { AppMenu },
  methods: {
    exitGame() {
      // Use the router to go back to the hub instead of an emit
      this.$router.push("/games");
    },
  },
};
</script>

<style scoped>
.game-page {
  background: black;
  width: 100vw;
  height: 100vh;
}
</style>
