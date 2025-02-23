<template>
    <div class="container"
         @mousedown="handleDragStart"
         @mousemove="handleDragMove"
         @mouseup="handleDragEnd"
         @touchstart="handleDragStart"
         @touchmove="handleDragMove"
         @touchend="handleDragEnd">
    
      <!-- Header -->
      <h1 class="header" :class="{ flying: isFlying }"
          :style="{ transitionDuration: isFlying ? '0.5s' : '0.1s' }">
        Sigurður Teitur Tannason
      </h1>
    
      <!-- Starfield -->
      <div class="starfield" v-if="!showMenu">
        <div
          v-for="(star, i) in stars"
          :key="i"
          class="star"
          :style="{ top: star.y + '%', left: star.x + '%' }"
        ></div>
      </div>
    
      <!-- Spaceship Button (visible if we're not in the menu) -->
      <Spaceship
        v-if="!showMenu && showSpaceship"
        class="spaceship-component"
        @click="handleSpaceshipClick"
        :playing="isFlying"
      />
    
      <!-- Destination Panel (hidden by default; only visible when user clicks spaceship) -->
      <div v-if="destinationPanelVisible" class="destination-panel">
        <p>Choose Destination:</p>
        <div class="destination-options">
            <div class="destination-option" 
                @click="selectDestination('HomePage')"
                :class="{ selected: selectedDestination === 'HomePage' }">
            Home
            </div>
            <div class="destination-option" 
                @click="selectDestination('TypingPractice')"
                :class="{ selected: selectedDestination === 'TypingPractice' }">
            Away
            </div>
        </div>
      </div>

    
      <!-- Info Popup -->
      <div class="info-popup" v-if="infoPopupVisible">
        <div class="info-content">
          <h3>How to Use</h3>
          <p>Press the spaceship to reveal destination options.<br />
          Choose Home or Away, then confirm to start your journey.</p>
          <button class="close-button" @click="toggleInfoPopup">Close</button>
        </div>
      </div>
    
      <!-- Transition Overlay for travel -->
      <div
        v-if="overlayActive"
        class="transition-overlay"
        :class="{ reverse: reverseActive }"
      ></div>
    
      <!-- Menu (displayed on top of the white star) -->
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
  
      isFlying: false,
      currentMultiplier: 4,
      targetMultiplier: 4,

  
      animationId: null,
      lastTimestamp: 0,
  
      // Destination logic – default is "Explore"
      selectedDestination: null,
      destinationPanelVisible: true,
  
      showSpaceship: true,
      overlayActive: false,
      reverseActive: false,
      showMenu: false,
      infoPopupVisible: false,
  
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
    // If the destination changes while already flying, automatically start journey.
    selectedDestination(newVal) {
      if (this.isFlying && newVal !== "Explore") {
        this.startJourney();
      }
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
    toggleFlight() {
      this.isFlying = !this.isFlying;
      this.targetMultiplier = this.isFlying ? 200 : 4;
      this.updateMultiplier();
    },
    // Instead of startJourney being triggered directly by the spaceship,
    // we now use a dedicated handler.
    handleSpaceshipClick() {
        if (!this.isFlying) {
            this.startJourney();
        }
        else {
            this.toggleFlight();
        }
    },
    selectDestination(option) {
        if (this.selectedDestination === option) {
        this.selectedDestination = null;
        } else {
        this.selectedDestination = option;
        }
    },
    startJourney() {
      // Only proceed if a destination (other than "Explore") is selected.
      if (this.selectedDestination == null) {
        this.isFlying = true;
        this.targetMultiplier = 200;
        this.updateMultiplier();
        return;
      }
      // Hide destination panel.
      this.destinationPanelVisible = false;
      // Begin journey: hide spaceship and set travel speed high.
      this.showSpaceship = false;
      this.isFlying = true;
      this.targetMultiplier = 200;
      this.updateMultiplier();
      // Trigger overlay forward animation.
      this.overlayActive = true;
      this.reverseActive = false;
      // After the overlay animation, show the menu.
      setTimeout(() => {
        this.showMenu = true;
      }, 2000);
    },
    goBackHome() {
      this.showMenu = false;
      this.overlayActive = true;
      this.reverseActive = true;
      setTimeout(() => {
        this.overlayActive = false;
        this.reverseActive = false;
        this.showSpaceship = true;
        this.isFlying = false;
        this.targetMultiplier = 4;
        this.destinationPanelVisible = true;

        this.updateMultiplier();
      }, 200);
    },
    toggleInfoPopup() {
      this.infoPopupVisible = !this.infoPopupVisible;
    },
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

<style>

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
@media (max-width: 800px) {
  .header {
    top: 30%;
    font-size: 1.5rem;
    transform: translateX(-50%) translateY(-200%) scale(1.2);
    transition: transform 0.1s ease;
  }
  .header.flying {
    transform: translateX(-50%) translateY(-1000%) scale(4);
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

/* Destination panel styling (hidden by default, appears when destinationPanelVisible is true) */
.destination-panel {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  background: transparent;
  color: white;
  padding: 20px 30px;
  border-radius: 15px;
  text-align: center;
  font-size: 1.2rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  z-index: 3;
}
.destination-panel p {
  margin: 0 0 10px;
  font-weight: bold;
}
.destination-options {
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
}
.destination-option {
  background: rgba(255, 255, 255, 0.3);
  padding: 10px 20px;
  border-radius: 10px;
  margin: 0 10px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background 0.3s ease;
}
.destination-option:hover {
  background: rgba(255, 255, 255, 0.1);
  /**shrinks by 5%*/
    transform: scale(0.95);
}

.destination-option.selected {
  background: rgb(177, 145, 145);
  border-color: white;
}
.destination-option.selected:hover {
  background: rgba(177, 145, 145, 0.582);
  border-color: white;
}

/* Confirm and Cancel buttons */
.confirm-button,
.cancel-button {
  background: white;
  color: black;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  margin: 5px;
  cursor: pointer;
  font-size: 1rem;
}
.confirm-button:hover,
.cancel-button:hover {
  background: #ddd;
}

/* Info icon in destination panel */
.info-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  background: white;
  color: black;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  text-align: center;
  line-height: 25px;
  font-weight: bold;
  cursor: pointer;
}

/* Info popup overlay */
.info-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.7);
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
}
.info-content {
  background: white;
  color: black;
  padding: 20px;
  border-radius: 10px;
  max-width: 80%;
  text-align: center;
}
.close-button {
  margin-top: 15px;
  padding: 5px 10px;
  border: none;
  background: black;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

/* Overlay for travel */
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
</style>