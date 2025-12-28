<template>
  <div id="app">
    <!-- 1. We apply a dynamic class 'is-dark-text' based on our script -->
    <nav class="ueno-nav" :class="{ 'is-dark-text': navIsDark }" v-if="showNav">
      <router-link to="/" class="logo">S.T.T</router-link>
      <div class="nav-links">
        <router-link to="/about">About</router-link>
        <router-link to="/experience">Work</router-link>
        <router-link to="/focus">Focus</router-link>
        <router-link to="/games">Play</router-link>
        <router-link to="/contact">Contact</router-link>
      </div>
    </nav>

    <router-view v-slot="{ Component }">
      <transition name="page-warp" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>

    <div class="warp-bridge" :class="{ active: isWarping }"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isWarping: false,
      navIsDark: false,
    };
  },
  computed: {
    showNav() {
      // List the paths where you want the "Immersive Fullscreen" experience
      const hiddenRoutes = ["/games/console", "/games/void-pilot"];

      return !hiddenRoutes.includes(this.$route.path);
    },
  },
  watch: {
    $route: {
      immediate: true,
      handler() {
        this.updateNavColor();
      },
    },
  },
  mounted() {
    window.addEventListener("scroll", this.updateNavColor);
  },
  unmounted() {
    window.removeEventListener("scroll", this.updateNavColor);
  },
  methods: {
    updateNavColor() {
      const path = this.$route.path;
      if (path !== "/") {
        this.navIsDark = true;
        return;
      }
      const heroHeight = window.innerHeight;
      if (window.scrollY > heroHeight - 80) {
        this.navIsDark = true;
      } else {
        this.navIsDark = false;
      }
    },
  },
};
</script>

<style>
/* 1. Global Setup - Force the base background to white */
html,
body {
  margin: 0;
  padding: 0;
  background-color: #ffffff; /* Critical for mix-blend-mode */
}

:root {
  --ueno-orange: #ff4d00;
}

.ueno-nav {
  position: absolute;
  top: 0;
  width: 100%;
  padding: 40px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 850;
  box-sizing: border-box;
  transition: padding 0.4s ease;
}

.logo,
.nav-links a {
  text-decoration: none;
  color: #ffffff;
  font-family: "Inter", sans-serif;
  font-weight: 700;
  transition: color 0.4s ease, opacity 0.3s ease;
}

.ueno-nav.is-dark-text .logo,
.ueno-nav.is-dark-text .nav-links a {
  color: #000000;
}

.nav-links a {
  margin-left: 35px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  opacity: 0.8;
}

.nav-links a:hover {
  opacity: 0.5;
}

.nav-links a.router-link-active {
  opacity: 1;
  border-bottom: 2px solid;
}

/* Warp Bridge Logic */
.warp-bridge {
  position: fixed;
  inset: 0;
  background: white;
  z-index: 9999;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
}
.warp-bridge.active {
  opacity: 1;
}

@media (max-width: 768px) {
  .ueno-nav {
    padding: 30px 24px;
  }
  .nav-links a {
    margin-left: 15px;
    font-size: 0.6rem;
    letter-spacing: 1px;
  }
}
</style>
