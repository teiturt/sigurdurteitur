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
            Systems at DTU. I'm quite good at most things, but I do enjoy it
            when I'm not.
          </p>

          <!-- Context paragraph kept for internal linking -->
          <p class="reveal">
            After years of
            <router-link to="/experience" class="inline-link"
              >working</router-link
            >
            for companies along my studies. I'm completly sure that 9-5 is not
            for me. That's why I'm working on my
            <router-link to="/focus" class="inline-link">startup</router-link>
            to hopefully change the way we learn.
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
      choice: null,
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
    setChoice(val) {
      this.choice = val;
    },
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

/* 3. Media Narrative (Interactive) */
.media-narrative {
  padding: 80px 6% 60px;
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

/* --- INTERACTIVE TEXT STYLES --- */
.interaction-container {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  font-weight: 900;
  line-height: 1.1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}

.prefix {
  margin-bottom: 5px;
}

.choice-row {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  color: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  text-align: left;
  transition: all 0.3s ease;
  outline: none;
}

.checkbox {
  width: 0.8em;
  height: 0.8em;
  border: 3px solid #000;
  margin-right: 20px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  flex-shrink: 0;
  position: relative;
  top: 0.05em;
  background: transparent;
}

.check-icon {
  font-size: 0.5em;
  color: white;
  font-weight: 800;
}

.choice-row.active-green {
  color: #000;
  opacity: 1;
}
.choice-row.active-green .checkbox {
  background-color: #00b862;
  border-color: #00b862;
}

.choice-row.active-red {
  color: #ff3b30;
  animation: shake 0.4s ease-in-out;
}
.choice-row.active-red .checkbox {
  background-color: #ff3b30;
  border-color: #ff3b30;
}
.choice-row.active-red.muted {
  font-weight: 500;
}

.choice-row.dimmed {
  opacity: 0.3;
}

@keyframes shake {
  0%,
  100% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-5px);
  }
  75% {
    transform: translateX(5px);
  }
}

.pop-enter-active {
  animation: pop-in 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
@keyframes pop-in {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
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
  color: #ff4d00;
  border-bottom-color: #ff4d00;
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
  color: #ff4d00;
  border-color: #ff4d00;
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
.muted {
  color: #999;
  font-weight: 400;
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
  .interaction-container {
    font-size: clamp(2rem, 5vw, 3rem);
  }
  .checkbox {
    width: 0.7em;
    height: 0.7em;
    border-width: 2px;
    margin-right: 15px;
  }
}
</style>
