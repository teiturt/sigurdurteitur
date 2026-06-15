<template>
  <div id="app">
    <!-- 1. We apply a dynamic class 'is-dark-text' based on our script -->
    <nav
      class="ueno-nav"
      :class="{ 'is-dark-text': navIsDark, 'menu-open': menuOpen }"
      v-if="showNav"
    >
      <router-link to="/" class="logo">S.T.T</router-link>
      <button
        class="menu-toggle"
        @click="menuOpen = !menuOpen"
        :aria-expanded="menuOpen"
        aria-label="Toggle menu"
      >
        <span></span><span></span><span></span>
      </button>
      <div class="nav-links" :class="{ open: menuOpen }">
        <router-link to="/about">About</router-link>
        <router-link to="/experience">CV</router-link>
        <router-link to="/focus">Focus</router-link>
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
      menuOpen: false,
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
        this.menuOpen = false;
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
  --ueno-accent: #000000;
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

/* Hamburger toggle (hidden on desktop) */
.menu-toggle {
  display: none;
  position: relative;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  width: 32px;
  height: 32px;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 860;
}
.menu-toggle span {
  display: block;
  width: 26px;
  height: 2px;
  background: #fff;
  transition: transform 0.3s ease, opacity 0.3s ease, background 0.4s ease;
}
.ueno-nav.is-dark-text .menu-toggle span {
  background: #000;
}

@media (max-width: 768px) {
  .ueno-nav {
    padding: 24px;
  }
  .menu-toggle {
    display: flex;
  }
  /* morph bars into an X when open */
  .ueno-nav.menu-open .menu-toggle span:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
  }
  .ueno-nav.menu-open .menu-toggle span:nth-child(2) {
    opacity: 0;
  }
  .ueno-nav.menu-open .menu-toggle span:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
  }

  /* full-screen overlay menu */
  .nav-links {
    position: fixed;
    inset: 0;
    background: #000;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 32px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.35s ease;
  }
  .ueno-nav.is-dark-text .nav-links {
    background: #fff;
  }
  .nav-links.open {
    opacity: 1;
    pointer-events: auto;
  }
  .nav-links a {
    margin-left: 0;
    font-size: 1.4rem;
    letter-spacing: 2px;
    opacity: 1;
  }
}
</style>
