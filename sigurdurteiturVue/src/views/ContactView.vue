<template>
  <main class="ueno-contact-view">
    <div class="contact-container">
      <!-- The Conversational Title -->
      <h1 class="main-title">
        Let’s build something <br />
        <span class="serif">together.</span>
      </h1>

      <div class="contact-body">
        <p class="intro-text">
          Currently based in <span class="highlight">Lyngby, Denmark</span>. I’m
          always open to discussing autonomous systems, creative engineering, or
          new ventures.
        </p>

        <!-- Structured Link Row -->
        <div class="link-row">
          <a href="mailto:sigurdurtt2990@gmail.com" class="big-link">Email.</a>
          <a href="tel:+3546189708" class="big-link">Phone.</a>
          <a
            href="https://www.linkedin.com/in/teiturtannason/"
            target="_blank"
            class="big-link"
            >LinkedIn.</a
          >
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&display=swap");

.ueno-contact-view {
  min-height: 100vh;
  background-color: #fff;
  /* Use Flexbox to center the container on the screen */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 80px 24px;
}

.contact-container {
  max-width: 750px;
  width: 100%;
  /* Keep text left-aligned inside the centered box */
  text-align: left;
}

.main-title {
  font-family: "Inter", sans-serif;
  font-size: clamp(2.5rem, 8vw, 5.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.9;
  margin-bottom: 60px;
  color: #000;
}

.serif {
  font-family: "Lora", serif;
  font-style: italic;
  font-weight: 400;
}

.intro-text {
  font-family: "Lora", serif;
  font-size: clamp(1.4rem, 2.5vw, 2.1rem);
  line-height: 1.4;
  margin-bottom: 80px;
  color: #000;
  max-width: 700px; /* Keep the paragraph from getting too wide */
}

.highlight {
  color: var(--ueno-orange, #ff4d00);
}

/* Punctuated Link Row */
.link-row {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  align-items: baseline;
  border-top: 1px solid #eee;
  padding-top: 40px;
}

.big-link {
  font-family: "Lora", serif;
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  font-weight: 500;
  color: #000;
  text-decoration: none;
  transition: all 0.3s ease;
  letter-spacing: -1px;
}

.big-link:hover {
  color: var(--ueno-orange, #ff4d00);
  transform: translateY(-3px);
}

@media (max-width: 768px) {
  .ueno-contact-view {
    /* On mobile, we align to the top instead of vertical center for better scrolling */
    align-items: flex-start;
    padding-top: 120px;
  }
  .main-title {
    margin-bottom: 40px;
  }
  .intro-text {
    margin-bottom: 60px;
  }
  .link-row {
    gap: 20px;
  }
}
</style>
