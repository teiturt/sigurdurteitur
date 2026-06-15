<template>
  <main class="ueno-work-view">
    <!-- Header Reveal -->
    <header class="work-header" ref="header">
      <h1 class="main-title reveal">Experience</h1>
      <p class="sub-title reveal">Stuff I've done.</p>
      <a href="/cv.pdf" target="_blank" class="cv-download reveal">
        Download CV (PDF) <span class="arrow">&rarr;</span>
      </a>
    </header>

    <div class="timeline-wrapper" ref="timeline">
      <!-- 2025: NNE -->
      <section class="timeline-item color-nne reveal">
        <div class="time-marker">
          <span class="year">2025</span>
          <span class="status">Present</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            NNE <span class="tag">Hardware</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Student Assistant · Automation Department</p>
          <p class="item-desc">
            Designed an automated inspection pipeline, later used in a course
            run with DTU. Covered cobot workflows, PLC programming, computer
            vision, and 3D modeling of custom hardware such as black-box
            structures. Separately, implemented security protocols for deployed
            smart sensor devices.
          </p>
          <div class="item-footer">
            Computer Vision · PLC Programming · Cobots · 3D Modeling · TIA
            Portal · Docker
          </div>
        </div>
      </section>

      <!-- 2024: Embla -->
      <section class="timeline-item color-embla reveal">
        <div class="time-marker">
          <span class="year">2024</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Embla Medical <span class="tag">Data</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Data Engineer · IT Department</p>
          <p class="item-desc">
            Migrated local SQL infrastructure to a Databricks Lakehouse
            architecture and built Azure data pipelines feeding it. Automated
            manual workflows, cutting multi-hour processes down to seconds of
            real work.
          </p>
          <div class="item-footer">
            Azure · Databricks · Python · SQL · Power BI · Git · Jira
          </div>
        </div>
      </section>

      <!-- 2024: Showdeck -->
      <section class="timeline-item color-web reveal">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Computer Science <span class="tag">Fullstack</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">Showdeck · B.Sc. Project</p>
          <p class="item-desc">
            Led full-stack development on a real-time chat system for a
            production management platform, with API and WebSocket connections,
            user auth, and encrypted message storage.
          </p>
          <div class="item-footer">
            Vue.js · Django · WebSockets · REST API · RabbitMQ · Socket.io
          </div>
        </div>
      </section>

      <!-- 2023: Marel -->
      <section class="timeline-item color-robotics reveal">
        <div class="time-marker">
          <span class="year">2023</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Mechatronics <span class="tag">AMR</span
            ><span class="tag">Software</span>
          </h3>
          <p class="role-title">JBT Marel · B.Sc. Project</p>
          <p class="item-desc">
            Built an Autonomous Mobile Robot for wet fish-factory floors, with
            JBT Marel as the stakeholder. Owned the navigation stack: SLAM
            mapping, path finding, and obstacle avoidance.
          </p>
          <div class="item-footer">
            ROS2 · C++ · Python · ODrive · Lidar · Depth Cameras · Linux
          </div>
        </div>
      </section>

      <!-- 2023: Biomed -->
      <section class="timeline-item color-biomed reveal">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Medical Instrumentation <span class="tag">Hardware</span
            ><span class="tag">Biomedical</span>
          </h3>
          <p class="role-title">Design Contractor · Reykjavík University</p>
          <p class="item-desc">
            Produced an ECG amplifier board reaching medical standards with a
            CMRR of 92 dB. Designed in KiCad, and wrote the build and validation
            guides used in the Medical Instrumentation course it was contracted
            for.
          </p>
          <div class="item-footer">
            KiCad · Analog Circuit Design · Signal Processing · Medical
            Standards
          </div>
        </div>
      </section>

      <!-- 2023: Research -->
      <section class="timeline-item color-research reveal">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Machine Learning <span class="tag">Research</span
            ><span class="tag">Optimization</span>
          </h3>
          <p class="role-title">Research Assistant · Reykjavík University</p>
          <p class="item-desc">
            Researched using Bayesian Optimization to improve antenna designs.
            Built simulation pipelines and compared results against older
            methods.
          </p>
          <div class="item-footer">
            Machine Learning · Bayesian Optimization · MATLAB · CST Studio ·
            Electromagnetic Simulation
          </div>
        </div>
      </section>

      <!-- 2023: Teaching -->
      <section class="timeline-item color-teaching reveal">
        <div class="time-marker"></div>
        <div class="timeline-content">
          <h3 class="item-header">
            Reykjavík University <span class="tag">Academia</span>
          </h3>
          <p class="role-title">Teaching Assistant</p>
          <p class="item-desc">
            Assisted in teaching Applied Programming, Linear Algebra, and
            Medical Instrumentation. Supported undergraduate students through
            lab sessions, created and graded assignments.
          </p>
          <div class="item-footer">Python · MATLAB · Patience</div>
        </div>
      </section>

      <!-- 2022: Skatturinn -->
      <section class="timeline-item color-it reveal">
        <div class="time-marker">
          <span class="year">2022</span>
        </div>
        <div class="timeline-content">
          <h3 class="item-header">
            Skatturinn <span class="tag">Support</span>
          </h3>
          <p class="role-title">IT Support · IT Department</p>
          <p class="item-desc">
            Resolved hardware/software issues for Iceland Revenue and Customs.
            Trained personnel on system operations and security protocols.
          </p>
          <div class="item-footer">
            Windows · PowerShell · SysAdmin · Security · Hardware
          </div>
        </div>
      </section>
    </div>

    <!-- EDUCATION SECTION -->
    <section class="education-section reveal">
      <h2 class="achievements-title">Education</h2>
      <div class="edu-list">
        <div class="edu-item">
          <div class="edu-head">
            <h4>M.Sc. in Autonomous Systems</h4>
            <span class="edu-dates">2024 – 2026</span>
          </div>
          <p>Technical University of Denmark (DTU)</p>
        </div>
        <div class="edu-item">
          <div class="edu-head">
            <h4>B.Sc. in Computer Science</h4>
            <span class="edu-dates">2021 – 2024</span>
          </div>
          <p>Reykjavík University · Dean's List, 2023</p>
        </div>
        <div class="edu-item">
          <div class="edu-head">
            <h4>B.Sc. in Mechatronics Engineering</h4>
            <span class="edu-dates">2020 – 2023</span>
          </div>
          <p>Reykjavík University</p>
        </div>
      </div>
    </section>

    <!-- NEW ACHIEVEMENTS SECTION -->
    <section class="achievements-section reveal">
      <h2 class="achievements-title">Side Quests & Trophies</h2>
      <div class="achievements-grid">
        <!-- Dean's List -->
        <div class="trophy-card">
          <div class="trophy-icon">🏆</div>
          <div class="trophy-content">
            <h4>Dean's List</h4>
            <p>Reykjavik University (2023)</p>
            <span class="details"
              >Award for exceptional academic performance.</span
            >
          </div>
        </div>

        <!-- Robotics Win -->
        <div class="trophy-card">
          <div class="trophy-icon">🏎️</div>
          <div class="trophy-content">
            <h4>RU Mechatronics race</h4>
            <p>1st Place (2022)</p>
            <span class="details">Class competition, still competitive.</span>
          </div>
        </div>

        <!-- Math Comp -->
        <div class="trophy-card">
          <div class="trophy-icon">➗</div>
          <div class="trophy-content">
            <h4>Physics 1 Final (2020)</h4>
            <p>Perfect Score</p>
            <span class="details">Embarrassingly proud.</span>
          </div>
        </div>

        <!-- Random Fun One -->
        <div class="trophy-card">
          <div class="trophy-icon">♟️</div>
          <div class="trophy-content">
            <h4>Chess Bot</h4>
            <p>Failed Experiment</p>
            <span class="details">Would have been cool.</span>
          </div>
        </div>
        <div class="trophy-card">
          <div class="trophy-icon">⛳</div>
          <div class="trophy-content">
            <h4>Longest Drive</h4>
            <p>GÖSSUR (2024)</p>
            <span class="details"
              >Won the prize for hitting the ball further than anyone
              else.</span
            >
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  name: "ExperienceView",
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      const targets = this.$el.querySelectorAll(".reveal");
      const observerOptions = { threshold: 0.25 };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      targets.forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.85) {
          el.classList.add("active", "initial-batch");
        } else {
          observer.observe(el);
        }
      });
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,700;1,500&display=swap");

.ueno-work-view {
  min-height: 100vh;
  padding: 160px 12% 100px;
  background-color: #fff;
  text-align: left;
  overflow-x: hidden;
}

/* REVEAL */
.reveal {
  opacity: 0;
  transition: opacity 2s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.active {
  opacity: 1;
  transition-delay: 0.4s;
}
.reveal.active.initial-batch {
  transition-delay: 0.2s;
  transition-duration: 1.5s;
}

/* HEADER */
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

.cv-download {
  display: inline-flex;
  align-items: center;
  margin-top: 30px;
  font-family: "Inter", sans-serif;
  font-weight: 800;
  font-size: 1rem;
  color: #000;
  text-decoration: none;
  border-bottom: 3px solid #000;
  padding-bottom: 4px;
  transition: all 0.3s ease;
}
.cv-download .arrow {
  margin-left: 8px;
  transition: transform 0.3s ease;
}
.cv-download:hover {
  color: #2563eb;
  border-color: #2563eb;
}
.cv-download:hover .arrow {
  transform: translateX(5px);
}

/* TIMELINE */
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
.timeline-item::after {
  content: "";
  position: absolute;
  left: -2px;
  top: 10px;
  width: 20px;
  height: 2px;
  background-color: inherit;
}
/* Colors */
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
}
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
  gap: 15px;
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

/* --- EDUCATION SECTION --- */
.education-section {
  margin-top: 100px;
  border-top: 1px solid #eee;
  padding-top: 80px;
}

.edu-list {
  display: flex;
  flex-direction: column;
  gap: 32px;
  max-width: 900px;
}

.edu-item {
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 24px;
}

.edu-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 20px;
  flex-wrap: wrap;
}

.edu-head h4 {
  font-family: "Lora", serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #000;
  margin: 0;
  letter-spacing: -0.01em;
}

.edu-dates {
  font-family: "Inter", sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  color: #999;
  white-space: nowrap;
}

.edu-item p {
  font-family: "Inter", sans-serif;
  font-size: 0.95rem;
  color: #666;
  margin: 8px 0 0;
}

/* --- ACHIEVEMENTS SECTION --- */
.achievements-section {
  margin-top: 100px;
  border-top: 1px solid #eee;
  padding-top: 80px;
}

.achievements-title {
  font-family: "Lora", serif;
  font-size: 2rem;
  font-weight: 700;
  color: #000;
  margin-bottom: 40px;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
}

.trophy-card {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.trophy-icon {
  font-size: 2rem;
  flex-shrink: 0;
  margin-top: -5px;
}

.trophy-content h4 {
  font-family: "Inter", sans-serif;
  font-size: 1rem;
  font-weight: 800;
  margin: 0 0 5px 0;
  text-transform: uppercase;
}

.trophy-content p {
  font-family: "Lora", serif;
  font-size: 1rem;
  color: #000;
  margin: 0 0 5px 0;
  font-weight: 600;
}

.trophy-content .details {
  font-family: "Inter", sans-serif;
  font-size: 0.8rem;
  color: #888;
  line-height: 1.4;
  display: block;
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
  .achievements-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style>
