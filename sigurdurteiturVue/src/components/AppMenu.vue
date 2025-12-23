<template>
  <div class="game-container" @mousemove="updateMouse" @mousedown="handleMouseDown">
    
    <!-- START MENU -->
    <div v-if="gameState === 'menu'" class="overlay">
      <div class="menu-box">
        <h1 class="glitch">VOID PILOT</h1>
        <div class="instructions">
          <p><strong>W / S:</strong> Warpspeed / Brake</p>
          <p><strong>SPACE / CLICK:</strong> Fire Lasers</p>
          <hr />
          <p>• Fly through <span>CYAN HOOPS</span> for Fuel.</p>
          <p>• Shoot <span>PURPLE TARGETS</span> for Energy.</p>
        </div>
        <button class="primary-btn" @click="startGame">START MISSION</button>
        <button class="secondary-btn" @click="$emit('goBack')">EXIT</button>
      </div>
    </div>

    <!-- PAUSE MENU -->
    <div v-if="gameState === 'paused'" class="overlay">
      <div class="menu-box">
        <h1>PAUSED</h1>
        <button class="primary-btn" @click="gameState = 'playing'">RESUME</button>
        <button class="secondary-btn" @click="startGame">RESTART</button>
      </div>
    </div>

    <!-- GAME OVER -->
    <div v-if="gameState === 'gameover'" class="overlay">
      <div class="menu-box">
        <h1 class="dead">MISSION FAILED</h1>
        <p class="final-score">SCORE: {{ score }}</p>
        <p class="cause">{{ deathReason }}</p>
        <button class="primary-btn" @click="startGame">RETRY</button>
        <button class="secondary-btn" @click="$emit('goBack')">EXIT</button>
      </div>
    </div>

    <!-- HUD -->
    <div class="cockpit-hud" v-if="gameState !== 'menu'">
      <div class="hud-top">
        <div class="stat">SCORE: {{ score }}</div>
        <div class="stat">SPEED: {{ Math.round(velocity * 10) }} km/s</div>
      </div>
      
      <div class="resource-bars">
        <div class="bar-container">
          <label>ENERGY</label>
          <div class="bar-bg">
            <div class="bar-fill energy" :class="{ flash: energyFlash }" :style="{width: energy + '%'}"></div>
          </div>
        </div>
        <div class="bar-container">
          <label>FUEL</label>
          <div class="bar-bg">
            <div class="bar-fill fuel" :class="{ flash: fuelFlash }" :style="{width: fuel + '%'}"></div>
          </div>
        </div>
      </div>

      <div class="crosshair" :style="crosshairStyle">
        <div class="aim-dot"></div>
      </div>

      <div class="cockpit-frame"></div>
      
      <div class="hud-bottom">
        <div class="hint">ESC: PAUSE | W: GO FAST (EFFICIENT)</div>
        <button class="exit-btn" @click="$emit('goBack')">ABORT</button>
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
      gameState: 'menu',
      deathReason: '',
      score: 0,
      energy: 100,
      fuel: 100,
      energyFlash: false,
      fuelFlash: false,
      
      canvas: null,
      ctx: null,
      animationId: null,
      
      velocity: 8,
      targetVelocity: 8,
      rotation: { x: 0, y: 0 },
      mouse: { x: 0, y: 0 },
      
      stars: [],
      targets: [],
      lasers: [],
      keys: { w: false, s: false },
      
      perspective: 400,
      lastTime: 0
    };
  },
  computed: {
    crosshairStyle() {
      return { transform: `translate(${this.mouse.x}px, ${this.mouse.y}px)` };
    }
  },
  mounted() {
    this.initCanvas();
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
    initCanvas() {
      this.canvas = this.$refs.gameCanvas;
      this.ctx = this.canvas.getContext("2d");
      this.resize();
      window.addEventListener("resize", this.resize);
      for (let i = 0; i < 200; i++) this.stars.push(this.createStar(true));
    },
    startGame() {
      this.score = 0;
      this.energy = 100;
      this.fuel = 100;
      this.velocity = 8;
      this.targets = [];
      this.lasers = [];
      this.gameState = 'playing';
    },
    resize() {
      this.canvas.width = window.innerWidth;
      this.canvas.height = window.innerHeight;
    },
    createStar(randomZ = false) {
      return {
        x: (Math.random() - 0.5) * 4000,
        y: (Math.random() - 0.5) * 4000,
        z: randomZ ? Math.random() * 2000 : 2000,
        size: Math.random() * 1.5
      };
    },
    createTarget() {
      const isInterceptor = Math.random() > 0.6; 
      return {
        type: isInterceptor ? 'interceptor' : 'hoop',
        x: (Math.random() - 0.5) * 1400,
        y: (Math.random() - 0.5) * 1400,
        z: 2500,
        radius: isInterceptor ? 50 : 90,
        vx: isInterceptor ? (Math.random() - 0.5) * 15 : 0, 
        passed: false,
        hit: false
      };
    },
    triggerFlash(type) {
      if (type === 'fuel') {
        this.fuelFlash = true;
        setTimeout(() => this.fuelFlash = false, 200);
      } else {
        this.energyFlash = true;
        setTimeout(() => this.energyFlash = false, 200);
      }
    },
    updateMouse(e) {
      this.mouse.x = e.clientX - window.innerWidth / 2;
      this.mouse.y = e.clientY - window.innerHeight / 2;
    },
    handleMouseDown() {
      if (this.gameState === 'playing') this.shoot();
    },
    handleKey(e) {
      const state = e.type === "keydown";
      if (e.key === "Escape" && state) {
        if (this.gameState === 'playing') this.gameState = 'paused';
        else if (this.gameState === 'paused') this.gameState = 'playing';
        return;
      }
      const key = e.key.toLowerCase();
      if (key === 'w') this.keys.w = state;
      if (key === 's') this.keys.s = state;
      if (e.code === 'Space' && state && this.gameState === 'playing') this.shoot();
    },
    shoot() {
      if (this.energy < 2) return;
      this.energy -= 2;

      const laserX = this.mouse.x * 0.2;
      const laserY = this.mouse.y * 0.2;
      this.lasers.push({
        x: laserX, y: laserY, z: 50,
        vx: this.mouse.x * 0.055,
        vy: this.mouse.y * 0.055,
        vz: 140
      });
    },
    update() {
      if (this.gameState !== 'playing') return;

      // 1. RESOURCE DRAIN
      // fuelEfficiency ranges from ~0.1 (slow) to ~1.0 (fast)
      const fuelEfficiency = this.velocity / 40; 
      
      // High penalty for going slow, high reward for warp speed
      const baseDrain = 0.05; 
      this.fuel -= baseDrain * (1.1 - fuelEfficiency);
      
      // Energy constant drain
      this.energy -= 0.015;

      if (this.fuel <= 0) { 
        this.gameState = 'gameover'; 
        this.deathReason = 'OUT OF FUEL - ENGINE STALLED'; 
      }
      if (this.energy <= 0) { 
        this.gameState = 'gameover'; 
        this.deathReason = 'SYSTEM POWER DEPLETED'; 
      }

      // 2. VELOCITY
      if (this.keys.w) this.targetVelocity = 40;
      else if (this.keys.s) this.targetVelocity = 5;
      else this.targetVelocity = 15;
      this.velocity += (this.targetVelocity - this.velocity) * 0.04;

      // 3. ROTATION
      this.rotation.x += (-this.mouse.x * 0.0005 - this.rotation.x) * 0.1;
      this.rotation.y += (-this.mouse.y * 0.0005 - this.rotation.y) * 0.1;

      // 4. STARS
      this.stars.forEach(s => {
        s.z -= this.velocity;
        s.x += this.rotation.x * s.z * 0.12;
        s.y += this.rotation.y * s.z * 0.12;
        if (s.z <= 0) Object.assign(s, this.createStar(false));
      });

      // 5. TARGETS
      if (this.targets.length < 6 && Math.random() < 0.03) this.targets.push(this.createTarget());
      this.targets.forEach((h, i) => {
        h.z -= this.velocity;
        h.x += (this.rotation.x * h.z * 0.12) + h.vx;
        h.y += this.rotation.y * h.z * 0.12;

        // collision window expanded for high velocity
        const collisionWindow = this.velocity + 50; 
        if (h.z < collisionWindow && h.z > -collisionWindow && !h.passed && !h.hit) {
          const dist = Math.sqrt(h.x * h.x + h.y * h.y);
          if (dist < h.radius) {
            this.score += 150;
            this.fuel = Math.min(100, this.fuel + 25); 
            this.triggerFlash('fuel');
            h.passed = true;
          }
        }
        if (h.z < -300) this.targets.splice(i, 1);
      });

      // 6. LASERS
      this.lasers.forEach((l, i) => {
        l.x += l.vx; l.y += l.vy; l.z += l.vz;
        this.targets.forEach(h => {
           // More generous hit detection for lasers
           const dist = Math.sqrt((l.x - h.x)**2 + (l.y - h.y)**2);
           const zDist = Math.abs(l.z - h.z);
           if (dist < h.radius * 1.2 && zDist < 150 && !h.hit && !h.passed) {
             h.hit = true;
             this.score += h.type === 'interceptor' ? 200 : 50;
             this.energy = Math.min(100, this.energy + 30);
             this.triggerFlash('energy');
             this.lasers.splice(i, 1);
           }
        });
        if (l.z > 3500) this.lasers.splice(i, 1);
      });
    },
    draw() {
      const { ctx, canvas, perspective } = this;
      const cx = canvas.width / 2, cy = canvas.height / 2;

      ctx.fillStyle = "#010206";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = "white";
      this.stars.forEach(s => {
        const sc = perspective / (perspective + s.z);
        ctx.beginPath();
        ctx.arc(s.x * sc + cx, s.y * sc + cy, s.size * sc * 3, 0, Math.PI * 2);
        ctx.fill();
      });

      this.targets.forEach(h => {
        const sc = perspective / (perspective + h.z);
        const px = h.x * sc + cx, py = h.y * sc + cy, r = h.radius * sc;

        if (h.z > 0 && !h.hit) {
          ctx.strokeStyle = h.passed ? "lime" : (h.type === 'interceptor' ? "#ff00ff" : "#00f2ff");
          ctx.lineWidth = h.type === 'interceptor' ? 6 * sc : 3 * sc;
          ctx.beginPath();
          ctx.arc(px, py, r, 0, Math.PI * 2);
          ctx.stroke();
          
          if (h.type === 'interceptor') {
              ctx.setLineDash([5, 5]);
              ctx.beginPath();
              ctx.arc(px, py, r * 0.5, 0, Math.PI * 2);
              ctx.stroke();
              ctx.setLineDash([]);
          }
        }
      });

      ctx.strokeStyle = "#ff0044";
      ctx.lineWidth = 3;
      this.lasers.forEach(l => {
        const sc = perspective / (perspective + l.z);
        const nextSc = perspective / (perspective + l.z + 100);
        ctx.beginPath();
        ctx.moveTo(l.x * sc + cx, l.y * sc + cy);
        ctx.lineTo(l.x * nextSc + cx, l.y * nextSc + cy);
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
  position: fixed; inset: 0; background: black; overflow: hidden; cursor: none;
  font-family: 'Orbitron', sans-serif;
}
.game-canvas { display: block; }

.overlay {
  position: absolute; inset: 0; background: rgba(0, 0, 0, 0.8);
  display: flex; align-items: center; justify-content: center; z-index: 100;
}
.menu-box {
  background: #0a0a0a; border: 2px solid #00f2ff; padding: 40px; text-align: center; color: white;
}
.glitch { font-size: 3rem; color: #00f2ff; margin-bottom: 20px; text-shadow: 2px 2px #ff00ff; }
.instructions span { color: #00f2ff; font-weight: bold; }
.dead { color: #ff3c00; }
.primary-btn { background: #00f2ff; border: none; padding: 12px 30px; font-weight: bold; width: 100%; cursor: pointer; margin-bottom: 10px; }
.secondary-btn { background: transparent; color: #00f2ff; border: 1px solid #00f2ff; padding: 12px 30px; width: 100%; cursor: pointer; }

.cockpit-hud { position: absolute; inset: 0; padding: 40px; pointer-events: none; color: #00f2ff; }
.hud-top { display: flex; justify-content: space-between; font-size: 1.8rem; }

.resource-bars { position: absolute; top: 120px; left: 40px; width: 220px; }
.bar-container { margin-bottom: 20px; }
.bar-container label { font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 5px; display: block; }
.bar-bg { width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px; overflow: hidden; }
.bar-fill { height: 100%; transition: width 0.2s ease; }
.energy { background: #ff00ff; }
.fuel { background: #00f2ff; }

/* Replenish Flash Animation */
.bar-fill.flash { background: white !important; filter: brightness(2); }

.cockpit-frame {
  position: absolute; inset: 0; border: 50px solid #111;
  mask-image: radial-gradient(circle at center, transparent 40%, black 100%);
}
.crosshair { position: absolute; top: 50%; left: 50%; width: 80px; height: 80px; border: 1px solid rgba(0, 242, 255, 0.2); border-radius: 50%; margin: -40px; }
.aim-dot { position: absolute; top: 50%; left: 50%; width: 4px; height: 4px; background: red; margin: -2px; }
.hud-bottom { position: absolute; bottom: 40px; left: 40px; right: 40px; display: flex; justify-content: space-between; }
.exit-btn { background: transparent; color: #ff3c00; border: 1px solid #ff3c00; padding: 8px 16px; pointer-events: auto; cursor: pointer; }
</style>