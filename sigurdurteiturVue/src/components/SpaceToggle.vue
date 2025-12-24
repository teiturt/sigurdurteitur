<template>
  <div
    class="star-container"
    @mousedown="handleDragStart"
    @mousemove="handleDragMove"
    @mouseup="handleDragEnd"
    @mouseleave="handleDragEnd"
  >
    <canvas ref="starCanvas" class="star-canvas"></canvas>
  </div>
</template>

<script>
export default {
  name: "SpaceToggle",
  props: {
    // Allows the home page to speed up the stars if it wants
    speed: { type: Number, default: 2 },
  },
  data() {
    return {
      canvas: null,
      ctx: null,
      stars: [],
      velocity: 2,
      angle: 0,
      dragging: false,
      lastX: 0,
      animationId: null,
    };
  },
  mounted() {
    this.initCanvas();
    this.animate();
    window.addEventListener("resize", this.resize);
  },
  beforeUnmount() {
    cancelAnimationFrame(this.animationId);
    window.removeEventListener("resize", this.resize);
  },
  watch: {
    speed(newVal) {
      this.velocity = newVal;
    },
  },
  methods: {
    initCanvas() {
      this.canvas = this.$refs.starCanvas;
      this.ctx = this.canvas.getContext("2d");
      this.resize();
      for (let i = 0; i < 400; i++) this.stars.push(this.createStar(true));
    },
    resize() {
      if (!this.canvas) return;
      this.canvas.width = window.innerWidth;
      this.canvas.height = window.innerHeight;
    },
    createStar(randomZ = false) {
      return {
        x: (Math.random() - 0.5) * 3000,
        y: (Math.random() - 0.5) * 3000,
        z: randomZ ? Math.random() * 2000 : 2000,
        size: Math.random() * 2,
      };
    },
    animate() {
      const { ctx, canvas, stars } = this;
      if (!ctx) return;

      ctx.fillStyle = "black";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const perspective = 500;

      ctx.fillStyle = "white";
      stars.forEach((s) => {
        s.z -= this.velocity;

        const rotatedX =
          s.x * Math.cos(this.angle) - s.y * Math.sin(this.angle);
        const rotatedY =
          s.x * Math.sin(this.angle) + s.y * Math.cos(this.angle);

        const scale = perspective / (perspective + s.z);
        const px = rotatedX * scale + cx;
        const py = rotatedY * scale + cy;

        if (s.z <= 0) Object.assign(s, this.createStar(false));

        ctx.beginPath();
        ctx.arc(px, py, s.size * scale * 2, 0, Math.PI * 2);
        ctx.fill();
      });

      this.animationId = requestAnimationFrame(this.animate);
    },
    handleDragStart(e) {
      this.dragging = true;
      this.lastX = e.clientX;
    },
    handleDragMove(e) {
      if (!this.dragging) return;
      const dx = e.clientX - this.lastX;
      this.angle += dx * 0.003;
      this.lastX = e.clientX;
    },
    handleDragEnd() {
      this.dragging = false;
    },
  },
};
</script>

<style scoped>
.star-container {
  width: 100%;
  height: 100%;
  background: black;
  cursor: grab;
}
.star-container:active {
  cursor: grabbing;
}
.star-canvas {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
