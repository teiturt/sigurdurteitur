<template>
  <main class="ueno-letter-view">
    <div class="letter-container">
      <div class="letter-body" ref="container">
        <!-- INTRO -->
        <p class="reveal large-intro">Hi. I’m Teitur.</p>

        <p class="reveal">
          I’m 24, from Iceland, currently completing my M.Sc. in Autonomous
          Systems at DTU. I'm quite good at most things, but I do enjoy it when
          I'm not.
        </p>

        <p class="reveal">
          I don't really know what to say, do I do a life story, do I just talk
          about my projects, or do I tell you about the time I almost broke my
          skull? I don't know so I'll just write it down once I've figured it
          out.
        </p>
        <p class="reveal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in culpa qui
          officia deserunt mollit anim id est laborum.
        </p>

        <p class="reveal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        </p>

        <p class="reveal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p class="reveal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        </p>

        <p class="reveal">
          I'll always do what I want to do, and right now that means fixing
          education.
        </p>

        <p class="reveal">
          And then maybe also golf, football, skiing, friends, family, finding
          love. The important stuff.
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
  transition: opacity 1.2s ease, transform 1.2s ease;
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
