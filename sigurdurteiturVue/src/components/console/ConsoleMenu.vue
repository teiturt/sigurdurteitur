<template>
  <div class="menu-screen">
    <h3>SELECT GAME</h3>
    <ul>
      <li :class="{ active: selected === 0 }">SNAKE</li>
      <li :class="{ active: selected === 1 }">TETRIS</li>
      <li :class="{ active: selected === 2 }">VOID PILOT (3D)</li>
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
      if (cmd === "UP") {
        this.selected = this.selected > 0 ? this.selected - 1 : 2;
      }
      if (cmd === "DOWN") {
        this.selected = this.selected < 2 ? this.selected + 1 : 0;
      }

      if (cmd === "A" || cmd === "START") {
        if (this.selected === 0) this.$emit("launchGame", "SnakeGame");
        if (this.selected === 1) this.$emit("launchGame", "TetrisGame"); // NEW
        if (this.selected === 2) this.$router.push("/games/void-pilot");
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
  color: #0f380f;
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
