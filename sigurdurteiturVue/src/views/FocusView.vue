<template>
  <main class="ueno-focus">
    <header class="focus-hero" ref="container">
      <div class="label reveal">Current Focus</div>
      <h1 class="huge-title reveal">
        The <span class="serif">Future</span> of <br />Learning.
      </h1>
      <p class="intro-text reveal">
        I'm building SNAM, a math learning platform that adapts to each student,
        along with the neuro-symbolic system behind it that reads and
        understands handwritten work in real time.
      </p>
    </header>

    <!-- SECTION 01: THE STARTUP -->
    <section class="focus-section">
      <div class="section-meta reveal">
        <span class="num">01</span>
        <span class="tag">STARTUP / SNAM.IS</span>
      </div>

      <div class="content-grid">
        <!-- Part A: Main Narrative -->
        <div class="main-content reveal">
          <h2 class="project-name">
            SNAM: learning that adapts to the student.
          </h2>
          <p class="summary">
            A math learning platform that adapts to each student instead of
            forcing the student to adapt to it. It reads handwriting straight
            off the screen, maps exactly where the knowledge gaps are, and
            builds problems around what each student actually cares about.
          </p>
          <div class="tech-stack">
            <strong>Stack:</strong> Vue.js, Django, PostgreSQL.
          </div>
        </div>

        <!-- Part B: Individual Sidebar Items -->
        <div class="detail-sidebar">
          <div class="detail-item reveal">
            <h4>The Interface</h4>
            <p>
              Learning math should feel like writing on paper. The system reads
              handwriting straight off the screen, follows the process, and
              steps in only when the student asks.
            </p>
          </div>
          <div class="detail-item reveal">
            <h4>The Knowledge Engine</h4>
            <p>
              No blind jumps between chapters. A continuous knowledge graph maps
              where the gaps are and secures the foundation before moving on to
              harder material.
            </p>
          </div>
          <div class="detail-item reveal">
            <h4>The Content</h4>
            <p>
              Personalized word problems. Each one is built around the student's
              own interests, the context itself, not just the numbers.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 02: THE THESIS -->
    <section class="focus-section">
      <div class="section-meta reveal">
        <span class="num">02</span>
        <span class="tag">RESEARCH / M.SC. THESIS</span>
      </div>

      <div class="content-grid">
        <!-- Part A: Main Narrative -->
        <div class="main-content reveal">
          <h2 class="project-name">
            SNAM: a modular neuro-symbolic architecture for process-level
            analysis of handwritten mathematics.
          </h2>
          <p class="summary">
            A system that analyses handwritten math at the process level, giving
            detailed feedback instantly, not just right or wrong.
            <span class="principle">Symbolic where possible, neural where
            necessary.</span>
          </p>
          <div class="tech-stack">
            <strong>Core:</strong> CNN, LSTM, Python, JS, HPC.
          </div>
        </div>

        <!-- Part B: Individual Sidebar Items -->
        <div class="detail-sidebar">
          <div class="detail-item reveal">
            <h4>Perception</h4>
            <p>
              The perception pipeline classifies handwritten symbols with
              neural models, then reads their coordinates and spatial
              relationships to reconstruct the full mathematical expression.
            </p>
          </div>
          <div class="detail-item reveal">
            <h4>Symbolic Reasoning</h4>
            <p>
              A logic engine performs validation over a finite library of
              mathematical rules for deterministic step analysis.
            </p>
          </div>
          <div class="detail-item reveal">
            <h4>High Efficiency</h4>
            <p>
              The perception model reads around 100 expressions per second, and
              the symbolic engine handles 465,000 per second on a single core.
              Fast enough for instant feedback, cost effective enough to scale
              globally.
            </p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  name: "FocusView",
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      const targets = this.$el.querySelectorAll(".reveal");

      const observerOptions = {
        threshold: 0.15, // Lowered slightly so reveals feel more responsive when scrolling fast
      };

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
        // Batch elements already visible
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
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800;900&display=swap");

/* --- REVEAL SYSTEM --- */
.reveal {
  opacity: 0;
  transition: opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal.active {
  opacity: 1;
  /* Reduced delay slightly for a more "flowing" feel since there are more parts */
  transition-delay: 0.3s;
}

.reveal.active.initial-batch {
  transition-delay: 0.15s;
  transition-duration: 1.2s;
}

/* SIDE-BY-SIDE STAGGER: 
   When in wide view, we give the sidebar items a staggered delay 
   so they don't pop in at exactly the same time as the main block.
*/
@media (min-width: 1001px) {
  .detail-item:nth-child(1) {
    transition-delay: 0.5s;
  }
  .detail-item:nth-child(2) {
    transition-delay: 0.7s;
  }
  .detail-item:nth-child(3) {
    transition-delay: 0.9s;
  }
}

/* --- SNAM-FLAVORED LAYOUT --- */
.ueno-focus {
  --snam-blue: #2563eb;
  --snam-blue-light: #60a5fa;
  font-family: "Plus Jakarta Sans", sans-serif;
  background: #fdfdfd;
  padding: 180px 8% 200px;
  max-width: 1400px;
  margin: 0 auto;
  text-align: left;
  color: #111827;
  overflow-x: hidden;
}

.focus-hero {
  margin-bottom: 120px;
}

.label {
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--snam-blue);
  margin-bottom: 30px;
}

.huge-title {
  font-size: clamp(3.4rem, 6.5vw, 6.5rem);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.04em;
  margin-bottom: 40px;
}

/* hero highlight word: solid blue */
.serif {
  font-family: inherit;
  font-style: normal;
  font-weight: 900;
  color: var(--snam-blue);
}

.intro-text {
  font-size: clamp(1.2rem, 2.6vw, 1.8rem);
  line-height: 1.45;
  max-width: 900px;
  color: #6b7280;
  font-weight: 500;
}

.focus-section {
  padding: 90px 0;
  border-top: 1px solid #eef0f3;
}

.section-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 48px;
}

.num {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--snam-blue-light);
}

.tag {
  background: var(--snam-blue);
  color: white;
  padding: 6px 16px;
  border-radius: 9999px;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 1.5px;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: start;
}

.project-name {
  font-size: clamp(2.2rem, 3.5vw, 3rem);
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 28px;
  letter-spacing: -0.03em;
}

.summary {
  font-size: 1.3rem;
  line-height: 1.6;
  color: #4b5563;
  font-weight: 500;
  margin-bottom: 32px;
}

.tech-stack {
  font-size: 0.8rem;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  font-weight: 600;
}

.tech-stack strong {
  color: var(--snam-blue);
}

.principle {
  display: block;
  margin-top: 18px;
  color: #111827;
  font-weight: 800;
  font-style: italic;
}

.detail-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.detail-item {
  background: #fff;
  border: 1px solid #eef0f3;
  border-radius: 1.5rem;
  padding: 28px 30px;
  box-shadow: 0 12px 32px -18px rgba(17, 24, 39, 0.18);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.detail-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px -20px rgba(37, 99, 235, 0.28);
}

.detail-item h4 {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 12px;
  color: var(--snam-blue);
  font-weight: 800;
}

.detail-item p {
  font-size: 1.05rem;
  color: #6b7280;
  line-height: 1.55;
  font-weight: 500;
}

@media (max-width: 1000px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
</style>
