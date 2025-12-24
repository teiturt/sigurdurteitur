<template>
  <main class="ueno-work-view">
    <header class="work-header">
      <h1 class="main-title">Experience</h1>
      <p class="sub-title">Some of it.</p>
    </header>

    <section class="work-grid">
      <div class="grid-item">
        <h3 class="bold-header">NNE</h3>
        <p class="muted-text">
          Helped implement low-level security protocols in production
          environments. Working on developing a chess cobot for office fun.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">Embla Medical</h3>
        <p class="muted-text">
          Worked on transitioning from a traditional SQL-based system to a
          Databricks Lakehouse architecture.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">IRON HORSE</h3>
        <!--It was a bsc project for mechatronics with the stakeholder being marel -->
        <p class="muted-text">
          Co-designed an AMR for fish-factory workflows. Focusing on navigation,
          mapping, and obstacle avoidance using ROS2.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">Showdeck</h3>
        <!--It was a bsc project in computer science with the stakeholder being showdeck -->
        <p class="muted-text">
          Designed and built a real-time, secure chat system for the
          production-management platform.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">Biomedical Engineering</h3>
        <p class="muted-text">
          Improved an electrocardiogram hardware design, achieving medical-grade
          noise performance along with getting a seizure.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">Research Assistant</h3>
        <p class="muted-text">
          Applied Bayesian Optimization to improve antenna designs.
        </p>
      </div>

      <div class="grid-item">
        <h3 class="bold-header">More</h3>
        <p class="muted-text">
          Other work includes IT support for Iceland Revenue and Customs,
          Teaching assistant positions, and deep-diving into the M.Sc.
          Autonomous Systems at DTU.
        </p>
      </div>
    </section>
  </main>
</template>

<style scoped>
.ueno-work-view {
  min-height: 100vh;
  padding: 180px 8% 200px;
  background-color: #fff;
  text-align: left;
}

.work-header {
  margin-bottom: 120px;
}

.main-title {
  font-family: "Lora", serif;
  font-size: clamp(3rem, 7vw, 5.5rem);
  font-weight: 700;
  margin: 0;
  color: #000;
  letter-spacing: -3px;
}

.sub-title {
  font-family: "Lora", serif;
  font-size: clamp(3rem, 7vw, 5.5rem);
  font-weight: 500;
  margin: 0;
  color: #b0b0b0; /* Light gray for the italic subtitle */
  font-style: italic;
  letter-spacing: -2px;
}

.work-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 100px 50px;
}

.bold-header {
  font-family: "Lora", serif;
  font-size: 2rem;
  font-weight: 700; /* Bold as per screenshot */
  margin-bottom: 25px;
  color: #000;
  letter-spacing: -1px;
}

.muted-text {
  font-family: "Lora", serif;
  font-size: 1.5rem;
  font-weight: 500; /* Semi-bold description */
  line-height: 1.4;
  color: #b0b0b0; /* The signature Ueno gray */
  letter-spacing: -0.5px;
}

@media (max-width: 1100px) {
  .work-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .work-grid {
    grid-template-columns: 1fr;
    gap: 60px;
  }
  .main-title,
  .sub-title {
    font-size: 3rem;
  }
}
</style>
