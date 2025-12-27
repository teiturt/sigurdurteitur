<template>
  <div class="tetris-board">
    <!-- UI OVERLAY -->
    <div class="ui-header">
      <div class="score">LINES: {{ lines }}</div>
      <div class="next-piece">
        <div v-for="(row, y) in nextPieceGrid" :key="y" class="next-row">
          <div
            v-for="(cell, x) in row"
            :key="x"
            class="next-cell"
            :class="{ filled: cell }"
          ></div>
        </div>
      </div>
    </div>

    <!-- GAME OVER SCREEN -->
    <div v-if="gameOver" class="game-over">
      GAME OVER
      <span class="blink">PRESS 'A'</span>
    </div>

    <!-- THE GRID -->
    <div class="grid">
      <!-- We render the 20x10 board -->
      <div v-for="(row, y) in displayGrid" :key="y" class="row">
        <div
          v-for="(cell, x) in row"
          :key="x"
          class="cell"
          :class="{
            filled: cell === 1,
            active: cell === 2,
          }"
        ></div>
      </div>
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
      arena: [], // The fixed blocks on the floor
      player: { pos: { x: 0, y: 0 }, matrix: null },
      nextPiece: null,
      gameOver: false,
      lines: 0,
      dropCounter: 0,
      dropInterval: 1000,
      lastTime: 0,
      animationId: null,
    };
  },
  computed: {
    // Merges the static arena with the moving player for rendering
    displayGrid() {
      // Deep clone the arena
      const display = this.arena.map((row) => [...row]);

      // Draw player if valid
      if (this.player.matrix) {
        this.player.matrix.forEach((row, y) => {
          row.forEach((value, x) => {
            if (value !== 0) {
              const py = y + this.player.pos.y;
              const px = x + this.player.pos.x;
              if (py >= 0 && py < 20 && px >= 0 && px < 10) {
                display[py][px] = 2; // 2 = Active Piece Color
              }
            }
          });
        });
      }
      return display;
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
    /* --- INPUT HANDLER (Called by Console) --- */
    onInput(cmd) {
      if (this.gameOver) {
        if (cmd === "A" || cmd === "START") this.resetGame();
        if (cmd === "B") this.$emit("exitGame");
        return;
      }

      if (cmd === "LEFT") this.playerMove(-1);
      if (cmd === "RIGHT") this.playerMove(1);
      if (cmd === "DOWN") this.playerDrop();
      if (cmd === "A" || cmd === "UP") this.playerRotate(1);
      if (cmd === "B") this.playerRotate(-1);
    },

    /* --- GAME ENGINE --- */
    resetGame() {
      this.arena = this.createMatrix(10, 20);
      this.lines = 0;
      this.gameOver = false;
      this.nextPiece = this.getRandomPiece();
      this.playerReset();
      this.dropInterval = 1000;
      this.lastTime = 0;
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

      // Center the piece
      this.player.pos.y = 0;
      this.player.pos.x =
        ((this.arena[0].length / 2) | 0) -
        ((this.player.matrix[0].length / 2) | 0);

      // Immediate Game Over check
      if (this.collide(this.arena, this.player)) {
        this.gameOver = true;
      }
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

    playerDrop() {
      this.player.pos.y++;
      if (this.collide(this.arena, this.player)) {
        this.player.pos.y--; // Move back up
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

      // Wall Kick (prevent rotating into walls)
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

    merge(arena, player) {
      player.matrix.forEach((row, y) => {
        row.forEach((value, x) => {
          if (value !== 0) {
            arena[y + player.pos.y][x + player.pos.x] = 1; // 1 = Fixed block
          }
        });
      });
    },

    arenaSweep() {
      outer: for (let y = this.arena.length - 1; y > 0; --y) {
        for (let x = 0; x < this.arena[y].length; ++x) {
          if (this.arena[y][x] === 0) continue outer;
        }
        const row = this.arena.splice(y, 1)[0].fill(0);
        this.arena.unshift(row);
        ++y;
        this.lines++;
        // Speed up every 5 lines
        if (this.lines % 5 === 0) this.dropInterval *= 0.9;
      }
    },

    update(time = 0) {
      if (this.gameOver) return;
      const deltaTime = time - this.lastTime;
      this.lastTime = time;
      this.dropCounter += deltaTime;
      if (this.dropCounter > this.dropInterval) {
        this.playerDrop();
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
  flex-direction: column;
  background: #9bbc0f;
  font-family: monospace;
  position: relative;
}

.ui-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 5px 10px;
  border-bottom: 2px solid #0f380f;
  margin-bottom: 2px;
  height: 50px;
}

.score {
  font-weight: bold;
  color: #0f380f;
  margin-top: 10px;
}

.next-piece {
  display: flex;
  flex-direction: column;
}
.next-row {
  display: flex;
}
.next-cell {
  width: 8px;
  height: 8px;
  background: transparent;
}
.next-cell.filled {
  background: #0f380f;
  border: 1px solid #9bbc0f;
}

.grid {
  flex: 1;
  display: flex;
  flex-direction: column;
  border: 2px solid #0f380f;
  margin: 0 5px 5px 5px;
  background: rgba(15, 56, 15, 0.05);
}

.row {
  flex: 1;
  display: flex;
}

.cell {
  flex: 1;
  border: 1px solid rgba(15, 56, 15, 0.1);
}

.cell.filled {
  background: #0f380f; /* Locked blocks are solid dark */
  border-color: #0f380f;
}

.cell.active {
  background: #0f380f; /* Active piece */
  border: 2px solid #9bbc0f; /* Has a border to distinguish it */
}

.game-over {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 56, 15, 0.85);
  color: #9bbc0f;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  z-index: 10;
}
.blink {
  font-size: 0.8rem;
  animation: blink 1s infinite;
  margin-top: 10px;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
