<template>
  <div class="menu-container">
    <h2>Calculation Canvas</h2>

    <div class="drawing-area">
      <canvas
        ref="drawingCanvas"
        @touchstart="handleTouchStart"
        @touchmove="handleTouchMove"
        @touchend="handleTouchEnd"
        @touchcancel="handleTouchEnd"
      ></canvas>
    </div>

    <button @click="clearCanvas">Clear Drawing</button>
    <button @click="$emit('goBack')">Go Back Home</button>
  </div>
</template>

<script>
export default {
  name: "AppMenu",
  emits: ["goBack"],
  data() {
    return {
      context: null,
      // --- State for Drawing ---
      isDrawing: false,
      // This will store all the lines we've drawn
      strokes: [],
      // This will hold the points of the line we are currently drawing
      currentStroke: [],

      // --- State for Gestures (Pan & Zoom) ---
      isGesturing: false,
      // Stores the state of the two fingers at the start of a gesture
      initialGestureState: null,
      // The current pan and zoom of our "camera"
      transform: {
        offsetX: 0,
        offsetY: 0,
        scale: 1,
      },
    };
  },
  mounted() {
    const canvas = this.$refs.drawingCanvas;
    this.context = canvas.getContext("2d");

    // Set the canvas to fill its container
    this.resizeCanvas();
    window.addEventListener("resize", this.resizeCanvas);
  },
  methods: {
    // --- Setup and Drawing ---
    resizeCanvas() {
      const canvas = this.$refs.drawingCanvas;
      const container = canvas.parentElement;
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
      this.drawCanvas(); // Redraw everything after resizing
    },
    // This is our main rendering function. It draws everything from scratch.
    drawCanvas() {
      if (!this.context) return;
      const canvas = this.$refs.drawingCanvas;
      const ctx = this.context;

      // Clear the entire visible canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Save the default state (no pan/zoom)
      ctx.save();

      // Apply our current "camera" transformation
      ctx.translate(this.transform.offsetX, this.transform.offsetY);
      ctx.scale(this.transform.scale, this.transform.scale);

      // --- Draw all the completed strokes ---
      ctx.lineWidth = 4 / this.transform.scale; // Keep line width consistent when zooming
      ctx.lineCap = "round";
      ctx.strokeStyle = "#000000";

      this.strokes.forEach(stroke => {
        if (stroke.length < 2) return;
        ctx.beginPath();
        ctx.moveTo(stroke[0].x, stroke[0].y);
        for (let i = 1; i < stroke.length; i++) {
          ctx.lineTo(stroke[i].x, stroke[i].y);
        }
        ctx.stroke();
      });

      // Restore the canvas to its default state
      ctx.restore();
    },
    clearCanvas() {
      this.strokes = [];
      this.drawCanvas();
    },

    // --- Coordinate Translation ---
    // Converts screen touch coordinates to our "infinite world" coordinates
    screenToWorld(screenPos) {
      return {
        x: (screenPos.x - this.transform.offsetX) / this.transform.scale,
        y: (screenPos.y - this.transform.offsetY) / this.transform.scale,
      };
    },
    
    // --- Touch Event Handlers ---
    handleTouchStart(event) {
      event.preventDefault();
      const touches = event.touches;

      if (touches.length === 1) { // --- START DRAWING ---
        this.isDrawing = true;
        const pos = this.screenToWorld({ x: touches[0].clientX, y: touches[0].clientY });
        this.currentStroke = [pos];
        // We add the new stroke to the main array immediately to make drawing reactive
        this.strokes.push(this.currentStroke);

      } else if (touches.length === 2) { // --- START GESTURE ---
        this.isDrawing = false; // Stop drawing if a second finger is added
        this.isGesturing = true;
        this.initialGestureState = {
          distance: Math.hypot(touches[0].clientX - touches[1].clientX, touches[0].clientY - touches[1].clientY),
          midpoint: {
            x: (touches[0].clientX + touches[1].clientX) / 2,
            y: (touches[0].clientY + touches[1].clientY) / 2,
          },
          // Save the transform state at the beginning of the gesture
          transform: { ...this.transform }
        };
      }
    },
    handleTouchMove(event) {
      event.preventDefault();
      const touches = event.touches;

      if (this.isDrawing && touches.length === 1) { // --- DRAWING ---
        const pos = this.screenToWorld({ x: touches[0].clientX, y: touches[0].clientY });
        this.currentStroke.push(pos);
        this.drawCanvas(); // Redraw to show the line in real-time

      } else if (this.isGesturing && touches.length === 2) { // --- PANNING & ZOOMING ---
        const newDistance = Math.hypot(touches[0].clientX - touches[1].clientX, touches[0].clientY - touches[1].clientY);
        const newMidpoint = {
          x: (touches[0].clientX + touches[1].clientX) / 2,
          y: (touches[0].clientY + touches[1].clientY) / 2,
        };

        // Calculate new scale
        const initial = this.initialGestureState;
        this.transform.scale = initial.transform.scale * (newDistance / initial.distance);

        // Calculate new offset (pan)
        this.transform.offsetX = initial.transform.offsetX + (newMidpoint.x - initial.midpoint.x);
        this.transform.offsetY = initial.transform.offsetY + (newMidpoint.y - initial.midpoint.y);

        this.drawCanvas();
      }
    },
    handleTouchEnd(event) {
      event.preventDefault();
      this.isDrawing = false;
      this.isGesturing = false;
      this.initialGestureState = null;
      this.currentStroke = [];
    },
  },
};
</script>

<style scoped>
.menu-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
  height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}

.drawing-area {
  width: 100%;
  flex-grow: 1; /* This makes the canvas container fill the available space */
  border: 2px solid #333;
  border-radius: 8px;
  touch-action: none; /* Absolutely critical for custom gestures */
  overflow: hidden; /* Hides anything drawn outside the bounds */
}

canvas {
  display: block; /* Removes any weird spacing issues */
}
</style>