<template>
  <div class="tetris-board">
    <!-- LEFT PANEL: SCORE & LEVEL -->
    <div class="side-panel left">
      <div class="panel-box">
        <label>SCORE</label>
        <span class="val">{{ score }}</span>
      </div>
      <div class="panel-box">
        <label>LEVEL</label>
        <span class="val">{{ level }}</span>
      </div>
      <div class="panel-box">
        <label>LINES</label>
        <span class="val">{{ lines }}</span>
      </div>
    </div>

    <!-- CENTER: THE GRID -->
    <div class="game-area">
      <div class="grid-container">
        <!-- 
           cell === 1: Locked Block
           cell === 2: Active Player Block
           cell === 3: Blinking Row (Animation)
        -->
        <div
          v-for="(cell, i) in flatGrid"
          :key="i"
          class="cell"
          :class="{
            filled: cell === 1,
            active: cell === 2,
            blinking: cell === 3,
          }"
        ></div>
      </div>
    </div>

    <!-- RIGHT COLUMN: NEXT PIECE -->
    <div class="side-panel right">
      <div class="panel-box next-box">
        <label>NEXT</label>
        <div class="mini-grid">
          <div v-for="(row, y) in nextPieceGrid" :key="y" class="mini-row">
            <div
              v-for="(c, x) in row"
              :key="x"
              class="mini-cell"
              :class="{ filled: c }"
            ></div>
          </div>
        </div>
      </div>
    </div>

    <!-- GAME OVER OVERLAY -->
    <div v-if="gameOver" class="game-over">
      GAME OVER
      <span class="blink">PRESS 'A'</span>
    </div>
  </div>
</template>

<script>
const SHAPES = [
  [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ], // I
  [
    [2, 0, 0],
    [2, 2, 2],
    [0, 0, 0],
  ], // J
  [
    [0, 0, 3],
    [3, 3, 3],
    [0, 0, 0],
  ], // L
  [
    [4, 4],
    [4, 4],
  ], // O
  [
    [0, 5, 5],
    [5, 5, 0],
    [0, 0, 0],
  ], // S
  [
    [0, 6, 0],
    [6, 6, 6],
    [0, 0, 0],
  ], // T
  [
    [7, 7, 0],
    [0, 7, 7],
    [0, 0, 0],
  ], // Z
];

export default {
  name: "TetrisGame",
  data() {
    return {
      arena: [],
      player: { pos: { x: 0, y: 0 }, matrix: null },
      nextPiece: null,
      gameOver: false,

      // Stats
      lines: 0,
      level: 1,
      score: 0,

      // Game Loop Vars
      dropCounter: 0,
      dropInterval: 1000,
      lastTime: 0,
      animationId: null,

      // Animation State
      isClearing: false, // Pauses gravity during animation
      clearingRows: [], // Stores Y-indices of rows currently blinking
    };
  },
  computed: {
    // Flatten logic for CSS Grid rendering
    flatGrid() {
      // 1. Clone Arena AND Handle Blinking Rows
      const display = this.arena.map((row, y) => {
        // If this row is currently clearing, replace it with '3's for styling
        if (this.clearingRows.includes(y)) {
          return new Array(10).fill(3);
        }
        return [...row];
      });

      // 2. Add Player (Only if NOT clearing/animating)
      if (this.player.matrix && !this.isClearing) {
        this.player.matrix.forEach((row, y) => {
          row.forEach((value, x) => {
            if (value !== 0) {
              const py = y + this.player.pos.y;
              const px = x + this.player.pos.x;
              if (py >= 0 && py < 20 && px >= 0 && px < 10) {
                display[py][px] = 2;
              }
            }
          });
        });
      }
      // 3. Flatten for single-loop rendering
      return display.flat();
    },
    nextPieceGrid() {
      if (!this.nextPiece)
        return [
          [0, 0, 0, 0],
          [0, 0, 0, 0],
        ];
      return this.nextPiece;
    },
  },
  mounted() {
    this.resetGame();
    this.update();
  },
  beforeUnmount() {
    cancelAnimationFrame(this.animationId);
  },
  methods: {
    onInput(cmd) {
      // Ignore inputs if Game Over OR if we are in the middle of a clear animation
      if (this.gameOver || this.isClearing) {
        if (this.gameOver && (cmd === "A" || cmd === "START")) this.resetGame();
        if (this.gameOver && cmd === "B") this.$emit("exitGame");
        return;
      }

      if (cmd === "LEFT") this.playerMove(-1);
      if (cmd === "RIGHT") this.playerMove(1);
      if (cmd === "DOWN") this.playerDrop();
      if (cmd === "UP") this.playerHardDrop();
      if (cmd === "A") this.playerRotate(1);
      if (cmd === "B") this.playerRotate(-1);
    },

    resetGame() {
      if (this.animationId) {
        cancelAnimationFrame(this.animationId);
        this.animationId = null;
      }

      this.arena = this.createMatrix(10, 20);
      this.lines = 0;
      this.level = 1;
      this.score = 0;
      this.gameOver = false;
      this.isClearing = false;
      this.clearingRows = [];

      this.nextPiece = this.getRandomPiece();
      this.playerReset();
      this.updateSpeed();
      this.lastTime = 0;

      this.update();
    },

    createMatrix(w, h) {
      const matrix = [];
      while (h--) matrix.push(new Array(w).fill(0));
      return matrix;
    },

    getRandomPiece() {
      return SHAPES[Math.floor(Math.random() * SHAPES.length)];
    },

    playerReset() {
      this.player.matrix = this.nextPiece;
      this.nextPiece = this.getRandomPiece();
      this.player.pos.y = 0;
      this.player.pos.x =
        ((this.arena[0].length / 2) | 0) -
        ((this.player.matrix[0].length / 2) | 0);

      // Game Over Check
      if (this.collide(this.arena, this.player)) {
        this.gameOver = true;
      }
    },

    playerHardDrop() {
      while (!this.collide(this.arena, this.player)) {
        this.player.pos.y++;
      }
      this.player.pos.y--;
      this.merge(this.arena, this.player);
      this.playerReset();
      this.arenaSweep();
      this.dropCounter = 0;
    },

    playerDrop() {
      this.player.pos.y++;
      if (this.collide(this.arena, this.player)) {
        this.player.pos.y--;
        this.merge(this.arena, this.player);
        this.playerReset();
        this.arenaSweep();
      }
      this.dropCounter = 0;
    },

    playerMove(dir) {
      this.player.pos.x += dir;
      if (this.collide(this.arena, this.player)) {
        this.player.pos.x -= dir;
      }
    },

    playerRotate(dir) {
      const pos = this.player.pos.x;
      let offset = 1;
      this.rotate(this.player.matrix, dir);
      while (this.collide(this.arena, this.player)) {
        this.player.pos.x += offset;
        offset = -(offset + (offset > 0 ? 1 : -1));
        if (offset > this.player.matrix[0].length) {
          this.rotate(this.player.matrix, -dir);
          this.player.pos.x = pos;
          return;
        }
      }
    },

    rotate(matrix, dir) {
      for (let y = 0; y < matrix.length; ++y) {
        for (let x = 0; x < y; ++x) {
          [matrix[x][y], matrix[y][x]] = [matrix[y][x], matrix[x][y]];
        }
      }
      if (dir > 0) matrix.forEach((row) => row.reverse());
      else matrix.reverse();
    },

    collide(arena, player) {
      const [m, o] = [player.matrix, player.pos];
      for (let y = 0; y < m.length; ++y) {
        for (let x = 0; x < m[y].length; ++x) {
          if (
            m[y][x] !== 0 &&
            (arena[y + o.y] && arena[y + o.y][x + o.x]) !== 0
          ) {
            return true;
          }
        }
      }
      return false;
    },

    merge(arena, player) {
      player.matrix.forEach((row, y) => {
        row.forEach((value, x) => {
          if (value !== 0) {
            arena[y + player.pos.y][x + player.pos.x] = 1;
          }
        });
      });
    },

    // --- NEW ANIMATION LOGIC ---
    arenaSweep() {
      // 1. Identify which rows are full
      const rowsToClear = [];
      this.arena.forEach((row, y) => {
        // If row has NO zeros, it is full
        if (row.every((value) => value !== 0)) {
          rowsToClear.push(y);
        }
      });

      // 2. If we found full rows, START THE PAUSE & ANIMATION
      if (rowsToClear.length > 0) {
        this.isClearing = true; // Pauses Update Loop
        this.clearingRows = rowsToClear; // Triggers 'blinking' CSS

        // 3. Wait 600ms (blinking time), then actually remove them
        setTimeout(() => {
          this.finalizeClear(rowsToClear.length);
        }, 600);
      }
    },

    finalizeClear(count) {
      // 1. Filter out the full rows (actual removal)
      const newArena = this.arena.filter((row) =>
        row.some((value) => value === 0)
      );

      // 2. Scoring
      const lineScores = [0, 40, 100, 300, 1200];
      this.score += lineScores[count] * this.level;

      // 3. Add new empty rows to top
      for (let i = 0; i < count; i++) {
        newArena.unshift(new Array(10).fill(0));
      }

      this.arena = newArena;
      this.lines += count;

      // 4. Level Up Logic
      const newLevel = Math.floor(this.lines / 10) + 1;
      if (newLevel > this.level) {
        this.level = newLevel;
        this.updateSpeed();
      }

      // 5. RESUME GAME
      this.clearingRows = [];
      this.isClearing = false;
      this.lastTime = performance.now(); // Reset timer so piece doesn't jump
    },

    updateSpeed() {
      const calculatedSpeed = 1000 - (this.level - 1) * 100;
      this.dropInterval = Math.max(100, calculatedSpeed);
    },

    update(time = 0) {
      if (this.gameOver) return;

      // ONLY process physics if we are NOT animating a clear
      if (!this.isClearing) {
        const deltaTime = time - this.lastTime;
        this.lastTime = time;
        this.dropCounter += deltaTime;
        if (this.dropCounter > this.dropInterval) {
          this.playerDrop();
        }
      }

      this.animationId = requestAnimationFrame(this.update);
    },
  },
};
</script>

<style scoped>
.tetris-board {
  height: 100%;
  display: flex;
  background: #9bbc0f;
  font-family: monospace;
  position: relative;
  overflow: hidden;
  padding: 5px;
  gap: 5px;
}

/* SIDE PANELS */
.side-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
}

.panel-box {
  border: 2px solid #0f380f;
  padding: 2px;
  text-align: center;
}
.panel-box label {
  display: block;
  font-size: 0.6rem;
  color: #0f380f;
  background: rgba(15, 56, 15, 0.1);
}
.val {
  font-size: 0.9rem;
  font-weight: bold;
  color: #0f380f;
}

/* THE CENTER GAME GRID */
.game-area {
  flex: 0 0 auto;
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.grid-container {
  width: 100%;
  aspect-ratio: 10 / 20;
  background: rgba(15, 56, 15, 0.05);
  border: 2px solid #0f380f;
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  grid-template-rows: repeat(20, 1fr);
}

.cell {
  border: 1px solid rgba(15, 56, 15, 0.1);
  box-sizing: border-box;
}

/* --- CELL STATES --- */
.cell.filled {
  background: #0f380f;
  border-color: #0f380f;
}

.cell.active {
  background: #0f380f;
  border: 2px solid #9bbc0f;
}

/* BLINK ANIMATION FOR CLEARED ROWS */
.cell.blinking {
  /* 1. Keep the block DARK so we can see it */
  background: #0f380f !important;
  border-color: #0f380f !important;

  /* 2. Slow it down: 0.2s per blink = 3 blinks in 600ms */
  animation: blink-animation 0.2s infinite;
}

/* 3. Hard toggle between Visible (Dark) and Invisible (Light Background) */
@keyframes blink-animation {
  0% {
    opacity: 1;
  }
  49% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
}

/* NEXT PIECE */
.mini-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 2px;
}
.mini-row {
  display: flex;
}
.mini-cell {
  width: 6px;
  height: 6px;
  background: transparent;
}
.mini-cell.filled {
  background: #0f380f;
}

/* GAME OVER */
.game-over {
  position: absolute;
  inset: 0;
  background: rgba(15, 56, 15, 0.9);
  color: #9bbc0f;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: bold;
  z-index: 20;
}
.blink {
  font-size: 0.8rem;
  animation: blink 1s infinite;
  margin-top: 5px;
}
@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
