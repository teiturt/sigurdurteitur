<template>
    <div class="spaceship" @click="handleClick">
      <svg v-if="!playing" width="80" height="80" viewBox="0 0 100 100">
        <!-- Play icon: a triangle -->
        <polygon points="30,20 30,80 70,50" fill="white" />
      </svg>
      <svg v-else width="80" height="80" viewBox="0 0 100 100">
        <!-- Pause icon: two vertical bars -->
        <rect x="30" y="20" width="12" height="60" fill="white" />
        <rect x="58" y="20" width="12" height="60" fill="white" />
      </svg>
    </div>
  </template>
  
  <script>
  export default {
    name: "SpaceShip",
    props: {
      playing: {
        type: Boolean,
        default: false
      }
    },
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
  