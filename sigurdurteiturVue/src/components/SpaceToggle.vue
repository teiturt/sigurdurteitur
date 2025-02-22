<template>
    <div class="container">
      <!-- Header with your name -->
      <h1 class="header" :class="{ flying: isFlying }" :style="{ transitionDuration: isFlying ? '0.5s' : '0.1s' }">
        Sigurður Teitur Tannason
      </h1>
    
      <!-- Starfield -->
      <div class="starfield">
        <div
          v-for="(star, i) in stars"
          :key="i"
          class="star"
          :style="{ top: star.y + '%', left: star.x + '%' }"
        ></div>
      </div>
    
      <!-- Spaceship Component in the center -->
      <Spaceship @toggle="toggleFlight" />
    </div>
  </template>
  
  <script>
  import Spaceship from "./Spaceship.vue";
  
  export default {
    name: "SpaceToggle",
    components: { Spaceship },
    data() {
    return {
        stars: [],
        starCount: 50,
        isFlying: false,
        currentMultiplier: 0.02,
        targetMultiplier: 0.02,
        animationId: null,
        lastTimestamp: 0  // For calculating delta time between frames
    };
    },

    mounted() {
    this.initStars();
    this.animationId = requestAnimationFrame(this.animateStars);
    },

    beforeUnmount() {
      if (this.animationId) {
        cancelAnimationFrame(this.animationId);
      }
    },
    methods: {
      randomNormal() {
        let u = 0, v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
      },
      randomStar(startCentered = false) {
        const angle = Math.random() * Math.PI * 2;
        const factor = 15; // Standard deviation factor.
        const radius = startCentered ? Math.random() * 2 : Math.abs(this.randomNormal() * factor);
        const speed = 0.2 + Math.random() * 0.5;
        return { angle, radius, speed, x: 50, y: 50 };
      },
      initStars() {
        const newStars = [];
        for (let i = 0; i < this.starCount; i++) {
          newStars.push(this.randomStar(false));
        }
        this.stars = newStars;
      },
      animateStars(timestamp) {
        if (!this.lastTimestamp) {
            this.lastTimestamp = timestamp;
        }
        // Calculate delta time (in seconds)
        const dt = (timestamp - this.lastTimestamp) / 1000;
        this.lastTimestamp = timestamp;

        this.stars.forEach(star => {
            // Update the radius using the delta time
            star.radius += star.speed * dt * this.currentMultiplier;
            // Convert from polar (radius, angle) to Cartesian coordinates (in percentages)
            star.x = 50 + star.radius * Math.cos(star.angle);
            star.y = 50 + star.radius * Math.sin(star.angle);
            // If the star moves outside the viewport, respawn it
            if (star.x < 0 || star.x > 100 || star.y < 0 || star.y > 100) {
            Object.assign(star, this.randomStar(false));
            }
        });
        // Force Vue to update the positions
        this.$forceUpdate();
        this.animationId = requestAnimationFrame(this.animateStars);
        }
,
      updateMultiplier() {
        const diff = this.targetMultiplier - this.currentMultiplier;
        if (Math.abs(diff) < 0.01) {
          this.currentMultiplier = this.targetMultiplier;
          return;
        }
        this.currentMultiplier += diff * 0.1;
        requestAnimationFrame(() => this.updateMultiplier());
      },
      toggleFlight() {
        this.isFlying = !this.isFlying;
        // Set a higher target multiplier when flying
        this.targetMultiplier = this.isFlying ? 100 : 4;
        this.updateMultiplier();
        }

    }
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
  
  .container {
    background: black;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    position: relative;
  }
  
  /* Header styling with Roboto, falling back to Helvetica */
  .header {
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translateX(-50%) translateY(-400%) scale(1.5);
    font-family: 'Roboto', 'Helvetica', sans-serif;
    color: white;
    font-size: 2rem;
    /* Transition duration is set dynamically via inline style */
    z-index: 2;
  }
  
  /* When flight is on, animate the header upward and enlarge it */
  .header.flying {
    transform: translateX(-50%) translateY(-1000%) scale(3.5);
  }
  
  .starfield {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
  
  .star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
  }
  </style>
  