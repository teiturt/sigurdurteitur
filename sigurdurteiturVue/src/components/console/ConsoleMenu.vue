<template>
  <div class="menu-screen">
    <h3>SELECT GAME</h3>
    <ul>
      <li :class="{ active: selected === 0 }">SNAKE</li>
      <li :class="{ active: selected === 1 }">VOID PILOT (3D)</li>
    </ul>
    <div class="hint">PRESS 'A' TO START</div>
  </div>
</template>

<script>
export default {
  data() {
    return { selected: 0 };
  },
  methods: {
    onInput(cmd) {
      if (cmd === "UP" || cmd === "DOWN") {
        this.selected = this.selected === 0 ? 1 : 0;
      }
      if (cmd === "A" || cmd === "START") {
        if (this.selected === 0) this.$emit("launchGame", "SnakeGame");
        // Since Void Pilot is 3D, we might want to route to the full page
        if (this.selected === 1) this.$router.push("/games/void-pilot");
      }
    },
  },
};
</script>

<style scoped>
.menu-screen {
  padding: 20px;
  font-family: "Courier New", monospace;
  font-weight: bold;
  color: #0f380f; /* Dark Green text on Light Green bg */
}
ul {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}
li {
  padding: 5px 0;
}
li.active::before {
  content: "> ";
}
.hint {
  font-size: 0.7rem;
  margin-top: 40px;
  text-align: center;
}
</style>
