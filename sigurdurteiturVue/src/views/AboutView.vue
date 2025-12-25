<template>
  <main class="ueno-letter-view">
    <div class="letter-container">
      <div class="letter-body">
        <p>Hi.</p>
        <p>
          My name is Teitur. I’m a software developer and a student of
          Autonomous Systems at DTU.
        </p>

        <p>
          I started my journey in Reykjavík, Iceland, where I earned my B.Sc. in
          Mechatronics and Computer Science.
        </p>

        <p>
          Currently, I’m focused on finishing my Msc, and making life a little
          bit easier.
        </p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "AboutView",
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap");

.ueno-letter-view {
  min-height: 100vh;
  display: flex;
  align-items: center; /* Vertical center */
  justify-content: center; /* Horizontal center */
  background-color: #ffffff;
  /* Margin/Padding increased by ~50% (from 60px to 100px) */
  padding: 100px 30px;
  box-sizing: border-box;
}

.letter-container {
  /* Reduced width to make the column narrower and easier to scan */
  max-width: 560px;
  width: 100%;
  text-align: left;
}

.letter-body p {
  font-family: "Lora", serif;
  /* Reduced font size for a more sophisticated, literary feel */
  font-size: clamp(1.2rem, 2.2vw, 1.7rem);
  font-weight: 500;
  line-height: 1.5; /* Slightly more leading for the smaller font */
  color: #000;
  margin-bottom: 1.3em;
  letter-spacing: -0.02em;
  -webkit-font-smoothing: antialiased;
}

.sign-off {
  margin-top: 50px;
  font-family: "Lora", serif;
  font-style: italic;
  font-weight: 600;
  /* Scaled down proportionally with the body text */
  font-size: 1.2rem;
  color: #000;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .ueno-letter-view {
    align-items: flex-start;
    padding-top: 140px;
  }
  .letter-body p {
    font-size: 1.3rem; /* Fixed comfortable size for mobile */
  }
  .letter-container {
    max-width: 90%; /* Give it a bit more breathing room on small screens */
  }
}
</style>
