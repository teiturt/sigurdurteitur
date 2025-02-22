<template>
    <div class="spaceship" @click="handleClick">
      <!-- Simple spaceship shape (back side) -->
      <svg width="80" height="80" viewBox="0 0 100 100">
        <!-- Main body -->
        <polygon points="50,20 70,80 50,65 30,80" fill="white" />
      </svg>
    </div>
  </template>
  
  <script>
  export default {
    name: "SpaceShipComponent",
    methods: {
      handleClick() {
        this.$emit('toggle');
      }
    }
  };
  </script>
  
  <style scoped>
  .spaceship {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    cursor: pointer;
    transition: transform 0.3s ease;
  }
  .spaceship:active {
    transform: translate(-50%, -50%) scale(0.9);
  }
  </style>
  