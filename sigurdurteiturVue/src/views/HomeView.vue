<template>
  <main class="ueno-home">
    <!-- HERO SECTION: The Space Identity -->
    <section class="hero-section">
      <SpaceToggle class="hero-bg" />
      <div class="hero-content">
        <h1 class="huge-title">
          Sigurður <br />
          <span class="serif">Teitur.</span>
        </h1>
        <p class="hero-subtitle">Software & Autonomous Systems</p>
      </div>
    </section>

    <!-- EXPERIENCE STRIP: Bleeding single-line layout -->
    <section class="experience-strip">
      <div class="label">Experience & Projects</div>
      <div class="overflow-wrapper">
        <div class="company-grid">
          <div class="company">NNE</div>
          <div class="company">Embla Medical</div>
          <div class="company">IRON HORSE</div>
          <div class="company">Showdeck</div>
          <div class="company">Biomedical</div>
          <div class="company">Research</div>
          <div class="company">Skatturinn</div>
          <div class="company">Teaching</div>
        </div>
      </div>
    </section>

    <!-- MEDIA SECTION: Video / Project Gallery -->
    <section class="media-narrative">
      <div class="media-container">
        <div class="video-placeholder">
          <div class="overlay-text">
            Visualizing <span class="serif">Automation</span>
          </div>
        </div>
      </div>

      <div class="media-description">
        <h2 class="serif">Performance.</h2>
        <p>
          I am driven by the intersection of humans and the technical world.
          From industrial robots to simple websites, I strive to deliver
          efficent solutions.
        </p>
        <router-link to="/experience" class="text-link"
          >View some projects →</router-link
        >
      </div>
    </section>

    <!-- FOOTER LINK -->
    <section class="home-footer">
      <router-link to="/contact" class="huge-footer-link">
        Let’s <span class="serif">Talk</span>
      </router-link>
    </section>
  </main>
</template>

<script>
import SpaceToggle from "../components/SpaceToggle.vue";

export default {
  name: "HomeView",
  components: { SpaceToggle },
};
</script>

<style scoped>
.ueno-home {
  background: #fff;
  text-align: left;
  overflow-x: hidden; /* Critical to prevent horizontal scroll on the whole page */
}

/* 1. Hero Section */
.hero-section {
  position: relative;
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  padding: 0 8%;
  color: #fff;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  pointer-events: none;
}

.huge-title {
  font-size: clamp(4rem, 15vw, 12rem);
  font-weight: 900;
  line-height: 0.8;
  letter-spacing: -6px;
  margin: 0;
}

.hero-subtitle {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-top: 40px;
  opacity: 0.6;
}

/* 2. Experience Strip - Single Line Bleed Effect */
.experience-strip {
  padding: 120px 0; /* Vertical padding only */
  background: #fff;
}

.label {
  padding-left: 8%; /* Align label with hero content */
  font-size: 0.75rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #999;
  margin-bottom: 60px;
}

.overflow-wrapper {
  width: 100%;
  overflow: visible; /* Let the grid run out of bounds */
  padding-left: 8%; /* Align starting company with label */
}

.company-grid {
  display: flex;
  flex-wrap: nowrap; /* Force everything on one line */
  gap: 100px; /* Large gaps for editorial feel */
  width: max-content; /* Container expands to fit all items */
}

.company {
  font-family: "Lora", serif;
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 400;
  color: #ddd; /* The lighter gray you liked */
  transition: color 0.3s, transform 0.3s;
  white-space: nowrap; /* Prevent names from breaking */
  cursor: default;
}

.company:hover {
  color: #000;
  transform: translateY(-5px);
}

/* 3. Media Narrative */
.media-narrative {
  padding: 100px 8% 200px;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 80px;
  align-items: center;
}

.video-placeholder {
  width: 100%;
  aspect-ratio: 16/9;
  background: #000;
  position: relative;
  overflow: hidden;
}

.overlay-text {
  position: absolute;
  bottom: 40px;
  left: 40px;
  color: #fff;
  font-size: 2rem;
  font-weight: 800;
}

.media-description h2 {
  font-size: 3.5rem;
  margin-bottom: 30px;
}

.media-description p {
  font-size: 1.4rem;
  line-height: 1.5;
  color: #555;
  margin-bottom: 40px;
}

.text-link {
  font-weight: 900;
  color: #000;
  text-decoration: none;
  border-bottom: 2px solid #000;
  padding-bottom: 5px;
}

/* 4. Footer Link */
.home-footer {
  padding-bottom: 200px;
  text-align: center;
}

.huge-footer-link {
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 900;
  text-decoration: none;
  color: #000;
  letter-spacing: -4px;
}

.huge-footer-link:hover {
  color: var(--ueno-orange, #ff4d00);
}

.serif {
  font-family: "Lora", serif;
  font-style: italic;
}

@media (max-width: 1000px) {
  .media-narrative {
    grid-template-columns: 1fr;
  }
  .experience-strip {
    padding-top: 80px;
  }
  .company-grid {
    gap: 60px; /* Slightly tighter on mobile */
  }
}
</style>
