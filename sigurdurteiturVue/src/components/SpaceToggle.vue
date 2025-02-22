<template>
    <div class="container"
         @mousedown="handleDragStart"
         @mousemove="handleDragMove"
         @mouseup="handleDragEnd"
         @touchstart="handleDragStart"
         @touchmove="handleDragMove"
         @touchend="handleDragEnd">
    
      <!-- Header with your name -->
      <h1 class="header" :class="{ flying: isFlying }"
          :style="{ transitionDuration: isFlying ? '0.5s' : '0.1s' }">
        Sigurður Teitur Tannason
      </h1>
    
      <!-- Starfield (only visible if we're not at the menu) -->
      <div class="starfield" v-if="!showMenu">
        <div
          v-for="(star, i) in stars"
          :key="i"
          class="star"
          :style="{ top: star.y + '%', left: star.x + '%' }"
        ></div>
      </div>
    
      <!-- Spaceship (hidden once we start traveling) -->
      <Spaceship
        v-if="!showMenu && showSpaceship && selectedDestination !== 'Explore'"
        class="spaceship-component"
        @click="startJourney"
        :playing="isFlying"
      />
      <Spaceship
        v-else-if="selectedDestination === 'Explore'"
        class="spaceship-component"
        :playing="isFlying"
        @toggle="toggleFlight"
        />
    
      <!-- Destination selection + Play button (shown when not in menu) -->
      <div v-if="!showMenu" class="destination-panel">
        <p>Destination</p>
        <label>
          <input type="radio" value="HomePage" v-model="selectedDestination" /> Home
        </label>
        <label>
          <input type="radio" value="TypingPractice" v-model="selectedDestination" /> Away
        </label>
        <label>
          <input type="radio" value="Explore" v-model="selectedDestination" /> Explore
        </label>
      </div>
    
      <!-- The overlay circle for forward travel (white star) -->
      <div
        v-if="overlayActive"
        class="transition-overlay"
        :class="{ reverse: reverseActive }"
      ></div>
    
      <!-- Menu (on white star) -->
      <AppMenu
        v-if="showMenu"
        :class="{ show: showMenu }"
        @goBack="goBackHome"
      />
    </div>
  </template>
    
  <script>
  import Spaceship from "./Spaceship.vue";
  import AppMenu from "./AppMenu.vue";
    
  export default {
    name: "SpaceToggle",
    components: { Spaceship, AppMenu },
    data() {
      return {
        stars: [],
        starCount: 50,
    
        /* Flight speed logic */
        isFlying: false,
        currentMultiplier: 0.02,
        targetMultiplier: 0.02,
    
        /* requestAnimationFrame tracking */
        animationId: null,
        lastTimestamp: 0,
    
        /* Destination logic */
        selectedDestination: null, // e.g. "HomePage", "TypingPractice", "Settings", "Explore"
    
        /* UI states */
        showSpaceship: true,  // Hide once we begin traveling
        overlayActive: false, // True when starApproach or starApproachReverse is running
        reverseActive: false, // True if playing the reverse animation
        showMenu: false,      // True once we've arrived at the menu
    
        /* Drag properties for turning (optional) */
        globalAngle: 0,
        dragging: false,
        startX: 0,
        initialGlobalAngle: 0
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
    watch: {
    selectedDestination(newVal) {
      // If we're already flying and the new destination isn't Explore,
      // automatically trigger the journey.
      if (this.isFlying && newVal !== "Explore") {
        this.startJourney();
      }
    }
  },
    methods: {
      /* Normal-distribution star placement */
      randomNormal() {
        let u = 0, v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
      },
      randomStar(startCentered = false) {
        const angle = Math.random() * Math.PI * 2;
        const factor = 15;
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
        const dt = (timestamp - this.lastTimestamp) / 1000;
        this.lastTimestamp = timestamp;
    
        this.stars.forEach(star => {
          star.radius += star.speed * dt * this.currentMultiplier;
          const effectiveAngle = star.angle + this.globalAngle;
          star.x = 50 + star.radius * Math.cos(effectiveAngle);
          star.y = 50 + star.radius * Math.sin(effectiveAngle);
    
          // Respawn if out of view
          if (star.x < 0 || star.x > 100 || star.y < 0 || star.y > 100) {
            Object.assign(star, this.randomStar(false));
          }
        });
    
        this.$forceUpdate();
        this.animationId = requestAnimationFrame(this.animateStars);
      },
    
      updateMultiplier() {
        const diff = this.targetMultiplier - this.currentMultiplier;
        if (Math.abs(diff) < 0.01) {
          this.currentMultiplier = this.targetMultiplier;
          return;
        }
        this.currentMultiplier += diff * 0.1;
        requestAnimationFrame(() => this.updateMultiplier());
      },
    
      /* Toggle flight speed */
      toggleFlight() {
        this.isFlying = !this.isFlying;
        this.targetMultiplier = this.isFlying ? 200 : 4;
        this.updateMultiplier();
      },
    
      /* Start journey if a destination is selected (other than Explore) */
      startJourney() {
        // Only start if a destination is selected and it's not Explore.
        if (!this.selectedDestination || this.selectedDestination === "Explore") {
          return;
        }
    
        // Begin journey: hide spaceship and set travel speed high.
        this.showSpaceship = false;
        this.isFlying = true;
        this.targetMultiplier = 200;
        this.updateMultiplier();
    
        // Trigger overlay forward animation.
        this.overlayActive = true;
        this.reverseActive = false;
    
        // After the overlay animation finishes, show the menu.
        setTimeout(() => {
          this.showMenu = true;
          // Note: We do NOT clear selectedDestination here; it remains for future reference.
        }, 2000); // Adjust duration as desired.
      },
    
      /* When user clicks "Go Back Home" in the menu */
      goBackHome() {
        // Hide the menu.
        this.showMenu = false;
    
        // Trigger reverse overlay animation.
        this.overlayActive = true;
        this.reverseActive = true;
    
        setTimeout(() => {
          // After reverse animation, hide overlay and restore state.
          this.overlayActive = false;
          this.reverseActive = false;
    
          // Show the spaceship.
          this.showSpaceship = true;
    
          // Stop travel: set flying to false but keep the previously selected destination.
          this.isFlying = false;
          this.targetMultiplier = 4;
          this.updateMultiplier();
        }, 200); // Adjust duration as desired.
      },
    
      /* Optional turning handlers */
      handleDragStart(e) {
        if (this.isFlying) return;
        this.dragging = true;
        this.startX = e.clientX || e.touches[0].clientX;
        this.initialGlobalAngle = this.globalAngle;
      },
      handleDragMove(e) {
        if (!this.dragging) return;
        const currentX = e.clientX || e.touches[0].clientX;
        const deltaX = currentX - this.startX;
        const sensitivity = 0.005;
        this.globalAngle = this.initialGlobalAngle + deltaX * sensitivity;
      },
      handleDragEnd() {
        this.dragging = false;
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
    
  /* Header styling */
  .header {
    position: absolute;
    top: 20%;
    left: 50%;
    transform: translateX(-50%) translateY(-400%) scale(1.5);
    font-family: 'Roboto', 'Helvetica', sans-serif;
    color: white;
    font-size: 2rem;
    transition: transform 0.1s ease;
    z-index: 2;
  }
  .header.flying {
    transform: translateX(-50%) translateY(-1000%) scale(3.5);
  }
  @media (max-width: 600px) {
    .header {
      top: 10%;
      font-size: 1.5rem;
      transform: translateX(-50%) translateY(-200%) scale(1.2);
      transition: transform 0.1s ease;
    }
    .header.flying {
      transform: translateX(-50%) translateY(-600%) scale(2);
    }
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
    
  .spaceship-component {
    transition: opacity 0.5s ease;
  }
    
  .destination-panel {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.2); /* Slightly more opaque */
    color: white;
    padding: 20px 30px; /* Increase padding for a larger box */
    border-radius: 15px; /* More rounded corners */
    text-align: center;
    font-size: 1.2rem; /* Increase font size */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); /* Add subtle shadow */
    z-index: 3;
    }
    .destination-panel p {
    margin: 0 0 10px;
    font-weight: bold;
    }
    .destination-panel label {
    display: inline-block;
    margin: 0 10px;
    cursor: pointer;
    font-size: 1.1rem;
    }
    .destination-panel input[type="radio"] {
    margin-right: 5px;
    }

    
  /* The overlay circle for travel */
  .transition-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 1vw;
    height: 1vw;
    background: white;
    border-radius: 50%;
    transform: translate(-50%, -50%) scale(0);
    z-index: 4;
    animation: starApproach 2s forwards;
  }
  .transition-overlay.reverse {
    animation: starApproachReverse 2s forwards;
  }
    
  /* Example exponential forward animation keyframes */
  @keyframes starApproach {
    0% {
      transform: translate(-50%, -50%) scale(0);
    }
    5% {
      transform: translate(-50%, -50%) scale(0.01);
    }
    10% {
      transform: translate(-50%, -50%) scale(0.015);
    }
    15% {
      transform: translate(-50%, -50%) scale(0.04);
    }
    20% {
      transform: translate(-50%, -50%) scale(0.07);
    }
    25% {
      transform: translate(-50%, -50%) scale(0.1);
    }
    30% {
      transform: translate(-50%, -50%) scale(0.15);
    }
    35% {
      transform: translate(-50%, -50%) scale(0.2);
    }
    40% {
      transform: translate(-50%, -50%) scale(0.3);
    }
    45% {
      transform: translate(-50%, -50%) scale(0.4);
    }
    50% {
      transform: translate(-50%, -50%) scale(0.5);
    }
    55% {
      transform: translate(-50%, -50%) scale(0.6);
    }
    60% {
      transform: translate(-50%, -50%) scale(0.7);
    }
    65% {
      transform: translate(-50%, -50%) scale(0.8);
    }
    70% {
      transform: translate(-50%, -50%) scale(1.3);
    }
    75% {
      transform: translate(-50%, -50%) scale(2.2);
    }
    80% {
      transform: translate(-50%, -50%) scale(3.1);
    }
    85% {
      transform: translate(-50%, -50%) scale(4);
    }
    90% {
      transform: translate(-50%, -50%) scale(7);
    }
    91% {
      transform: translate(-50%, -50%) scale(9);
    }
    92% {
      transform: translate(-50%, -50%) scale(12);
    }
    93% {
      transform: translate(-50%, -50%) scale(14);
    }
    94% {
      transform: translate(-50%, -50%) scale(16);
    }
    95% {
      transform: translate(-50%, -50%) scale(20);
    }
    96% {
      transform: translate(-50%, -50%) scale(28);
    }
    97% {
      transform: translate(-50%, -50%) scale(48);
    }
    98% {
      transform: translate(-50%, -50%) scale(100);
    }
    99% {
      transform: translate(-50%, -50%) scale(200);
    }
    100% {
      transform: translate(-50%, -50%) scale(400);
    }
  }
    
  /* Reverse animation keyframes */
  @keyframes starApproachReverse {
    0% {
      transform: translate(-50%, -50%) scale(400);
    }
    3% {
      transform: translate(-50%, -50%) scale(48);
    }
    6% {
      transform: translate(-50%, -50%) scale(24);
    }
    9% {
      transform: translate(-50%, -50%) scale(12);
    }
    12% {
      transform: translate(-50%, -50%) scale(2);
    }
    15% {
      transform: translate(-50%, -50%) scale(1);
    }
    18% {
      transform: translate(-50%, -50%) scale(0.5);
    }
    21% {
      transform: translate(-50%, -50%) scale(0.2);
    }
    24% {
      transform: translate(-50%, -50%) scale(0.1);
    }
    27% {
      transform: translate(-50%, -50%) scale(0.05);
    }
    30% {
      transform: translate(-50%, -50%) scale(0.01);
    }
    100% {
      transform: translate(-50%, -50%) scale(0);
    }
  }
    
  /* Menu styles are defined in AppMenu.vue */
  </style>
  