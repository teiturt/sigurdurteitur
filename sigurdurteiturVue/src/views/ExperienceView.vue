<template>
  <main class="ueno-work-view">
    <header class="work-header">
      <h1 class="main-title">Experience</h1>
      <p class="sub-title">The Chronicle.</p>
    </header>

    <div class="timeline-wrapper">
      <!-- 2025 -->
      <section class="timeline-item color-nne">
        <div class="time-marker">
          <span class="year">2025</span>
          <span class="status">Present</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            NNE <span class="tag">Hardware</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Student Assistant, Automation</p>
          <p class="item-desc">
            Implemented low-level security protocols in production environments.
            Worked on a chess cobot to play chess with the employes.
          </p>
          <div class="item-footer">
            TIA Portal · 3D Modeling · Human-Robot Interaction
          </div>
        </div>
      </section>

      <!-- 2024 -->
      <section class="timeline-item color-embla">
        <div class="time-marker">
          <span class="year">2024</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Embla Medical <span class="tag">Data</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Junior Data Engineer</p>
          <p class="item-desc">
            Migrated local SQL infrastructure to a Databricks Lakehouse
            architecture. Automated contract generation, achieving a 360x
            reduction in processing time.
          </p>
          <div class="item-footer">Azure · Databricks · Python</div>
        </div>
      </section>

      <!-- 2024 (Year label hidden) -->
      <section class="timeline-item color-web">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Showdeck <span class="tag">Fullstack</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Software Engineer (B.Sc. Project)</p>
          <p class="item-desc">
            Architected a real-time, chat infrastructure for production
            management, ensuring reliability for large-scale event teams.
          </p>
          <div class="item-footer">Vue.js · Django · WebSockets</div>
        </div>
      </section>

      <!-- 2023 -->
      <section class="timeline-item color-robotics">
        <div class="time-marker">
          <span class="year">2023</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Marel <span class="tag">AMR</span><span class="tag">SOFTWARE</span>
          </h3>
          <p class="role-title">Mechatronics (B.Sc. Project)</p>
          <p class="item-desc">
            Co-designed an Autonomous Mobile Robot for fish-factory workflows.
            Owned the navigation stack, SLAM mapping, and obstacle avoidance
            logic.
          </p>
          <div class="item-footer">ROS2 · C++ · Navigation Stack</div>
        </div>
      </section>

      <!-- 2023 (Split: Hardware Innovation) -->
      <section class="timeline-item color-biomed">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Medical Instrumentation <span class="tag">Hardware</span
            ><span class="tag">Biomedical</span>
          </h3>
          <p class="role-title">Design Contractor</p>
          <p class="item-desc">
            Independently designed, prototyped, and validated a 3-lead ECG
            amplifier board that achieved medical-grade noise performance,
            surpassing the previous design by 26 dB.
          </p>
          <div class="item-footer">
            KiCad · Analog Circuit Design · Signal Processing · Medical
            Standards
          </div>
        </div>
      </section>

      <!-- 2023 (Split: Research & Optimization) -->
      <section class="timeline-item color-research">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Antenna Research <span class="tag">Research</span
            ><span class="tag">Optimization</span>
          </h3>
          <p class="role-title">Research Assistant</p>
          <p class="item-desc">
            Applied Bayesian Optimization with custom cost functions to automate
            and improve antenna design parameters, comparing performance against
            traditional methods in simulation.
          </p>
          <div class="item-footer">
            MATLAB · Bayesian Optimization · CST Studio · Electromagnetic
            Simulation
          </div>
        </div>
      </section>

      <!-- 2023 (Year label hidden) -->
      <section class="timeline-item color-teaching">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            RU Teaching <span class="tag">Academia</span>
          </h3>
          <p class="role-title">Teaching Assistant</p>
          <p class="item-desc">
            Assisted in teaching Applied Programming, Linear Algebra, and
            Medical Instrumentation. Supported undergraduate students through
            lab sessions, created and graded assignments.
          </p>
          <div class="item-footer">C++ · MATLAB · Pedagogy</div>
        </div>
      </section>

      <!-- 2022 -->
      <section class="timeline-item color-it">
        <div class="time-marker">
          <span class="year">2022</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Skatturinn <span class="tag">Support</span>
          </h3>
          <p class="role-title">IT Support Specialist</p>
          <p class="item-desc">
            Resolved hardware/software issues for Iceland Revenue and Customs.
            Trained personnel on system operations and security protocols.
          </p>
          <div class="item-footer">SysAdmin · Security · Hardware</div>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,700;1,500&display=swap");

.ueno-work-view {
  min-height: 100vh;
  padding: 160px 12% 100px;
  background-color: #fff;
  text-align: left;
}

.work-header {
  margin-bottom: 100px;
}

.main-title {
  font-family: "Lora", serif;
  font-size: clamp(3rem, 7vw, 5rem);
  font-weight: 700;
  letter-spacing: -0.04em;
  color: #000;
  margin: 0;
}

.sub-title {
  font-family: "Lora", serif;
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 500;
  color: #eee;
  font-style: italic;
  letter-spacing: -0.02em;
  margin: 0;
}

.timeline-wrapper {
  max-width: 900px;
  margin: 0;
}

.timeline-item {
  display: grid;
  grid-template-columns: 100px 1fr;
  padding-bottom: 60px;
  border-left: 2px solid #eee;
  position: relative;
  padding-left: 40px;
  margin-left: 10px;
}

/* Horizontal Connector Line */
.timeline-item::after {
  content: "";
  position: absolute;
  left: -2px;
  top: 10px;
  width: 20px;
  height: 2px;
  background-color: inherit;
}

/* SECTION COLORS - Added Biomed Color */
.color-nne {
  border-left-color: #131e40;
}
.color-embla {
  border-left-color: #222b38;
}
.color-web {
  border-left-color: #9900ff;
}
.color-robotics {
  border-left-color: #ffcc00;
}
.color-biomed {
  border-left-color: #ff4d00;
} /* Sharp orange for Innovation */
.color-research {
  border-left-color: #00ff88;
}
.color-teaching {
  border-left-color: #ff0055;
}
.color-it {
  border-left-color: #333333;
}

.time-marker {
  display: flex;
  flex-direction: column;
  font-family: "Inter", sans-serif;
  user-select: none;
}

.year {
  font-weight: 900;
  font-size: 1.1rem;
  color: #000;
}

.status {
  font-size: 0.6rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #999;
  margin-top: 5px;
}

.item-header {
  font-family: "Lora", serif;
  font-size: 1.8rem;
  font-weight: 700;
  margin: -5px 0 10px 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  letter-spacing: -0.02em;
}

.tag {
  font-family: "Inter", sans-serif;
  font-size: 0.55rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 3px 8px;
  border: 1px solid #eee;
  color: #aaa;
  border-radius: 4px;
}

.role-title {
  font-family: "Inter", sans-serif;
  font-weight: 700;
  font-size: 0.85rem;
  color: #000;
  margin-bottom: 15px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.item-desc {
  font-family: "Lora", serif;
  font-size: 1.2rem;
  line-height: 1.5;
  color: #444;
  max-width: 600px;
  margin-bottom: 20px;
}

.item-footer {
  font-family: "Inter", sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 1px;
}

@media (max-width: 768px) {
  .ueno-work-view {
    padding: 100px 24px;
  }
  .timeline-item {
    grid-template-columns: 1fr;
    gap: 15px;
    padding-left: 30px;
  }
  .time-marker {
    flex-direction: row;
    gap: 10px;
    align-items: baseline;
  }
  .timeline-item::after {
    top: 12px;
    width: 15px;
  }
  .main-title,
  .sub-title {
    font-size: 2.5rem;
  }
}
</style>
