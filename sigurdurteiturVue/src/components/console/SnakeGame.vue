<template>
  <div class="snake-board">
    <div class="score">SCORE: {{ score }}</div>
    <div v-if="gameOver" class="game-over">
      GAME OVER
      <span>PRESS 'A'</span>
    </div>

    <!-- Render the Grid -->
    <div class="grid" :style="gridStyle">
      <div
        v-for="(cell, i) in grid"
        :key="i"
        class="cell"
        :class="{
          snake: isSnake(i),
          food: isFood(i),
        }"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      width: 15, // Grid width
      snake: [10, 9, 8], // Snake body positions (indices)
      food: 50,
      direction: 1, // 1=Right, -1=Left, 15=Down, -15=Up
      interval: null,
      gameOver: false,
      score: 0,
    };
  },
  computed: {
    grid() {
      return new Array(this.width * this.width).fill(0);
    },
    gridStyle() {
      return {
        display: "grid",
        gridTemplateColumns: `repeat(${this.width}, 1fr)`,
        gridTemplateRows: `repeat(${this.width}, 1fr)`,
      };
    },
  },
  mounted() {
    this.startGame();
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
  methods: {
    startGame() {
      this.snake = [20, 19, 18];
      this.direction = 1;
      this.score = 0;
      this.gameOver = false;
      this.spawnFood();
      this.interval = setInterval(this.tick, 150);
    },
    onInput(cmd) {
      if (this.gameOver && cmd === "A") return this.startGame();
      if (this.gameOver && cmd === "B") return this.$emit("exitGame");

      const W = this.width;
      // Prevent reversing directly
      if (cmd === "UP" && this.direction !== W) this.direction = -W;
      if (cmd === "DOWN" && this.direction !== -W) this.direction = W;
      if (cmd === "LEFT" && this.direction !== 1) this.direction = -1;
      if (cmd === "RIGHT" && this.direction !== -1) this.direction = 1;
    },
    tick() {
      const head = this.snake[0] + this.direction;
      const W = this.width;

      // Collision Detection (Walls & Self)
      const hitWall =
        (this.direction === 1 && head % W === 0) || // Hit Right
        (this.direction === -1 && (head + 1) % W === 0) || // Hit Left
        head < 0 ||
        head >= W * W; // Hit Top/Bottom

      const hitSelf = this.snake.includes(head);

      if (hitWall || hitSelf) {
        this.gameOver = true;
        clearInterval(this.interval);
        return;
      }

      this.snake.unshift(head); // Move head forward

      if (head === this.food) {
        this.score++;
        this.spawnFood();
      } else {
        this.snake.pop(); // Remove tail
      }
    },
    spawnFood() {
      let newFood;
      do {
        newFood = Math.floor(Math.random() * (this.width * this.width));
      } while (this.snake.includes(newFood));
      this.food = newFood;
    },
    isSnake(i) {
      return this.snake.includes(i);
    },
    isFood(i) {
      return this.food === i;
    },
  },
};
</script>

<style scoped>
.snake-board {
  height: 100%;
  display: flex;
  flex-direction: column;
  color: #0f380f;
}
.score {
  text-align: right;
  font-family: monospace;
  font-weight: bold;
  margin-bottom: 5px;
}
.grid {
  flex: 1;
  border: 2px solid #0f380f;
  background: #9bbc0f;
}
.cell {
  border: 1px solid rgba(15, 56, 15, 0.05);
}
.cell.snake {
  background: #0f380f;
  border-color: #0f380f;
}
.cell.food {
  background: #0f380f;
  border-radius: 50%;
}

.game-over {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 56, 15, 0.8);
  color: #9bbc0f;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: monospace;
  font-size: 1.5rem;
  font-weight: bold;
}
.game-over span {
  font-size: 0.8rem;
  margin-top: 10px;
}
</style>
