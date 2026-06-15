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
            <template v-for="n in 4" :key="'set1-' + n">
              <div class="company" v-for="c in companies" :key="c + n">
                {{ c }}
              </div>
            </template>
          </div>
          <div class="company-set" aria-hidden="true">
            <template v-for="n in 4" :key="'set2-' + n">
              <div
                class="company"
                v-for="c in companies"
                :key="c + n + '-copy'"
              >
                {{ c }}
              </div>
            </template>
          </div>
        </div>
      </div>
    </section>

    <!-- ABOUT SUMMARY -->
    <section class="home-about-summary">
      <div class="centered-content">
        <div class="label centered reveal">About me</div>

        <div class="about-text-wrapper">
          <!-- UPDATED INTRO TEXT -->
          <p class="reveal">
            I’m 24, from Iceland, currently completing my M.Sc. in Autonomous
            Systems at DTU.
          </p>

          <!-- Context paragraph kept for internal linking -->
          <p class="reveal">
            I've tried a lot of things, but software development and automation
            are the two I keep coming back to. After years of
            <router-link to="/experience" class="inline-link"
              >working</router-link
            >
            for companies and building projects alongside my studies, I'm
            wrapping up my degree and ready to step out of academia and put my
            skills to work, whether that's with a team I'd be glad to join or on
            my own
            <router-link to="/focus" class="inline-link">startup</router-link>.
          </p>

          <!-- READ MORE BUTTON -->
          <div class="reveal read-more-wrapper">
            <router-link to="/about" class="full-story-link">
              Read full story <span class="arrow">&rarr;</span>
            </router-link>
          </div>
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
        { threshold: 0.15 },
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

/* 2. Experience Strip */
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
  animation: slide-left 120s linear infinite;
}

.company-set {
  display: flex;
  align-items: center;
  gap: clamp(30px, 6vw, 100px);
  padding-right: clamp(30px, 6vw, 100px);
  padding-left: var(--side-padding);
}

.company {
  font-family: "Lora", serif;
  font-size: clamp(1.5rem, 4vw, 3.2rem);
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

/* 4. About Summary */
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

/* LINKS */
.inline-link {
  color: #000;
  font-weight: 700;
  text-decoration: none;
  border-bottom: 2px solid #ddd;
  transition: all 0.3s ease;
}
.inline-link:hover {
  color: #000000;
  border-bottom-color: #000000;
}

/* Full Story Link */
.read-more-wrapper {
  margin-top: 30px;
}
.full-story-link {
  display: inline-flex;
  align-items: center;
  font-family: "Inter", sans-serif;
  font-weight: 900;
  font-size: 1.1rem;
  color: #000;
  text-decoration: none;
  border-bottom: 3px solid #000;
  padding-bottom: 4px;
  transition: all 0.3s ease;
}
.full-story-link:hover {
  color: #000000;
  border-color: #000000;
}
.arrow {
  margin-left: 8px;
  transition: transform 0.3s ease;
}
.full-story-link:hover .arrow {
  transform: translateX(5px);
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
</style>
