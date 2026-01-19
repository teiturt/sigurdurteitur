<template>
  <main class="ueno-contact-view">
    <div class="contact-container">
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
  position: relative;
  min-height: 100vh;
  width: 100%;
  background-color: #fff;

  /* Flexbox centers it vertically */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  /* Reduced top padding so it centers better without hitting the navbar */
  padding: 100px 24px 60px;
  box-sizing: border-box;
}

.contact-container {
  max-width: 750px;
  width: 100%;
  text-align: left;
}

.main-title {
  font-family: "Inter", sans-serif;
  font-size: clamp(2.5rem, 8vw, 5.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.9;
  /* Reduced margin to pull content up */
  margin-bottom: 40px;
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
  /* Reduced margin to pull links up */
  margin-bottom: 50px;
  color: #000;
  max-width: 700px;
}

.highlight {
  color: var(--ueno-orange, #ff4d00);
}

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
    padding-top: 120px;
    align-items: center;
  }
  .main-title {
    margin-bottom: 30px;
  }
  .intro-text {
    margin-bottom: 40px;
  }
  .link-row {
    gap: 20px;
    padding-top: 20px;
  }
}
</style>
