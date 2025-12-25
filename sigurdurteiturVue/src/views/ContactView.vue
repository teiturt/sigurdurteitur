<template>
  <main class="ueno-contact-view">
    <div class="contact-container">
      <h1 class="contact-greeting">Get in <span class="serif">touch.</span></h1>

      <div class="contact-body">
        <p class="intro-text">
          Currently based in <span class="highlight">Lyngby, Denmark</span>. I’m
          always open to discussing autonomous systems, creative engineering, or
          new ventures.
        </p>

        <!-- Large Contact Links -->
        <div class="contact-links">
          <div class="link-row">
            <a href="mailto:sigurdurtt2990@gmail.com" class="big-link"
              >Email.
            </a>
            <a href="tel:+3546189708" class="big-link">Phone.</a>
            <a
              href="https://www.linkedin.com/in/teiturtannason/"
              target="_blank"
              class="big-link"
              >LinkedIn.</a
            >
          </div>
        </div>

        <p class="sign-off serif">Let’s build something together.</p>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&display=swap");

.ueno-contact-view {
  min-height: 100vh;
  /* Top 130px (reduced from 180), Sides 20% (increased for narrow width), Bottom 80px */
  padding: 130px 20% 80px;
  background-color: #fff;
  text-align: left;
}

.contact-container {
  /* Restricting max-width to keep lines comfortable for reading */
  max-width: 650px;
  margin: 0 auto;
}

.contact-greeting {
  font-family: "Inter", sans-serif;
  font-size: clamp(3rem, 7vw, 7rem);
  font-weight: 900;
  letter-spacing: -3px;
  margin-bottom: 60px;
  color: #000;
}

.serif {
  font-family: "Lora", serif;
  font-style: italic;
  font-weight: 400;
  letter-spacing: -1px;
}

.intro-text {
  font-family: "Lora", serif;
  font-size: clamp(1.4rem, 2.5vw, 2rem);
  line-height: 1.4;
  margin-bottom: 80px;
  color: #000;
}

.highlight {
  color: var(--ueno-orange, #ff4d00);
}

/* Link List Styling */
.contact-links {
  margin-bottom: 60px;
}

.link-row {
  display: flex;
  flex-wrap: wrap; /* Allows wrapping on small mobile screens */
  gap: 40px; /* Space between the links */
  align-items: baseline;
}

.big-link {
  font-family: "Lora", serif;
  font-size: clamp(1.4rem, 2.5vw, 2rem);
  font-weight: 500;
  color: #000;
  text-decoration: none;
  transition: all 0.3s ease;
  line-height: 1.1;
  letter-spacing: -1px;
}

.big-link:hover {
  color: var(--ueno-orange, #ff4d00);
  transform: translateY(
    -5px
  ); /* Subtle lift instead of horizontal slide for row layout */
}

.sign-off {
  font-size: clamp(1.2rem, 2vw, 1.6rem);
  color: #666;
  margin-top: 40px;
}

@media (max-width: 1024px) {
  .ueno-contact-view {
    padding: 120px 10% 60px;
  }
}

@media (max-width: 768px) {
  .ueno-contact-view {
    padding: 100px 24px 60px;
  }
  .contact-greeting {
    margin-bottom: 30px;
  }
  .intro-text {
    margin-bottom: 50px;
  }
  .contact-links {
    gap: 40px;
  }
}
</style>
