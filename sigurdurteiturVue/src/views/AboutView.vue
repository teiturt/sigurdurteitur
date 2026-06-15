<template>
  <main class="ueno-letter-view">
    <div class="letter-container">
      <div class="letter-body" ref="container">
        <!-- INTRO -->
        <p class="reveal large-intro">Hi. I’m Teitur.</p>

        <p class="reveal">
          I’m 24, from Iceland, currently completing my M.Sc. in Autonomous
          Systems at DTU.
        </p>

        <p class="reveal">
          I've tried a lot of things. Plenty of them interesting, fewer that I
          could see myself doing for life. But software development and
          automation are the two I can genuinely imagine working on for the
          foreseeable future.
        </p>

        <p class="reveal">
          I'm at the end of my studies now, with just the thesis left to hand
          in. I'm ready for a break from academia and to put my skills to work
          in the real world. Whether that ends up being at a company I'd be
          proud to represent, or going all in on my startup to change how we
          learn, I'll be happy either way.
        </p>

        <p class="reveal">
          So yeah, excited to build solutions, fix my golf swing and move back
          to Iceland.
        </p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "AboutView",
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      const targets = this.$refs.container.querySelectorAll(".reveal");
      const observerOptions = { threshold: 0.15 };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      targets.forEach((el) => {
        const rect = el.getBoundingClientRect();
        // If it's already on screen at load, pop it in
        if (rect.top < window.innerHeight * 0.9) {
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
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap");

.ueno-letter-view {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  background-color: #ffffff;
  padding: 180px 30px 150px;
  box-sizing: border-box;
}

.letter-container {
  max-width: 680px;
  width: 100%;
  text-align: left;
}

/* GENERAL TYPOGRAPHY */
.letter-body p {
  font-family: "Lora", serif;
  font-size: clamp(1.2rem, 2.2vw, 1.6rem);
  font-weight: 500;
  line-height: 1.6;
  color: #000;
  margin-bottom: 1.5em;
  letter-spacing: -0.01em;
  -webkit-font-smoothing: antialiased;
}

.large-intro {
  font-size: clamp(2rem, 4vw, 3rem) !important;
  font-weight: 700 !important;
  margin-bottom: 40px !important;
}

.section-spacer {
  height: 60px; /* Gap before new sections */
}

.section-title {
  font-family: sans-serif;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 900;
  color: #999;
  margin-bottom: 20px;
  margin-top: 0;
}

.serif {
  font-style: italic;
  font-weight: 600;
  color: #000;
}

/* REVEAL ANIMATIONS */
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity 1.2s ease,
    transform 1.2s ease;
}

.reveal.active {
  opacity: 1;
  transform: translateY(0);
}

.reveal.active.initial-batch {
  transition-delay: 0.1s;
}

@media (max-width: 768px) {
  .ueno-letter-view {
    padding-top: 140px;
  }
  .section-spacer {
    height: 40px;
  }
}
</style>
