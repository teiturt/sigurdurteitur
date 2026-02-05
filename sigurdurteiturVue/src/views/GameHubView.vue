<template>
  <main class="ueno-playroom">
    <!-- Hero Header (Static) -->
    <header class="playroom-hero">
      <div class="label">Experiments & Prototypes</div>
      <h1 class="huge-title">The <span class="serif">Playroom.</span></h1>
      <p class="intro-text">
        A collection of interactive experiments, simulations, and creative
        coding projects.
      </p>
    </header>

    <div class="game-list">
      <!-- Entry 01: Void Pilot -->
      <router-link to="/games/void-pilot" class="game-entry">
        <div class="entry-meta">
          <span class="num">01</span>
          <span class="status-tag">ACTIVE MISSION</span>
        </div>

        <div class="entry-content">
          <div class="text-side">
            <h2 class="game-title">Void Pilot</h2>
            <p class="game-desc">
              An immersive 1st-person space flight simulator. Navigate through
              deep space hoops while managing energy and fuel consumption. Built
              with a custom 3D canvas engine and deterministic physics.
            </p>
            <div class="launch-hint">Initiate Launch →</div>
          </div>

          <div class="visual-side">
            <!-- Only the media box has the 'reveal' class -->
            <div class="preview-box void-pilot-preview reveal">
              <div class="cockpit-glimmer"></div>
            </div>
          </div>
        </div>
      </router-link>

      <!-- Entry 02: TeiturBoy Console (NEW) -->
      <router-link to="/games/console" class="game-entry">
        <div class="entry-meta">
          <span class="num">02</span>
          <!-- Changed status to ONLINE -->
          <span class="status-tag online">SYSTEM ONLINE</span>
        </div>
        <div class="entry-content">
          <div class="text-side">
            <h2 class="game-title">Pocket System</h2>
            <p class="game-desc">
              A virtual handheld console emulator running entirely in the
              browser. Features classic algorithm implementations (Snake) and a
              reactive control system that supports both touch and keyboard
              input.
            </p>
            <div class="launch-hint">Power On →</div>
          </div>
          <div class="visual-side">
            <!-- New CSS Art for the Preview -->
            <div class="preview-box console-preview reveal">
              <div class="mini-screen">
                <div class="snake-pixel"></div>
              </div>
              <div class="mini-dpad"></div>
              <div class="mini-btns"></div>
            </div>
          </div>
        </div>
      </router-link>

      <router-link to="/games/day-guesser" class="game-entry">
        <div class="entry-meta">
          <span class="num">03</span>
          <span class="status-tag online">LEARNING MODULE</span>
        </div>
        <div class="entry-content">
          <div class="text-side">
            <h2 class="game-title">The Autistico</h2>
            <p class="game-desc">
              Master the "Doomsday Algorithm" using Conway's 12-Method. Learn to
              calculate the weekday of any date in history mentally. Features
              the rules, stepwise practice, and a speed test mode (it's
              humbling).
            </p>
            <div class="launch-hint">Open Manual →</div>
          </div>
          <div class="visual-side">
            <div class="preview-box savant-preview reveal">
              <!-- CSS Art: A flipping calendar page -->
              <div class="calendar-page">
                <div class="cal-header"></div>
                <div class="cal-body">
                  <span class="cal-num">12</span>
                </div>
                <div class="cal-corner"></div>
              </div>
            </div>
          </div>
        </div>
      </router-link>

      <!-- Entry 02: Future Experiment -->
      <div class="game-entry disabled">
        <div class="entry-meta">
          <span class="num">02</span>
          <span class="status-tag locked">CLASSIFIED</span>
        </div>
        <div class="entry-content">
          <div class="text-side">
            <h2 class="game-title">Neuro-Symbolic Visualizer</h2>
            <p class="game-desc">
              Upcoming experiment: A real-time visualization of knowledge graph
              traversals and symbolic reasoning paths.
            </p>
          </div>
          <div class="visual-side">
            <!-- Placeholder for future reveal -->
            <div class="preview-box reveal placeholder-preview"></div>
          </div>
        </div>
      </div>
    </div>

    <footer class="playroom-footer">
      <p>More experiments coming soon.</p>
    </footer>
  </main>
</template>

<script>
export default {
  name: "GameHubView",
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      // We only target the visual elements
      const targets = this.$el.querySelectorAll(".reveal");

      const observerOptions = {
        threshold: 0.2, // Trigger reveal when 20% of the image is visible
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
        // If it's already on screen at load, show it after a tiny delay
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
/* --- REVEAL STYLES (Only for Media) --- */
.reveal {
  opacity: 0;
  /* Using a slow, elegant fade with no movement */
  transition: opacity 1.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal.active {
  opacity: 1;
}

/* On initial load, wait for the page to 'settle' before showing the images */
.reveal.active.initial-batch {
  transition-delay: 0.3s;
}

/* On scroll, use a slightly longer delay so the user sees the reveal */
.reveal.active:not(.initial-batch) {
  transition-delay: 0.1s;
}

/* --- EXISTING LAYOUT STYLES --- */
.ueno-playroom {
  padding: 180px 10% 100px;
  max-width: 1400px;
  margin: 0 auto;
  text-align: left;
  background: white;
}

.playroom-hero {
  margin-bottom: 120px;
}

.label {
  font-size: 0.8rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--ueno-orange);
  margin-bottom: 30px;
}

.huge-title {
  font-size: clamp(3.4rem, 6.5vw, 6.5rem);
  font-weight: 900;
  letter-spacing: -4px;
  line-height: 0.9;
  margin-bottom: 40px;
}

.serif {
  font-family: "Playfair Display", serif;
  font-style: italic;
  font-weight: 700;
}

.intro-text {
  font-size: clamp(1.2rem, 3vw, 2rem);
  line-height: 1.3;
  max-width: 800px;
  color: #333;
}

.game-list {
  border-top: 1px solid #eee;
}

.game-entry {
  display: block;
  text-decoration: none;
  color: inherit;
  padding: 80px 0;
  border-bottom: 1px solid #eee;
}

.game-entry.disabled {
  opacity: 0.3;
  cursor: default;
}

.entry-meta {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
}

.num {
  font-family: "Playfair Display", serif;
  font-size: 1.5rem;
  font-style: italic;
  color: #ccc;
}

.status-tag {
  font-size: 0.7rem;
  font-weight: 900;
  letter-spacing: 1px;
  color: var(--ueno-orange);
  border: 1px solid var(--ueno-orange);
  padding: 3px 10px;
}

.status-tag.locked {
  color: #999;
  border-color: #999;
}

.entry-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.game-title {
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 900;
  letter-spacing: -2px;
  margin-bottom: 20px;
  text-transform: uppercase;
}

.game-desc {
  font-size: 1.2rem;
  line-height: 1.5;
  color: #555;
  margin-bottom: 30px;
  max-width: 500px;
}

.launch-hint {
  font-weight: 900;
  text-transform: uppercase;
  font-size: 0.8rem;
  letter-spacing: 2px;
  color: black;
  transition: color 0.3s, transform 0.3s;
}

.visual-side {
  position: relative;
}

.preview-box {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #050505;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.8s ease;
}

.placeholder-preview {
  background: #f7f7f7;
}

.void-pilot-preview {
  background: radial-gradient(circle at center, #111 0%, #000 100%);
  border: 1px solid #222;
}

.game-entry:hover .preview-box {
  transform: scale(1.02) rotate(1deg);
}

.game-entry:hover .launch-hint {
  color: var(--ueno-orange);
  transform: translateX(10px);
}

.cockpit-glimmer {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 2px;
  height: 2px;
  background: white;
  box-shadow: 0 0 40px 20px rgba(0, 242, 255, 0.1);
  border-radius: 50%;
}

.status-tag.online {
  color: #8bac0f;
  border-color: #8bac0f;
}

.console-preview {
  background: #c0c0c0; /* Grey plastic */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}

/* The Grey Screen Bezel */
.mini-screen {
  width: 50%;
  height: 40%;
  background: #555;
  border-radius: 4px 4px 15px 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
}

/* The Green LCD */
.mini-screen::after {
  content: "";
  width: 80%;
  height: 80%;
  background: #8bac0f; /* Retro Green */
  box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.5);
}

/* The Controls */
.mini-dpad {
  width: 40px;
  height: 40px;
  background: #333;
  clip-path: polygon(
    33% 0,
    66% 0,
    66% 33%,
    100% 33%,
    100% 66%,
    66% 66%,
    66% 100%,
    33% 100%,
    33% 66%,
    0 66%,
    0 33%,
    33% 33%
  );
  position: absolute;
  bottom: 15%;
  left: 20%;
}

.mini-btns {
  width: 12px;
  height: 12px;
  background: #b01050;
  border-radius: 50%;
  position: absolute;
  bottom: 20%;
  right: 25%;
  box-shadow: -18px 5px 0 #b01050; /* Creates the second button using shadow */
}

/* Hover Effect */
.game-entry:hover .mini-screen::after {
  background: #9bbc0f; /* Brighter green on hover */
  box-shadow: 0 0 15px #9bbc0f;
}

@media (max-width: 1000px) {
  .entry-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .visual-side {
    order: -1;
  }
}

.playroom-footer {
  padding-top: 100px;
  color: #999;
  font-size: 0.9rem;
  text-align: center;
}

/* --- SAVANT (CALENDAR) PREVIEW --- */
.savant-preview {
  background: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.calendar-page {
  width: 100px;
  height: 120px;
  background: white;
  border-radius: 6px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.cal-header {
  height: 25%;
  background: #ff4444;
  width: 100%;
}

.cal-body {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cal-num {
  font-family: "Playfair Display", serif;
  font-size: 3rem;
  font-weight: 700;
  color: #333;
}

/* The page peel effect */
.cal-corner {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 0 30px 30px;
  border-color: transparent transparent #ccc transparent;
  box-shadow: -2px -2px 5px rgba(0, 0, 0, 0.1);
}

.game-entry:hover .calendar-page {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
</style>
