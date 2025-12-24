<template>
  <div id="app" :class="{ 'menu-open': isMenuOpen }">
    <!-- Ueno-style Minimalist Nav -->
    <nav class="ueno-nav">
      <router-link to="/" class="logo">S.T.T</router-link>
      <div class="nav-links">
        <router-link to="/about">About</router-link>
        <router-link to="/experience">Work</router-link>
        <router-link to="/focus">Focus</router-link>
        <router-link to="/games">Play</router-link>
        <router-link to="/contact">Contact</router-link>
      </div>
    </nav>

    <!-- Page Content -->
    <router-view v-slot="{ Component }">
      <transition name="page-warp" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>

    <!-- The "Warp" Bridge (Flash of White) -->
    <div class="warp-bridge" :class="{ active: isWarping }"></div>
  </div>
</template>

<script>
export default {
  data() {
    return { isWarping: false };
  },
  watch: {
    $route() {
      // Every time we change pages, we do a quick warp flash
      this.isWarping = true;
      setTimeout(() => {
        this.isWarping = false;
      }, 600);
    },
  },
};
</script>

<style>
/* Ueno Typography Setup */
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Playfair+Display:italic,wght@700&display=swap");

:root {
  --ueno-orange: #ff4d00; /* Their signature International Orange */
  --bg: #ffffff;
  --text: #000000;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: "Inter", sans-serif;
  -webkit-font-smoothing: antialiased;
}

/* Nav Styles */
.ueno-nav {
  position: absolute;
  top: 0;
  width: 100%;
  padding: 40px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
  box-sizing: border-box;
  background: transparent;
}

.logo {
  font-weight: 900;
  text-decoration: none;
  color: var(--text);
  font-size: 1.2rem;
}

.nav-links a {
  margin-left: 40px;
  text-decoration: none;
  color: var(--text);
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  opacity: 0.4;
  transition: opacity 0.3s;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  opacity: 1;
}

/* Page Warp Transition */
.warp-bridge {
  position: fixed;
  inset: 0;
  background: white;
  z-index: 9999;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}
.warp-bridge.active {
  opacity: 1;
}

.page-warp-enter-active,
.page-warp-leave-active {
  transition: opacity 0.3s, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.page-warp-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.page-warp-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

@media (max-width: 768px) {
  .ueno-nav {
    padding: 20px;
  }
  .nav-links a {
    margin-left: 15px;
    font-size: 0.7rem;
  }
}
</style>
