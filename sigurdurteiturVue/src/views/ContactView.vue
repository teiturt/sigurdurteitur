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
          <div class="link-item">
            <span class="label">Email</span>
            <a href="mailto:sigurdurtt2990@gmail.com" class="big-link"
              >sigurdurtt2990@gmail.com</a
            >
          </div>

          <div class="link-item">
            <span class="label">Phone</span>
            <a href="tel:+3546189708" class="big-link">+354 618-9708</a>
          </div>

          <div class="link-item">
            <span class="label">Social</span>
            <div class="social-row">
              <a
                href="https://www.linkedin.com/in/teiturtannason/"
                target="_blank"
                class="big-link"
                >LinkedIn</a
              >
            </div>
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
  padding: 180px 10% 200px;
  background-color: #fff;
  text-align: left;
}

.contact-container {
  max-width: 900px;
  margin: 0 auto;
}

.contact-greeting {
  font-family: "Inter", sans-serif;
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 900;
  letter-spacing: -3px;
  margin-bottom: 80px;
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
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  line-height: 1.4;
  margin-bottom: 100px;
  color: #000;
}

.highlight {
  color: var(--ueno-orange, #ff4d00);
}

/* Link List Styling */
.contact-links {
  display: flex;
  flex-direction: column;
  gap: 60px;
  margin-bottom: 120px;
}

.link-item {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.label {
  font-family: "Inter", sans-serif;
  font-size: 0.75rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #999;
}

.big-link {
  font-family: "Lora", serif;
  font-size: clamp(1.2rem, 2.5vw, 2.5rem);
  color: #000;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  width: fit-content;
  transition: all 0.3s ease;
}

.big-link:hover {
  color: var(--ueno-orange, #ff4d00);
  border-bottom-color: var(--ueno-orange, #ff4d00);
}

.social-row {
  display: flex;
  align-items: baseline;
  gap: 15px;
}

.dot {
  color: #ccc;
  font-size: 1.5rem;
}

.sign-off {
  font-size: 1.8rem;
  color: #666;
  margin-top: 40px;
}

@media (max-width: 768px) {
  .ueno-contact-view {
    padding: 120px 24px;
  }
  .contact-greeting {
    margin-bottom: 40px;
  }
  .intro-text {
    margin-bottom: 60px;
  }
  .contact-links {
    gap: 40px;
  }
}
</style>
