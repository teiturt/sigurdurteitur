<template>
  <main class="ueno-letter-view">
    <div class="letter-container">
      <div class="letter-body" ref="container">
        <!-- INTRO -->
        <p class="reveal large-intro">Hi. I’m Teitur.</p>

        <p class="reveal">
          I’m 24, from Iceland, and currently completing my M.Sc. in Autonomous
          Systems at DTU. I’m a fierce believer in merit-based success. I might
          forget a doctor's appointment, but I can tell you exactly how to
          optimize a robot's path through a factory.
        </p>

        <!-- SECTION 1: Physics/Math -->
        <div class="section-spacer"></div>
        <h3 class="reveal section-title">Architecture over Arithmetic</h3>
        <p class="reveal">
          Early on I realized I had a knack for logic but a strong distaste for
          meaningless memorization. The contrast is extreme. In my first
          semester I received a below-average score in a pure math final, yet I
          finished my Physics final an hour early with a perfect score. The
          average that year was 4.8 out of 10.
        </p>
        <p class="reveal">
          Physics is about the <span class="serif">logic of the solution</span>,
          not the trivial calculation steps. That is why I love it.
        </p>

        <!-- SECTION 2: Programming -->
        <div class="section-spacer"></div>
        <h3 class="reveal section-title">The Feedback Loop</h3>
        <p class="reveal">
          When I started programming I found that same logic but with something
          even better. Immediate feedback. I loved that you could build complex
          systems and see the results instantly. It’s only you and the code. You
          don’t need obscene amounts of money for physical tests or months of
          waiting for hardware parts. You can just build, test, and iterate. I
          thrived in my programming classes because they fit my brain’s need for
          speed.
        </p>

        <!-- SECTION 3: The Innovation Story -->
        <div class="section-spacer"></div>
        <h3 class="reveal section-title">The Innovation Paradox</h3>
        <p class="reveal">
          This divide defines my journey. I have failed exactly two courses in
          my life. "Innovation" in high school and "Innovation" in my Master's.
          Even though the pass rate was 99% and I genuinely love innovation, the
          classes felt poorly taught and the assignments felt pointless. I ended
          up forgetting to even submit them.
        </p>
        <p class="reveal">
          Compare that to my B.Sc. in Computer Science where I ended up on the
          Dean’s List because my grades were in the top 1%. It’s a crazy
          contrast but it proves a simple truth.
          <span class="serif"
            >I am bad at what I don't want to do, and great at what I
            love.</span
          >
        </p>

        <!-- SECTION 4: Hardware/Future -->
        <div class="section-spacer"></div>
        <h3 class="reveal section-title">Hardware vs Software</h3>
        <p class="reveal">
          For my B.Sc. thesis we built an AMR for Marel. Dealing with hardware
          delays and wobbly motors confirmed my path. While I love working on
          the navigation logic and UX I hate the friction of hardware. Hardware
          takes months to ship. Software takes a day to deploy.
        </p>
        <p class="reveal">
          I recently received a startup grant to start building an education
          platform. I'm excited because it gives me an opportunity to fix an
          education system which is far from ideal.
        </p>
        <p class="reveal">
          I’m ready to spend my life focusing on what I want to do. And right
          now, that means fixing education.
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
