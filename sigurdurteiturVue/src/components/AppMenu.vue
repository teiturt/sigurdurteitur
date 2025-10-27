<template>
  <div class="menu-container">
    <h2>Welcome to my Home Menu</h2>

    <button @click="logSampleAction">Log 'Created Something'</button>

    <!-- This is the drawing area -->
    <div class="drawing-area">
      <canvas
        ref="drawingCanvas"
        @touchstart="startDrawing"
        @touchmove="draw"
        @touchend="stopDrawing"
        @touchcancel="stopDrawing"
      ></canvas>
    </div>

    <button @click="$emit('goBack')">Go Back Home</button>
  </div>
</template>

<script>
export default {
  name: "AppMenu",
  emits: ["goBack", "logAction"],
  data() {
    return {
      isDrawing: false,
      context: null,
    };
  },
  // 'mounted' is a special function that runs after the component is created
  // and added to the page. It's the perfect place to set up the canvas.
  mounted() {
    const canvas = this.$refs.drawingCanvas;
    this.context = canvas.getContext("2d");

    // Set a fixed size for the canvas for this test
    canvas.width = 300;
    canvas.height = 300;

    // Configure the drawing style
    this.context.lineWidth = 4;
    this.context.lineCap = "round";
    this.context.strokeStyle = "#000000";
  },
  methods: {
    logSampleAction() {
      const sampleAction = {
        category: "Focus and creation",
        action: "Created something",
        points: 2,
        note: "Logged from the web app!"
      };
      // Send the 'logAction' event and the data up to the parent component (App.vue)
      this.$emit('logAction', sampleAction);
    },
    // Helper function to get the correct touch coordinates relative to the canvas
    getTouchPosition(event) {
      const canvas = this.$refs.drawingCanvas;
      const rect = canvas.getBoundingClientRect();
      const touch = event.touches[0]; // We only care about the first finger touch

      return {
        x: touch.clientX - rect.left,
        y: touch.clientY - rect.top,
      };
    },
    // Called when you first touch the screen
    startDrawing(event) {
      // This is important to prevent the whole page from scrolling while you draw
      event.preventDefault();

      this.isDrawing = true;
      const { x, y } = this.getTouchPosition(event);
      this.context.beginPath();
      this.context.moveTo(x, y);
    },
    // Called when you move your finger while touching the screen
    draw(event) {
      event.preventDefault();
      if (!this.isDrawing) return; // Only draw if the finger is down

      const { x, y } = this.getTouchPosition(event);
      this.context.lineTo(x, y);
      this.context.stroke(); // This command actually draws the line
    },
    // Called when you lift your finger off the screen
    stopDrawing(event) {
      event.preventDefault();
      if (!this.isDrawing) return;

      this.isDrawing = false;
      this.context.closePath();
    },
  },
};
</script>

<style scoped>
.menu-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
  text-align: center;
  z-index: 5;
  background: transparent;
  padding: 20px;
  display: flex; /* Use flexbox to easily arrange items vertically */
  flex-direction: column;
  align-items: center;
  gap: 20px; /* Adds space between the title, canvas, and button */
}

/* This is the new style for our drawing box */
.drawing-area {
  border: 2px solid #333;
  border-radius: 8px;
  /* This is critical: it tells the browser not to handle scrolling or zooming
     when you touch inside this box, giving our code full control. */
  touch-action: none;
}
</style>