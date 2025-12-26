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
        <p class="hero-subtitle">I'm a Software Developer</p>
      </div>
    </section>

    <!-- EXPERIENCE STRIP -->
    <section class="experience-strip">
      <div class="label">Experience & Projects</div>
      <div class="marquee-wrapper">
        <div class="marquee-content">
          <div class="company-set">
            <div class="company" v-for="c in companies" :key="c">{{ c }}</div>
          </div>
          <div class="company-set" aria-hidden="true">
            <div class="company" v-for="c in companies" :key="c + '2'">
              {{ c }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MEDIA SECTION: Balanced Margins -->
    <section class="media-narrative">
      <div class="media-visual">
        <div class="video-container">
          <video autoplay muted loop playsinline class="project-video">
            <source src="@/assets/DependableSystems.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <div class="overlay-text">
            This is <span class="serif">Newton</span>
          </div>
        </div>
      </div>

      <div class="media-description">
        <h2 class="serif"><span class="muted">Why</span> Automate?</h2>
        <p>
          I'm great at having fun and horrible at doing boring tasks. So I
          automate the tasks. From industrial robots to simple scripts, I love
          making life easier.
        </p>
        <router-link to="/experience" class="text-link"
          >View some projects →</router-link
        >
      </div>
    </section>

    <!-- CENTERED ABOUT SUMMARY -->
    <section class="home-about-summary">
      <div class="centered-content">
        <div class="label centered">The Story</div>
        <h2 class="about-title reveal">
          Logic first, <br />
          <span class="serif">everything else second.</span>
        </h2>

        <div class="about-text-wrapper">
          <p class="reveal">
            I’m a software developer and M.Sc. student at
            <span class="highlight">DTU</span>
            specializing in Autonomous Systems. I don’t just write code; I
            design systems that move, perceive, and act in the real world.
          </p>
          <p class="reveal">
            I’ve realized that the traditional 9–5 grind, where the reward for
            good work is often just more work, isn’t for me. I’m great at what I
            love, and I’m ready to spend my life getting rid of the boring
            stuff.
          </p>
          <router-link to="/about" class="text-link reveal"
            >Read the full story →</router-link
          >
        </div>
      </div>
    </section>

    <div class="bottom-buffer"></div>
  </main>
</template>

<script>
import SpaceToggle from "../components/SpaceToggle.vue";

export default {
  name: "HomeView",
  components: { SpaceToggle },
  data() {
    return {
      companies: [
        "SNAM.IS",
        "NNE",
        "Embla Medical",
        "Showdeck",
        "Reykjavik University",
        "Skatturinn",
        "DTU",
      ],
    };
  },
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
  padding: 0 12%;
  color: #fff;
  background: #000;
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

/* 2. Experience Strip */
.experience-strip {
  padding: 120px 0 40px;
  background: #fff;
  pointer-events: none;
}
.label {
  padding-left: 12%;
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
  animation: slide-left 40s linear infinite;
}
.company-set {
  display: flex;
  align-items: center;
  gap: 100px;
  padding-left: 12%;
  padding-right: 100px;
}
.company {
  font-family: "Lora", serif;
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 400;
  color: #ddd;
  white-space: nowrap;
}

@keyframes slide-left {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-50%);
  }
}

/* 3. Media Narrative: Balanced Margins */
.media-narrative {
  /* Using 6% side padding makes it wider than text (12%) but prevents edge-to-edge */
  padding: 100px 6% 80px;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr; /* Slightly asymmetric for interest */
  gap: 60px;
  align-items: center;
}

.video-container {
  width: 100%;
  aspect-ratio: 16/9;
  background: #000;
  position: relative;
  overflow: hidden;
  border-radius: 4px;
}

.project-video {
  width: 100%;
  height: 100%;
  object-fit: cover; /* This makes the video fill the area like a background image */
  display: block;
}

.overlay-text {
  position: absolute;
  bottom: 30px;
  left: 30px;
  color: #fff;
  font-size: 1.5rem;
  font-weight: 800;
  opacity: 0.8;
}

.media-description {
  /* This ensures the text stays perfectly aligned with the 12% markers of the page */
  padding-right: 8%;
}

.media-description h2 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 30px;
  line-height: 1;
}
.muted {
  color: #999;
  font-weight: 400;
}
.media-description p {
  font-size: 1.4rem;
  line-height: 1.5;
  color: #555;
  margin-bottom: 40px;
}

/* 4. Centered About Summary */
.home-about-summary {
  padding: 120px 12%;
  border-top: 1px solid #eee;
  background: #fff;
  display: flex;
  justify-content: center;
}

.centered-content {
  max-width: 800px;
  width: 100%;
  text-align: center;
}

.label.centered {
  padding-left: 0;
  margin-bottom: 40px;
}
.about-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -2px;
  margin-bottom: 60px;
}

.about-text-wrapper {
  text-align: left;
  max-width: 600px;
  margin: 0 auto;
}
.about-text-wrapper p {
  font-family: "Lora", serif;
  font-size: 1.5rem;
  line-height: 1.4;
  color: #333;
  margin-bottom: 30px;
}

.highlight {
  color: #ff4d00;
  font-weight: 700;
}

/* 5. Utility Styles */
.text-link {
  font-weight: 900;
  color: #000;
  text-decoration: none;
  border-bottom: 2px solid #000;
  padding-bottom: 5px;
  transition: color 0.3s, border-color 0.3s;
}
.text-link:hover {
  color: #ff4d00;
  border-color: #ff4d00;
}
.serif {
  font-family: "Lora", serif;
  font-style: italic;
}
.bottom-buffer {
  height: 100px;
}

/* 6. Responsive Adjustments */
@media (max-width: 1024px) {
  .media-narrative {
    grid-template-columns: 1fr;
    padding: 60px 8%;
    gap: 40px;
  }
  .media-description {
    padding-right: 0;
  }
}

@media (max-width: 768px) {
  .video-placeholder {
    aspect-ratio: 16/9;
  }
  .about-title {
    font-size: 2.2rem;
  }
  .about-text-wrapper p {
    font-size: 1.2rem;
  }
}
</style>
