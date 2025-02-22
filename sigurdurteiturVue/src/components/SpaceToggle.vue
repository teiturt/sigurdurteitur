<template>
    <div class="container">
      <!-- Header with your name -->
      <h1 class="header" :class="{ flying: isFlying }">
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
        stars: [],         // Array of star objects: { angle, radius, speed, x, y }
        starCount: 50,     // Total number of stars in the starfield
        isFlying: false,   // True when boosters are on (stars move quickly); false: nearly static
        currentMultiplier: 0.02, // This value is used to update star positions.
        targetMultiplier: 0.02,  // This is what we want the multiplier to eventually be.
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
        const angle = Math.random() * Math.PI * 2;
        const factor = 15; // Adjust standard deviation factor for initial radius.
        const radius = startCentered ? Math.random() * 2 : Math.abs(this.randomNormal() * factor);
        const speed = 0.2 + Math.random() * 0.5;
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
      // Main animation loop: update star positions based on currentMultiplier.
      animateStars() {
        this.stars.forEach(star => {
          // Use the currentMultiplier that is being smoothly updated.
          star.radius += star.speed * this.currentMultiplier;
          // Convert from polar (radius, angle) to Cartesian coordinates (in percentages).
          star.x = 50 + star.radius * Math.cos(star.angle);
          star.y = 50 + star.radius * Math.sin(star.angle);
          // If the star moves outside the viewport, respawn it.
          if (star.x < 0 || star.x > 100 || star.y < 0 || star.y > 100) {
            Object.assign(star, this.randomStar(false));
          }
        });
        // Force Vue to update the positions.
        this.$forceUpdate();
        this.animationId = requestAnimationFrame(this.animateStars);
      },
      // Gradually update currentMultiplier toward targetMultiplier.
      updateMultiplier() {
        const diff = this.targetMultiplier - this.currentMultiplier;
        if (Math.abs(diff) < 0.01) {
          this.currentMultiplier = this.targetMultiplier;
          return;
        }
        this.currentMultiplier += diff * 0.1;
        requestAnimationFrame(() => this.updateMultiplier());
      },
      // Toggle flight mode when the spaceship is clicked.
      toggleFlight() {
        this.isFlying = !this.isFlying;
        // Set the target multiplier: 1 for flying, 0.02 for nearly static.
        this.targetMultiplier = this.isFlying ? 1 : 0.02;
        // Start gradually updating the current multiplier.
        this.updateMultiplier();
      }
    }
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap');
  
  /* Container covers full viewport with black background (space) */
  .container {
    background: black;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    position: relative;
  }
  
  /* Header styling */
  .header {
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translateX(-50%) translateY(-400%) scale(1.5);
    font-family: 'Cinzel', serif;
    color: white;
    font-size: 2rem;
    transition: transform 0.5s ease;
    z-index: 2;
  }
  
  /* When flight is on, animate the header upward and enlarge it */
  .header.flying {
    transform: translateX(-50%) translateY(-1000%) scale(3.5);
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
  