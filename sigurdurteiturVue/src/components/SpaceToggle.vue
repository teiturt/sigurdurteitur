<template>
    <div class="container">
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
        stars: [],         // Array of star objects: { angle, radius, speed, x, y }
        starCount: 50,     // Total number of stars in the starfield
        isFlying: false,   // True: booster on (stars move quickly); false: nearly static
        animationId: null  // For canceling requestAnimationFrame if needed
      };
    },
    mounted() {
      this.initStars();
      this.animateStars();
    },
    beforeUnmount() {
      if (this.animationId) {
        cancelAnimationFrame(this.animationId);
      }
    },
    methods: {
      // Generate a normally distributed random number using the Box-Muller transform.
      randomNormal() {
        let u = 0, v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
      },
      // Generate a star object.
      // If startCentered is true, spawn it very near the center.
      randomStar(startCentered = false) {
        const angle = Math.random() * Math.PI * 2; // Uniform angle in radians
        const factor = 15; // Standard deviation factor for initial radius (adjust as desired)
        // For a normally distributed radius, use the absolute value of a normal number.
        const radius = startCentered ? Math.random() * 2 : Math.abs(this.randomNormal() * factor);
        const speed = 0.2 + Math.random() * 0.5; // Base speed for the star
        return { angle, radius, speed, x: 50, y: 50 };
      },
      // Initialize the starfield with stars distributed (via a normal distribution) about the center.
      initStars() {
        const newStars = [];
        for (let i = 0; i < this.starCount; i++) {
          newStars.push(this.randomStar(false));
        }
        this.stars = newStars;
      },
      // Main animation loop: update star positions based on flight mode.
      animateStars() {
        // If flying, multiplier is 1; if not, stars move very slowly.
        const multiplier = this.isFlying ? 1 : 0.02;
        this.stars.forEach(star => {
          star.radius += star.speed * multiplier;
          // Convert from polar (radius, angle) to Cartesian coordinates (as percentages).
          star.x = 50 + star.radius * Math.cos(star.angle);
          star.y = 50 + star.radius * Math.sin(star.angle);
          // If star goes out of view, respawn it near the center.
          if (star.x < 0 || star.x > 100 || star.y < 0 || star.y > 100) {
            Object.assign(star, this.randomStar(false));
            }
        });
        // Force Vue to update the positions.
        this.$forceUpdate();
        this.animationId = requestAnimationFrame(this.animateStars);
      },
      // Toggle the flight mode when the spaceship is clicked.
      toggleFlight() {
        this.isFlying = !this.isFlying;
      }
    }
  };
  </script>
  
  <style scoped>
  /* Container: full viewport with black background (space) */
  .container {
    background: black;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    position: relative;
  }
  
  /* Starfield covers the viewport; stars are positioned absolutely */
  .starfield {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
  
  /* Star styling: white dots */
  .star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
  }
  </style>
  