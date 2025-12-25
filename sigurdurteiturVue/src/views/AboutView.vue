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
          Currently, I’m focused on finishing my Msc, and building fun
          interactive experiences. I believe in creating tools that are as
          satisfying to use.
        </p>

        <p class="sign-off">
          Best regards
          <br />
          Sigurður Teitur Tannason
        </p>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap");

.ueno-letter-view {
  min-height: 100vh;
  /* UPDATED: Increased sides to 18% to narrow the text, slashed bottom to 40px */
  padding: 180px 18% 180px;
  background-color: #fff;
  -webkit-font-smoothing: subpixel-antialiased;
  text-align: left;
}

.letter-container {
  /* UPDATED: Slightly smaller max-width for that narrow 'letter' look */
  max-width: 650px;
  margin: 0 auto;
}

/* ... (Greeting and letter-body p styles remain the same) ... */

.letter-body p {
  font-family: "Lora", serif;
  font-size: clamp(1.6rem, 3.4vw, 2rem);
  font-weight: 500;
  line-height: 1.4;
  color: #000;
  margin-bottom: 1em;
  letter-spacing: -0.03em;
}

.sign-off {
  margin-top: 60px; /* UPDATED: Slightly tighter sign-off */
  font-style: italic;
  font-weight: 600;
  color: #000;
}

@media (max-width: 768px) {
  .ueno-letter-view {
    /* Mobile needs less aggressive side padding but still smaller bottom */
    padding: 120px 10% 40px;
  }
}
</style>
