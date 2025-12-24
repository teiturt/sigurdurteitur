<template>
  <main class="ueno-playroom">
    <!-- Hero Header -->
    <header class="playroom-hero">
      <div class="label">Experiments & Prototypes</div>
      <h1 class="huge-title">The <span class="serif">Playroom.</span></h1>
      <p class="intro-text">
        A collection of high-performance interactive experiments, 1st-person
        simulations, and creative coding projects built to push the limits of
        the browser.
      </p>
    </header>

    <!-- Game Selection List -->
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
            <div class="preview-box void-pilot-preview">
              <!-- This represents where a screenshot or mini-animation would go -->
              <div class="cockpit-glimmer"></div>
            </div>
          </div>
        </div>
      </router-link>

      <!-- Entry 02: Future Experiment Placeholder -->
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
        </div>
      </div>
    </div>

    <!-- Professional Footer -->
    <footer class="playroom-footer">
      <p>More experiments coming soon.</p>
    </footer>
  </main>
</template>

<style scoped>
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
  font-size: clamp(3.5rem, 10vw, 8rem);
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

/* Game Entry List Styles */
.game-list {
  border-top: 1px solid #eee;
}

.game-entry {
  display: block;
  text-decoration: none;
  color: inherit;
  padding: 80px 0;
  border-bottom: 1px solid #eee;
  transition: background 0.4s ease;
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

/* Visual Side / Thumbnail */
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
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.void-pilot-preview {
  background: radial-gradient(circle at center, #111 0%, #000 100%);
  border: 1px solid #222;
}

/* Hover Effects */
.game-entry:hover .preview-box {
  transform: scale(1.02) rotate(1deg);
}

.game-entry:hover .launch-hint {
  color: var(--ueno-orange);
  transform: translateX(10px);
}

/* Cockpit decorative glimmer */
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

@media (max-width: 1000px) {
  .entry-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .visual-side {
    order: -1; /* Move image above text on mobile */
  }
}

.playroom-footer {
  padding-top: 100px;
  color: #999;
  font-size: 0.9rem;
  text-align: center;
}
</style>
