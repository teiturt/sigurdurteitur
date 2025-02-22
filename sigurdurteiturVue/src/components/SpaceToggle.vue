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
        v-if="!showMenu && showSpaceship"
        class="spaceship-component"
        @toggle="toggleFlight"
        :playing="isFlying"
      />
  
      <!-- Destination selection + Play button (shown when not in menu) -->
      <div v-if="!showMenu" class="destination-panel">
        <p>Select Destination:</p>
        <label>
          <input type="radio" value="HomePage" v-model="selectedDestination" /> HomePage
        </label>
        <label>
          <input type="radio" value="TypingPractice" v-model="selectedDestination" /> Typing Practice
        </label>
        <label>
          <input type="radio" value="Settings" v-model="selectedDestination" /> Settings
        </label>
        <label>
          <input type="radio" value="Explore" v-model="selectedDestination" /> Explore
        </label>
        <br />
        <button @click="startJourney">Play</button>
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
    methods: {
      /* 
        Normal-distribution star placement 
      */
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
  
      /* 
        Toggle normal flight speed 
      */
      toggleFlight() {
        this.isFlying = !this.isFlying;
        this.targetMultiplier = this.isFlying ? 200 : 4;
        this.updateMultiplier();
      },
  
      /* 
        Called when user presses "Play" 
        If "Explore" is chosen, do nothing special
        Else do a starApproach animation
      */
      startJourney() {
        // If no destination or "Explore," do your logic...
        if (!this.selectedDestination || this.selectedDestination === "Explore") {
            return;
        }

        // 1. Hide the spaceship
        this.showSpaceship = false;

        // 2. Increase star speed for “travel”
        this.isFlying = true;
        this.targetMultiplier = 200; // for example
        this.updateMultiplier();

        // 3. Trigger your overlay’s forward animation
        this.overlayActive = true;
        this.reverseActive = false;

        // 4. After 4 seconds (the length of starApproach), show the menu
        setTimeout(() => {
            this.showMenu = true;
            // The overlay remains behind the menu
        }, 2000);
    },

  
      /* 
        Called from the menu "Go Back Home" 
        Plays the reverse animation from scale(20)->scale(0) 
      */
      goBackHome() {
        // Hide the menu
        this.showMenu = false;

        // Start the reverse overlay animation by activating overlay and setting reverse flag.
        this.overlayActive = true;
        this.reverseActive = true; // This triggers starApproachReverse keyframes

        // After the reverse animation finishes (here 2 seconds), reset the state.
        setTimeout(() => {
            // Hide the overlay and reset the reverse flag.
            this.overlayActive = false;
            this.reverseActive = false;

            // Show the spaceship again.
            this.showSpaceship = true;

            // Stop the stars by setting isFlying to false and reducing the speed.
            this.isFlying = false;
            this.targetMultiplier = 4; // Lower travel speed.
            this.updateMultiplier();
            
            // Optionally, reset the destination selection.
            // this.selectedDestination = null;
        }, 200); // Adjust the duration to match your reverse animation's length.
        },
  
      /* 
        Optional turning 
      */
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
  
  /* Destination selection panel */
  .destination-panel {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.1);
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-align: center;
    z-index: 3;
  }
  
  /* The overlay circle for forward/backward star approach */
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
  
  /* Reverse animation triggers starApproachReverse */
  .transition-overlay.reverse {
    animation: starApproachReverse 2s forwards;
  }
  
  /* 
    Forward animation: 
    We want to have an exponential scale-up effect
    I want the reverse of this
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
    */
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
    93% {
      transform: translate(-50%, -50%) scale(14);
    }
    95% {
      transform: translate(-50%, -50%) scale(20);
    }
    97% {
      transform: translate(-50%, -50%) scale(48);
    }
    100% {
      transform: translate(-50%, -50%) scale(400);
    }




  }
  
  /* 
    Reverse animation: 
    total 2s 
     We want reverse of this:
       @keyframes starApproach {
    0% {
      transform: translate(-50%, -50%) scale(0.1);
    }
    70% {
      transform: translate(-50%, -50%) scale(0.5);
    }
    73% {
      transform: translate(-50%, -50%) scale(0.6);
    }
    76% {
      transform: translate(-50%, -50%) scale(0.7);
    }
    79% {
      transform: translate(-50%, -50%) scale(0.8);
    }
    82% {
      transform: translate(-50%, -50%) scale(0.9);
    }
    85% {
      transform: translate(-50%, -50%) scale(1);
    }
    88% {
      transform: translate(-50%, -50%) scale(2);
    }
    91% {
      transform: translate(-50%, -50%) scale(4);
    }
    94% {
      transform: translate(-50%, -50%) scale(8);
    }
    97% {
      transform: translate(-50%, -50%) scale(16);
    }

    

    100% {
      transform: translate(-50%, -50%) scale(400);
    }
  }
  */
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
  
  /* Menu styles are in AppMenu.vue, presumably. */
  </style>
  