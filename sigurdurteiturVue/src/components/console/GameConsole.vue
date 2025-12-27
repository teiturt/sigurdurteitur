<template>
  <div class="console-wrapper">
    <div class="console-body">
      <!-- THE SCREEN -->
      <div class="screen-bezel">
        <div class="battery-light"></div>
        <div class="lcd-screen">
          <!-- This loads the Menu, Snake, or Tetris dynamically -->
          <component
            :is="activeComponent"
            ref="currentGame"
            @launchGame="switchGame"
            @exitGame="switchGame('ConsoleMenu')"
          />
        </div>
      </div>

      <!-- THE CONTROLS -->
      <div class="controls-area">
        <div class="brand">TEITUR<span>BOY</span></div>

        <div class="d-pad">
          <button
            class="d-btn up"
            @touchstart.prevent="input('UP')"
            @mousedown.prevent="input('UP')"
          ></button>
          <button
            class="d-btn left"
            @touchstart.prevent="input('LEFT')"
            @mousedown.prevent="input('LEFT')"
          ></button>
          <button
            class="d-btn right"
            @touchstart.prevent="input('RIGHT')"
            @mousedown.prevent="input('RIGHT')"
          ></button>
          <button
            class="d-btn down"
            @touchstart.prevent="input('DOWN')"
            @mousedown.prevent="input('DOWN')"
          ></button>
          <div class="d-center"></div>
        </div>

        <div class="action-btns">
          <div class="btn-group">
            <button
              class="btn-round b-btn"
              @touchstart.prevent="input('B')"
              @mousedown.prevent="input('B')"
            >
              B
            </button>
            <button
              class="btn-round a-btn"
              @touchstart.prevent="input('A')"
              @mousedown.prevent="input('A')"
            >
              A
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ConsoleMenu from "./ConsoleMenu.vue";
import SnakeGame from "./SnakeGame.vue";

export default {
  name: "GameConsole",
  components: { ConsoleMenu, SnakeGame },
  data() {
    return {
      activeComponent: "ConsoleMenu",
    };
  },
  mounted() {
    window.addEventListener("keydown", this.handleKey);
  },
  beforeUnmount() {
    window.removeEventListener("keydown", this.handleKey);
  },
  methods: {
    switchGame(gameName) {
      this.activeComponent = gameName;
    },
    input(command) {
      // We call a specific method 'onInput' inside the active game component
      if (this.$refs.currentGame && this.$refs.currentGame.onInput) {
        this.$refs.currentGame.onInput(command);
      }
    },
    handleKey(e) {
      const keyMap = {
        ArrowUp: "UP",
        w: "UP",
        ArrowDown: "DOWN",
        s: "DOWN",
        ArrowLeft: "LEFT",
        a: "LEFT",
        ArrowRight: "RIGHT",
        d: "RIGHT",
        Enter: "START",
        z: "A",
        x: "B",
      };
      if (keyMap[e.key]) {
        e.preventDefault(); // Stop page scrolling
        this.input(keyMap[e.key]);
      }
    },
  },
};
</script>

<style scoped>
/* RETRO STYLING */
.console-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 0;
}

.console-body {
  width: 320px;
  height: 540px;
  background: #c8c8c8; /* Classic Grey */
  border-radius: 15px 15px 40px 15px;
  box-shadow: inset -5px -5px 10px rgba(0, 0, 0, 0.1),
    10px 10px 30px rgba(0, 0, 0, 0.2);
  padding: 30px 20px;
  position: relative;
}

/* SCREEN AREA */
.screen-bezel {
  background: #555;
  border-radius: 10px 10px 30px 10px;
  padding: 30px 35px 10px 35px;
  box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.5);
  margin-bottom: 40px;
  position: relative;
}

.battery-light {
  width: 8px;
  height: 8px;
  background: red;
  border-radius: 50%;
  position: absolute;
  top: 100px; /* Adjust based on bezel size */
  left: 10px;
  box-shadow: 0 0 5px red;
  opacity: 0.8;
}

.lcd-screen {
  background: #8bac0f; /* Iconic Green-ish GameBoy color */
  width: 100%;
  aspect-ratio: 1/1;
  box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.6);
  overflow: hidden;
  position: relative;
  /* Pixel Art Look */
  image-rendering: pixelated;
}

/* CONTROLS AREA */
.brand {
  font-family: sans-serif;
  font-weight: 900;
  font-style: italic;
  color: #303080;
  margin-bottom: 20px;
  padding-left: 10px;
}
.brand span {
  color: #b01050;
}

.d-pad {
  width: 90px;
  height: 90px;
  position: absolute;
  left: 30px;
  bottom: 80px;
}

.d-btn {
  background: #222;
  border: none;
  position: absolute;
  width: 30px;
  height: 30px;
  cursor: pointer;
}
.d-btn:active {
  background: #444;
}

.up {
  top: 0;
  left: 30px;
  border-radius: 4px 4px 0 0;
}
.down {
  bottom: 0;
  left: 30px;
  border-radius: 0 0 4px 4px;
}
.left {
  top: 30px;
  left: 0;
  border-radius: 4px 0 0 4px;
}
.right {
  top: 30px;
  right: 0;
  border-radius: 0 4px 4px 0;
}
.d-center {
  width: 30px;
  height: 30px;
  background: #222;
  position: absolute;
  top: 30px;
  left: 30px;
}

.action-btns {
  position: absolute;
  right: 30px;
  bottom: 90px;
}
.btn-group {
  display: flex;
  gap: 15px;
  transform: rotate(-25deg);
}
.btn-round {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  border: none;
  background: #b01050; /* A/B Button Red */
  color: rgba(0, 0, 0, 0.3);
  font-weight: bold;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  cursor: pointer;
}
.btn-round:active {
  transform: scale(0.95);
  box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.5);
}
</style>
