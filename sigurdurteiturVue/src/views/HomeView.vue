<template>
  <main class="ueno-home">
    <!-- HERO SECTION -->
    <section class="hero-section">
      <SpaceToggle class="hero-bg" />
      <div class="hero-content">
        <h1 class="huge-title">
          Sigurður <br />
          <span class="serif second-line">Teıtur</span>
        </h1>
        <p class="hero-subtitle">Autonomous Systems</p>
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

    <!-- MEDIA SECTION: Tightened Pacing -->
    <section class="media-narrative">
      <div class="media-visual">
        <div class="video-container reveal">
          <video autoplay muted loop playsinline class="project-video">
            <source src="@/assets/DependableSystems.mp4" type="video/mp4" />
          </video>
          <div class="overlay-text">
            This is <span class="serif">Newton</span>
          </div>
        </div>
      </div>

      <div class="media-description">
        <h2 class="serif reveal">
          I choose Autonomous workflows<br />
          <span class="muted">over manual bottlenecks.</span>
        </h2>
      </div>
    </section>

    <!-- CENTERED ABOUT SUMMARY: Simplified and Re-labeled -->
    <section class="home-about-summary">
      <div class="centered-content">
        <!-- Re-labeled as requested -->
        <div class="label centered reveal">About me</div>

        <div class="about-text-wrapper">
          <p class="reveal">
            I'm a software developer and M.Sc. student at
            <router-link to="/about" class="inline-link">DTU</router-link>
            specializing in Autonomous Systems. I don’t just write code; I
            design systems that move, perceive, and act in the real world.
          </p>
          <p class="reveal">
            After years of work and creating solutions for companies like
            <router-link to="/experience" class="inline-link"
              >Embla Medical</router-link
            >, I’ve realized that the reward for good work shouldn't just be
            more work. I'm currently building
            <router-link to="/focus" class="inline-link">SNAM.is</router-link>
            to change how we learn, and spending the rest of my time
            <router-link to="/games" class="inline-link">playing</router-link>
            around.
          </p>
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
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      const targets = this.$el.querySelectorAll(".reveal");
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("active");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.15 }
      );

      targets.forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.85) {
          el.classList.add("active", "initial-batch");
        } else {
          observer.observe(el);
        }
      });
    },
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

/* 2. Experience Strip - Tightened padding */
.experience-strip {
  padding: 80px 0 40px;
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
  margin-bottom: 40px;
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

/* 3. Media Narrative - Tightened Pacing */
.media-narrative {
  padding: 80px 6% 60px; /* Reduced bottom padding to draw in the summary */
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 80px;
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
  object-fit: cover;
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
  padding-right: 8%;
}
.media-description h2 {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  font-weight: 900;
  margin-bottom: 0;
  line-height: 1.1;
}
.media-description h2 .muted {
  color: #999;
  font-weight: 400;
  display: block;
  margin-top: 10px;
}

/* 4. Manifesto Section - Reduced top padding to make it part of the same flow */
.home-about-summary {
  padding: 80px 12% 120px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: center;
}
.centered-content {
  max-width: 900px;
  width: 100%;
  text-align: center;
}
.label.centered {
  padding-left: 0;
  margin-bottom: 40px;
}

.about-text-wrapper {
  text-align: left;
  max-width: 750px;
  margin: 0 auto;
}
.about-text-wrapper p {
  font-family: "Lora", serif;
  font-size: clamp(1.4rem, 2.5vw, 1.9rem);
  font-weight: 500;
  line-height: 1.45;
  color: #000;
  margin-bottom: 1.2em;
}

/* NARRATIVE NAVIGATION LINKS */
.inline-link {
  color: #000;
  font-weight: 700;
  text-decoration: none;
  border-bottom: 2px solid #ddd;
  transition: all 0.3s ease;
}
.inline-link:hover {
  color: #ff4d00;
  border-bottom-color: #ff4d00;
}
.full-story-link {
  font-weight: 900;
  color: #000;
  text-decoration: none;
  border-bottom: 3px solid #000;
  padding-bottom: 5px;
  font-size: 1.1rem;
  transition: 0.3s;
}
.full-story-link:hover {
  color: #ff4d00;
  border-color: #ff4d00;
}

/* REVEAL SYSTEM */
.reveal {
  opacity: 0;
  transition: opacity 2s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.active {
  opacity: 1;
  transition-delay: 0.4s;
}
.reveal.active.initial-batch {
  transition-delay: 0.2s;
  transition-duration: 1.5s;
}

.serif {
  font-family: "Lora", serif;
  font-style: italic;
}
.second-line {
  margin-top: 0.08em;
  display: inline-block;
  font-weight: 400;
}
.bottom-buffer {
  height: 100px;
}

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
</style>
