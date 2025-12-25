<template>
  <main class="ueno-home">
    <!-- HERO SECTION -->
    <section class="hero-section">
      <SpaceToggle class="hero-bg" />
      <div class="hero-content">
        <h1 class="huge-title">
          Sigurður <br />
          <span class="serif second-line">Teıtur.</span>
        </h1>
        <p class="hero-subtitle">Software & Autonomous Systems</p>
      </div>
    </section>

    <!-- EXPERIENCE STRIP: Infinite Marquee -->
    <section class="experience-strip">
      <div class="label">Experience & Projects</div>

      <div class="marquee-wrapper">
        <!-- We duplicate the list to create the infinite loop -->
        <div class="marquee-content">
          <!-- First Set -->
          <div class="company-set">
            <div class="company">SNAM.IS</div>
            <div class="company">NNE</div>
            <div class="company">Embla Medical</div>
            <div class="company">Showdeck</div>
            <div class="company">Reykjavik University</div>
            <div class="company">Skatturinn</div>
            <div class="company">DTU</div>
          </div>
          <!-- Second Set (Identical) -->
          <div class="company-set" aria-hidden="true">
            <div class="company">SNAM.IS</div>
            <div class="company">NNE</div>
            <div class="company">Embla Medical</div>
            <div class="company">Showdeck</div>
            <div class="company">Reykjavik University</div>
            <div class="company">Skatturinn</div>
            <div class="company">DTU</div>
          </div>
        </div>
      </div>
    </section>

    <!-- MEDIA SECTION -->
    <section class="media-narrative">
      <div class="media-container">
        <div class="video-placeholder">
          <div class="overlay-text">
            Visualizing <span class="serif">Automation</span>
          </div>
        </div>
      </div>

      <div class="media-description">
        <h2 class="serif"><span class="muted">Why</span> Automate?</h2>
        <p>
          I'm great at having fun and horrible at doing boring tasks. So I just
          automate the tasks. From industrial robots to simple scripts, I love
          making life easier.
        </p>
        <router-link to="/experience" class="text-link"
          >View some projects →</router-link
        >
      </div>
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
  overflow-x: hidden;
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
  font-size: clamp(4rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  margin: 0;
}

.hero-subtitle {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-top: 40px;
  opacity: 0.6;
}

/* 2. Experience Strip - Infinite Marquee Styles */
.experience-strip {
  padding: 120px 0;
  background: #fff;
  pointer-events: none; /* Disable all interactions/hover as requested */
  user-select: none; /* Prevent text selection while sliding */
}

.label {
  padding-left: 8%;
  font-size: 0.75rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #2d2b2b;
  margin-bottom: 60px;
}

.marquee-wrapper {
  overflow: hidden;
  width: 100%;
  display: flex;
}

.marquee-content {
  display: flex;
  width: max-content;
  /* Adjust the '40s' to make the slide faster or slower */
  animation: slide-left 40s linear infinite;
}

.company-set {
  display: flex;
  align-items: center;
  gap: 100px; /* Space between company names */
  padding-right: 100px; /* Matches the gap for seamless transition */
}

.company {
  font-family: "Lora", serif;
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 400;
  color: #888;
  white-space: nowrap;
}

@keyframes slide-left {
  0% {
    transform: translateX(0);
  }
  100% {
    /* Moves the entire content by exactly half (one full set of companies) */
    transform: translateX(-50%);
  }
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

/* This makes 'Why' disappear into the background slightly */
.muted {
  color: #999;
  font-weight: 400; /* Optional: make it slightly thinner than 'Automate?' */
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
  .company-set {
    gap: 60px;
    padding-right: 60px;
  }
}
</style>
