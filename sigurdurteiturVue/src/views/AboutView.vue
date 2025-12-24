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
/* Importing Lora with heavy weights (500, 600, 700) */
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap");

.ueno-letter-view {
  min-height: 100vh;
  padding: 180px 10% 200px;
  background-color: #fff;
  /* Standard smoothing makes text look thicker/bolder than 'antialiased' */
  -webkit-font-smoothing: subpixel-antialiased;
  text-align: left;
}

.letter-container {
  max-width: 900px;
  margin: 0 auto;
}

.greeting {
  font-family: "Lora", serif;
  font-size: clamp(3rem, 8vw, 5rem);
  font-weight: 700; /* Bolder header */
  margin-bottom: 60px;
  color: #000;
  letter-spacing: -2px;
}

.letter-body p {
  font-family: "Lora", serif;
  /* Massive, bold body text like the screenshot */
  font-size: clamp(1.8rem, 3.8vw, 2.4rem);
  font-weight: 500; /* The secret to the "thick" look */
  line-height: 1.4;
  color: #000;
  margin-bottom: 1em;
  letter-spacing: -0.03em;
}

.sign-off {
  margin-top: 100px;
  font-style: italic;
  font-weight: 600;
  color: #000;
}

@media (max-width: 768px) {
  .ueno-letter-view {
    padding: 120px 24px;
  }
}
</style>
