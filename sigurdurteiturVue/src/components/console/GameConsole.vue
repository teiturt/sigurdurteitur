<template>
  <div class="console-wrapper">
    <div class="console-body">
      <!-- SCREEN SECTION -->
      <div class="screen-bezel">
        <div class="battery-light"></div>
        <div class="lcd-screen">
          <component
            :is="activeComponent"
            ref="currentGame"
            @launchGame="switchGame"
            @exitGame="switchGame('ConsoleMenu')"
          />
        </div>
      </div>

      <!-- CONTROLS SECTION -->
      <div class="controls-area">
        <div class="brand">TEITUR<span>BOY</span></div>

        <!-- D-PAD: Now supports Multi-Touch / Multi-Key -->
        <div class="d-pad">
          <!-- UP -->
          <button
            class="d-btn up"
            @touchstart.prevent="startInput('UP')"
            @touchend.prevent="stopInput('UP')"
            @mousedown.prevent="startInput('UP')"
            @mouseup.prevent="stopInput('UP')"
            @mouseleave.prevent="stopInput('UP')"
          ></button>

          <!-- LEFT -->
          <button
            class="d-btn left"
            @touchstart.prevent="startInput('LEFT')"
            @touchend.prevent="stopInput('LEFT')"
            @mousedown.prevent="startInput('LEFT')"
            @mouseup.prevent="stopInput('LEFT')"
            @mouseleave.prevent="stopInput('LEFT')"
          ></button>

          <!-- RIGHT -->
          <button
            class="d-btn right"
            @touchstart.prevent="startInput('RIGHT')"
            @touchend.prevent="stopInput('RIGHT')"
            @mousedown.prevent="startInput('RIGHT')"
            @mouseup.prevent="stopInput('RIGHT')"
            @mouseleave.prevent="stopInput('RIGHT')"
          ></button>

          <!-- DOWN -->
          <button
            class="d-btn down"
            @touchstart.prevent="startInput('DOWN')"
            @touchend.prevent="stopInput('DOWN')"
            @mousedown.prevent="startInput('DOWN')"
            @mouseup.prevent="stopInput('DOWN')"
            @mouseleave.prevent="stopInput('DOWN')"
          ></button>

          <div class="d-center"></div>
        </div>

        <!-- ACTION BUTTONS: Discrete clicks (No repeat needed for A/B usually) -->
        <div class="action-btns">
          <div class="btn-group">
            <button
              class="btn-round b-btn"
              @touchstart.prevent="triggerInput('B')"
              @mousedown.prevent="triggerInput('B')"
            >
              B
            </button>
            <button
              class="btn-round a-btn"
              @touchstart.prevent="triggerInput('A')"
              @mousedown.prevent="triggerInput('A')"
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
import TetrisGame from "./TetrisGame.vue";

export default {
  name: "GameConsole",
  components: { ConsoleMenu, SnakeGame, TetrisGame },
  data() {
    return {
      activeComponent: "ConsoleMenu",
      // Stores objects: { UP: { timeout: ID, interval: ID } }
      activeTimers: {},
    };
  },
  mounted() {
    window.addEventListener("keydown", this.handleKeyDown);
    window.addEventListener("keyup", this.handleKeyUp);
  },
  beforeUnmount() {
    window.removeEventListener("keydown", this.handleKeyDown);
    window.removeEventListener("keyup", this.handleKeyUp);
    // Cleanup all timers
    Object.keys(this.activeTimers).forEach((cmd) => this.stopInput(cmd));
  },
  methods: {
    switchGame(gameName) {
      this.activeComponent = gameName;
    },

    // FIRES ONCE (For A/B buttons)
    triggerInput(command) {
      if (this.$refs.currentGame && this.$refs.currentGame.onInput) {
        this.$refs.currentGame.onInput(command);
      }
    },

    // STARTS DELAYED LOOP (For D-Pad)
    startInput(command) {
      // If key is already held (prevent OS repeat), ignore
      if (this.activeTimers[command]) return;

      // 1. Fire the FIRST move immediately (The Tap)
      this.triggerInput(command);

      // 2. Init timer object
      this.activeTimers[command] = { timeout: null, interval: null };

      // 3. Wait 300ms (The "Delay") before starting the rapid fire
      this.activeTimers[command].timeout = setTimeout(() => {
        // 4. Start the rapid fire (The "Hold")
        this.activeTimers[command].interval = setInterval(() => {
          this.triggerInput(command);
        }, 100); // Repeat speed (100ms is fast/smooth)
      }, 300); // Initial delay (300ms is standard)
    },

    stopInput(command) {
      // Clear both the Timeout (wait) and the Interval (repeat)
      if (this.activeTimers[command]) {
        clearTimeout(this.activeTimers[command].timeout);
        clearInterval(this.activeTimers[command].interval);
        delete this.activeTimers[command];
      }
    },

    handleKeyDown(e) {
      if (e.repeat) return; // Ignore browser auto-repeat

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
        e: "A",
        " ": "A",
        q: "B",
      };

      const cmd = keyMap[e.key];
      if (cmd) {
        e.preventDefault();

        // D-PAD: Use the new "Delay + Repeat" logic
        if (["UP", "DOWN", "LEFT", "RIGHT"].includes(cmd)) {
          this.startInput(cmd);
        }
        // ACTIONS: Trigger Once (no hold needed usually)
        else {
          this.triggerInput(cmd);
        }
      }
    },

    handleKeyUp(e) {
      const keyMap = {
        ArrowUp: "UP",
        w: "UP",
        ArrowDown: "DOWN",
        s: "DOWN",
        ArrowLeft: "LEFT",
        a: "LEFT",
        ArrowRight: "RIGHT",
        d: "RIGHT",
      };

      const cmd = keyMap[e.key];
      if (cmd) {
        this.stopInput(cmd);
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
  top: 100px;
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

/* D-PAD BUTTONS */
.d-btn {
  background: #222;
  border: none;
  position: absolute;
  width: 30px;
  height: 30px;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}
.d-btn:active {
  background: #444;
}

/* Positioning */
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

/* ACTION BUTTONS */
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
  background: #b01050;
  color: rgba(0, 0, 0, 0.3);
  font-weight: bold;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}
.btn-round:active {
  transform: scale(0.95);
  box-shadow: inset 1px 1px 3px rgba(0, 0, 0, 0.5);
}
</style>
