<template>
  <div class="game-container" @mousemove="updateMouse" @mousedown="shoot">
    <!-- HUD / Cockpit Overlay -->
    <div class="cockpit-hud">
      <div class="hud-top">
        <div class="stat">SCORE: {{ score }}</div>
        <div class="stat">SPEED: {{ Math.round(velocity * 10) }} km/s</div>
      </div>
      
      <!-- Crosshair that follows mouse slightly -->
      <div class="crosshair" :style="crosshairStyle">
        <div class="aim-dot"></div>
      </div>

      <!-- Glass/Frame Effect -->
      <div class="cockpit-frame"></div>
      
      <div class="hud-bottom">
        <div class="hint">MOUSE: AIM | SPACE: SHOOT | W/S: ACCEL</div>
        <button class="exit-btn" @click="$emit('goBack')">ABORT MISSION</button>
      </div>
    </div>

    <canvas ref="gameCanvas" class="game-canvas"></canvas>
  </div>
</template>

<script>
export default {
  name: "AppMenu",
  emits: ["goBack"],
  data() {
    return {
      score: 0,
      canvas: null,
      ctx: null,
      animationId: null,
      
      // Physics - Slower, more controlled
      velocity: 8,
      targetVelocity: 8,
      rotation: { x: 0, y: 0 }, // View offset based on mouse
      mouse: { x: 0, y: 0 },
      
      // Game Objects
      stars: [],
      hoops: [],
      lasers: [], // Projectiles
      
      keys: { w: false, s: false },
      
      // Config
      starCount: 200,
      perspective: 400,
    };
  },
  computed: {
    crosshairStyle() {
      // Crosshair follows mouse with a bit of "weight"
      return {
        transform: `translate(${this.mouse.x}px, ${this.mouse.y}px)`
      };
    }
  },
  mounted() {
    this.initGame();
    window.addEventListener("keydown", this.handleKey);
    window.addEventListener("keyup", this.handleKey);
    this.animationId = requestAnimationFrame(this.gameLoop);
  },
  beforeUnmount() {
    cancelAnimationFrame(this.animationId);
    window.removeEventListener("keydown", this.handleKey);
    window.removeEventListener("keyup", this.handleKey);
  },
  methods: {
    initGame() {
      this.canvas = this.$refs.gameCanvas;
      this.ctx = this.canvas.getContext("2d");
      this.resize();
      window.addEventListener("resize", this.resize);

      for (let i = 0; i < this.starCount; i++) this.stars.push(this.createStar(true));
    },
    resize() {
      this.canvas.width = window.innerWidth;
      this.canvas.height = window.innerHeight;
    },
    createStar(randomZ = false) {
      return {
        x: (Math.random() - 0.5) * 3000,
        y: (Math.random() - 0.5) * 3000,
        z: randomZ ? Math.random() * 2000 : 2000,
        size: Math.random() * 1.5
      };
    },
    createHoop() {
      return {
        x: (Math.random() - 0.5) * 1000,
        y: (Math.random() - 0.5) * 1000,
        z: 2500,
        radius: 80,
        passed: false,
        hit: false
      };
    },
    updateMouse(e) {
      // Calculate mouse offset from center
      this.mouse.x = e.clientX - window.innerWidth / 2;
      this.mouse.y = e.clientY - window.innerHeight / 2;
    },
    handleKey(e) {
      const state = e.type === "keydown";
      if (e.key.toLowerCase() === 'w') this.keys.w = state;
      if (e.key.toLowerCase() === 's') this.keys.s = state;
      if (e.code === 'Space' && state) this.shoot();
    },
    shoot() {
      // Shoot from slightly left and right of center (dual cannons)
      const laserX = this.mouse.x * 0.2; // Laser origin
      const laserY = this.mouse.y * 0.2;
      this.lasers.push({
        x: laserX,
        y: laserY,
        z: 50,
        vx: this.mouse.x * 0.05, // Laser moves toward crosshair
        vy: this.mouse.y * 0.05,
        vz: 100 // High speed forward
      });
    },
    update() {
      // 1. Velocity Control (Slow transitions)
      if (this.keys.w) this.targetVelocity = 35;
      else if (this.keys.s) this.targetVelocity = 4;
      else this.targetVelocity = 12;
      
      this.velocity += (this.targetVelocity - this.velocity) * 0.05;

      // 2. Rotation / Tilting (Mouse movement affects universe)
      // We divide mouse by 100 to make it subtle
      this.rotation.x += (-this.mouse.x * 0.0005 - this.rotation.x) * 0.1;
      this.rotation.y += (-this.mouse.y * 0.0005 - this.rotation.y) * 0.1;

      // 3. Update Stars
      this.stars.forEach(s => {
        s.z -= this.velocity;
        // Apply rotation "drift"
        s.x += this.rotation.x * s.z * 0.1;
        s.y += this.rotation.y * s.z * 0.1;

        if (s.z <= 0) Object.assign(s, this.createStar(false));
      });

      // 4. Update Hoops
      if (this.hoops.length < 4 && Math.random() < 0.01) this.hoops.push(this.createHoop());
      this.hoops.forEach((h, i) => {
        h.z -= this.velocity;
        h.x += this.rotation.x * h.z * 0.1;
        h.y += this.rotation.y * h.z * 0.1;

        // Check if flying through
        if (h.z < 50 && h.z > -50 && !h.passed) {
          const dist = Math.sqrt(h.x * h.x + h.y * h.y);
          if (dist < h.radius) {
            this.score += 50;
            h.passed = true;
          }
        }
        if (h.z < -200) this.hoops.splice(i, 1);
      });

      // 5. Update Lasers
      this.lasers.forEach((l, i) => {
        l.x += l.vx;
        l.y += l.vy;
        l.z += l.vz;
        
        // Collision with hoops
        this.hoops.forEach(h => {
           const dx = l.x - h.x;
           const dy = l.y - h.y;
           const dz = l.z - h.z;
           const dist = Math.sqrt(dx*dx + dy*dy + dz*dz);
           if (dist < h.radius && !h.hit) {
             h.hit = true;
             this.score += 10;
           }
        });

        if (l.z > 3000) this.lasers.splice(i, 1);
      });
    },
    draw() {
      const { ctx, canvas, perspective } = this;
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      ctx.fillStyle = "#020408";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Stars
      ctx.fillStyle = "white";
      this.stars.forEach(s => {
        const scale = perspective / (perspective + s.z);
        const px = s.x * scale + cx;
        const py = s.y * scale + cy;
        ctx.beginPath();
        ctx.arc(px, py, s.size * scale * 3, 0, Math.PI * 2);
        ctx.fill();
      });

      // Hoops
      this.hoops.forEach(h => {
        const scale = perspective / (perspective + h.z);
        const px = h.x * scale + cx;
        const py = h.y * scale + cy;
        const r = h.radius * scale;

        if (h.z > 0) {
          ctx.strokeStyle = h.hit ? "red" : (h.passed ? "lime" : "cyan");
          ctx.lineWidth = 4 * scale;
          ctx.beginPath();
          ctx.arc(px, py, r, 0, Math.PI * 2);
          ctx.stroke();
          
          // Outer ring
          ctx.beginPath();
          ctx.arc(px, py, r + 10 * scale, 0, Math.PI * 2);
          ctx.setLineDash([5, 10]);
          ctx.stroke();
          ctx.setLineDash([]);
        }
      });

      // Lasers
      ctx.strokeStyle = "red";
      ctx.lineWidth = 2;
      this.lasers.forEach(l => {
        const scale = perspective / (perspective + l.z);
        const px = l.x * scale + cx;
        const py = l.y * scale + cy;
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(px, py - 10 * scale);
        ctx.stroke();
      });
    },
    gameLoop() {
      this.update();
      this.draw();
      this.animationId = requestAnimationFrame(this.gameLoop);
    }
  }
};
</script>

<style scoped>
.game-container {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background: black;
  overflow: hidden;
  cursor: none; /* Hide cursor for immersion */
}

.game-canvas { display: block; }

/* Cockpit HUD */
.cockpit-hud {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 40px;
  pointer-events: none;
  z-index: 10;
  font-family: 'Orbitron', 'Courier New', monospace;
  color: #00f2ff;
}

.hud-top { display: flex; justify-content: space-between; font-size: 1.5rem; text-shadow: 0 0 10px #00f2ff; }

/* 1st Person Cockpit Frame */
.cockpit-frame {
  position: absolute;
  inset: 0;
  border: 40px solid #111;
  border-image: linear-gradient(to bottom, #222, #000) 1;
  pointer-events: none;
  mask-image: radial-gradient(circle at center, transparent 40%, black 100%);
  background: radial-gradient(circle at center, transparent 50%, rgba(0,0,0,0.4) 100%);
}

.crosshair {
  position: absolute;
  top: 50%; left: 50%;
  width: 60px; height: 60px;
  border: 1px solid rgba(0, 242, 255, 0.5);
  border-radius: 50%;
  margin: -30px 0 0 -30px;
  transition: transform 0.05s linear;
}

.aim-dot {
  position: absolute;
  top: 50%; left: 50%;
  width: 4px; height: 4px;
  background: red;
  border-radius: 50%;
  margin: -2px 0 0 -2px;
  box-shadow: 0 0 10px red;
}

.hud-bottom { display: flex; justify-content: space-between; align-items: flex-end; }
.hint { font-size: 0.8rem; opacity: 0.6; }

.exit-btn {
  background: transparent;
  color: #ff3c00;
  border: 1px solid #ff3c00;
  padding: 8px 16px;
  cursor: pointer;
  pointer-events: auto;
  font-size: 0.7rem;
  transition: all 0.3s;
}
.exit-btn:hover { background: #ff3c00; color: white; }
</style>