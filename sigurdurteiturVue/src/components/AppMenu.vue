<template>
  <div class="menu-container">
    <h2>Welcome to my website, It does not work</h2>

    <button @click="$emit('goBack')">Go Back Home</button>
  </div>
</template>

<script>
export default {
  name: "AppMenu",
  emits: ["goBack"]
};
</script>

<style scoped>
.menu-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* Black text on white star behind it */
  color: black;
  text-align: center;
  z-index: 5; /* above the white circle */
  background: transparent; /* so the white star behind is visible */
  padding: 20px;
}
</style>
