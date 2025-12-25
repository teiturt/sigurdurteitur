<template>
  <main class="ueno-focus">
    <header class="focus-hero">
      <div class="label">Current Focus</div>
      <h1 class="huge-title">
        The <span class="serif">Future</span> of <br />Learning.
      </h1>
      <p class="intro-text">
        I am currently operating at the intersection of startup venture and
        academic research. Building an Education platform and a neuro-symbolic
        system for analysing handwritten mathematics.
      </p>
    </header>

    <!-- SECTION 01: THE STARTUP -->
    <section class="focus-section">
      <div class="section-meta">
        <span class="num">01</span>
        <span class="tag">STARTUP / SNAM.IS</span>
      </div>

      <div class="content-grid">
        <div class="main-content">
          <h2 class="project-name">
            SNAM: The Variable Fidelity Knowledge Engine.
          </h2>
          <p class="summary">
            Not a generative guesser. Not a static textbook. SNAM is a learning
            platform that generates infinite, personalized math problems using a
            structured Knowledge Graph and template-based generation.
          </p>
          <div class="tech-stack">
            <strong>Stack:</strong> Vue.js, Django (Python, Postgres), BÍN
            Integration.
          </div>
        </div>

        <div class="detail-sidebar">
          <div class="detail-item">
            <h4>The Innovation</h4>
            <p>
              Infinite problem generation with zero marginal cost. Problems are
              about Football or Biology—not abstract "Train A vs Train B."
            </p>
          </div>
          <div class="detail-item">
            <h4>Personalization</h4>
            <p>
              Queries the KG for logical parameters: "student interest" =
              "electricity", "location = Denmark", "parameter" = "length" ->
              Wind turbine heights.
            </p>
          </div>
          <div class="detail-item">
            <h4>BÍN Integration</h4>
            <p>
              Automated Icelandic grammar. The system fetches correct forms
              (Hestur, Hest, Hesti) based on sentence structure automatically.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 02: THE THESIS -->
    <section class="focus-section">
      <div class="section-meta">
        <span class="num">02</span>
        <span class="tag">RESEARCH / M.SC. THESIS</span>
      </div>

      <div class="content-grid">
        <div class="main-content">
          <h2 class="project-name">Neuro-Symbolic Process Assessment.</h2>
          <p class="summary">
            Developing an autonomous system capable of assessing the *process*
            of handwritten mathematics, not just the final result. We replace
            generative predictions with deterministic logic to overcome LLM
            limitations in correctness and inference speed.
          </p>
          <div class="tech-stack">
            <strong>Core:</strong> Lightweight CNN (Perception) + Symbolic
            Reasoning (Logic Validation).
          </div>
        </div>

        <div class="detail-sidebar">
          <div class="detail-item">
            <h4>Neural Perception</h4>
            <p>
              A lightweight CNN classifies and locates individual handwritten
              symbols using adaptive segmentation.
            </p>
          </div>
          <div class="detail-item">
            <h4>Symbolic Reasoning</h4>
            <p>
              A logic engine performs validation over a finite library of atomic
              mathematical rules for deterministic error recovery.
            </p>
          </div>
          <div class="detail-item">
            <h4>High Efficiency</h4>
            <p>
              Targeting energy use under 0.01 Wh per full cycle, enabling global
              scale at PostgreSQL-level costs.
            </p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
.ueno-focus {
  padding: 180px 10% 200px;
  max-width: 1400px;
  margin: 0 auto;
  text-align: left;
}

.focus-hero {
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
  line-height: 0.9;
  letter-spacing: -4px;
  margin-bottom: 40px;
}

.serif {
  font-family: "Playfair Display", serif;
  font-style: italic;
  font-weight: 700;
}

.intro-text {
  font-size: clamp(1.2rem, 2.6vw, 1.9rem);
  line-height: 1.3;
  max-width: 900px;
  color: #333;
}

/* Section Grid */
.focus-section {
  padding: 100px 0;
  border-top: 1px solid #eee;
}

.section-meta {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 40px;
}

.num {
  font-family: "Playfair Display", serif;
  font-size: 1.5rem;
  font-style: italic;
  color: #ccc;
}

.tag {
  background: var(--ueno-orange);
  color: white;
  padding: 4px 12px;
  font-size: 0.75rem;
  font-weight: 900;
  letter-spacing: 1px;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
}

.project-name {
  font-size: 2.8rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 30px;
  letter-spacing: -1px;
}

.summary {
  font-size: 1.25rem;
  line-height: 1.6;
  color: #444;
  margin-bottom: 30px;
}

.tech-stack {
  font-size: 0.9rem;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Sidebar Details */
.detail-sidebar {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.detail-item h4 {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 10px;
  color: #111;
}

.detail-item p {
  font-size: 1.05rem;
  color: #666;
  line-height: 1.5;
}

.playroom-footer {
  text-align: center;
  margin-top: 150px;
}

.huge-link {
  font-size: clamp(2.5rem, 6vw, 6rem);
  font-weight: 900;
  text-decoration: none;
  color: #000;
  letter-spacing: -3px;
}

.huge-link:hover {
  color: var(--ueno-orange);
}

@media (max-width: 1000px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .project-name {
    font-size: 2.2rem;
  }
}
</style>
