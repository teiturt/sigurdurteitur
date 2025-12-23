<template>
  <div class="portfolio-container">
    <!-- Close Button -->
    <button class="back-btn" @click="$emit('goBack')">✕ Close</button>

    <!-- Centered Wrapper -->
    <div class="cv-wrapper">
      
      <!-- Header -->
      <header class="cv-header">
        <h1>Sigurður Teitur Tannason</h1>
        <div class="contact-info">
          <span>Lyngby, Denmark</span>
          <span class="dot">·</span>
          <a href="mailto:sigurdurtt2990@gmail.com">sigurdurtt2990@gmail.com</a>
          <span class="dot">·</span>
          <span>+354 618-9708</span>
        </div>
      </header>

      <!-- About Me -->
      <section class="cv-section">
        <h2 class="section-title">About Me</h2>
        <div class="clean-block">
          <p>My passion lies in automating complex processes and developing creative solutions that eliminate repetitive work. I thrive on solving challenging problems and building tools that make a difference.</p>
        </div>
      </section>

      <!-- Education -->
      <section class="cv-section">
        <h2 class="section-title">Education</h2>
        <div class="cv-item">
          <div class="item-header">
            <span class="bold">M.Sc. in Autonomous Systems</span>
            <span class="date">Sept 2024 – June 2026</span>
          </div>
          <div class="item-subhead">Technical University of Denmark</div>
        </div>
        <div class="cv-item">
          <div class="item-header">
            <span class="bold">B.Sc. in Computer Science</span>
            <span class="date">Aug 2021 – June 2024</span>
          </div>
          <div class="item-subhead">Reykjavík University</div>
          <div class="indent-detail">
            <p>Dean’s List in 2023</p>
          </div>
        </div>
        <div class="cv-item">
          <div class="item-header">
            <span class="bold">B.Sc. in Mechatronics Engineering</span>
            <span class="date">Aug 2020 – June 2023</span>
          </div>
          <div class="item-subhead">Reykjavík University</div>
        </div>
      </section>

      <!-- Experience -->
      <section class="cv-section">
        <h2 class="section-title">Experience</h2>
        
        <div class="cv-item">
          <div class="item-header">
            <span class="bold">Student Assistant, Automation</span>
            <span class="date">Feb 2025 – Present</span>
          </div>
          <div class="item-subhead">NNE, Copenhagen</div>
          <div class="indent-detail">
            <p>Helped with the setup of Robotech 4.0, a course hosted in collaboration with DTU.</p>
            <p>Contributed to the implementation of security protocols in production environments.</p>
          </div>
        </div>

        <div class="cv-item">
          <div class="item-header">
            <span class="bold">Junior Data Engineer</span>
            <span class="date">May 2024 – Aug 2024</span>
          </div>
          <div class="item-subhead">Embla Medical, Reykjavík</div>
          <div class="indent-detail">
            <p>Worked on data ingestion and processing from SQL to Databricks.</p>
            <p>Automated contract generation, reducing completion time by over 36,000%.</p>
            <p>Developed an incremental Azure pipeline for unstable API sources.</p>
          </div>
        </div>

        <div class="cv-item">
          <div class="item-header">
            <span class="bold">Teaching Assistant</span>
            <span class="date">Aug 2023 – Jan 2024</span>
          </div>
          <div class="item-subhead">Reykjavik University</div>
          <div class="indent-detail">
            <p>Courses: Applied Programming, Linear Algebra, and Medical Instrumentation.</p>
            <p>Led lab sessions, designed and graded assignments, and provided help to students.</p>
          </div>
        </div>

        <div class="cv-item">
          <div class="item-header">
            <span class="bold">Research Assistant</span>
            <span class="date">Aug 2023 – Jan 2024</span>
          </div>
          <div class="item-subhead">Reykjavik University</div>
          <div class="indent-detail">
            <p>Applied Bayesian Optimization with custom cost functions to improve antenna designs.</p>
            <p>Conducted testing and data analysis using MATLAB and CST Studio.</p>
          </div>
        </div>

        <div class="cv-item">
          <div class="item-header">
            <span class="bold">Medical Instrumentation Contractor</span>
            <span class="date">May 2023 – Sept 2023</span>
          </div>
          <div class="item-subhead">Reykjavik University</div>
          <div class="indent-detail">
            <p>Redesigned and developed an advanced ECG amplifier board for a Medical Instrumentation course.</p>
            <p>Achieved medical standards for noise reduction, improving previous design by 26 dB.</p>
          </div>
        </div>
      </section>

      <!-- Skills (Styled like About Me) -->
      <section class="cv-section">
        <h2 class="section-title">Skills</h2>
        <div class="clean-block">
          <p><strong>Languages & Frameworks:</strong> Python, SQL, C#, .NET, C++, Typescript, Javascript, ROS2, MATLAB</p>
          <p><strong>Cloud & Data Platforms:</strong> Microsoft Azure, Databricks, Git, Docker</p>
          <p><strong>AI & Machine Learning:</strong> TensorFlow, Keras, PyTorch, scikit-learn</p>
          <p><strong>Tools & Hardware:</strong> KiCad, Inventor, PLC programming, Jira, Confluence, Power BI</p>
          <p><strong>Spoken Languages:</strong> Icelandic (native), English (fluent), Danish (elementary)</p>
        </div>
      </section>

      <!-- Projects (Styled like About Me) -->
      <section class="cv-section">
        <h2 class="section-title">Projects</h2>
        <div class="clean-block project-item">
          <p class="bold">Showdeck Chat / <a href="https://showdeck.io" target="_blank">showdeck.io</a> (2024)</p>
          <p>Designed and built a real-time, secure chat system for the Showdeck production-management platform using Django, Vue.js, Socket.io, RabbitMQ, GraphQL, .NET, and Python.</p>
        </div>
        <div class="clean-block project-item">
          <p class="bold">IRON HORSE / Autonomous Robot (2023)</p>
          <p>Co-designed and implemented an Autonomous Mobile Robot for fish-factory workflows, focusing on navigation, mapping, and obstacle avoidance using ROS2, Python, C++, Linux, and Inventor.</p>
        </div>
      </section>
      
    </div>
  </div>
</template>

<style scoped>
/* Main Background Container */
.portfolio-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #ffffff;
  color: #1a1a1a;
  overflow-y: auto;
  padding: 80px 24px 200px 24px; /* Generous bottom spacing */
  font-family: 'Inter', -apple-system, system-ui, sans-serif;
  z-index: 100;
  box-sizing: border-box;
}

/* Centered content block */
.cv-wrapper {
  max-width: 800px; /* Controlled width */
  margin: 0 auto;   /* Centers the block on screen */
  text-align: left; /* Ensures text inside is left-aligned */
}

/* Header */
.cv-header {
  margin-bottom: 70px;
}

.cv-header h1 {
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 800;
  letter-spacing: -2px;
  margin-bottom: 12px;
  line-height: 1.1;
}

.contact-info {
  font-size: 0.95rem;
  color: #666;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.contact-info a { color: #000; text-decoration: none; border-bottom: 1px solid #eee; }
.dot { color: #ccc; }

/* Sections */
.cv-section { margin-bottom: 30px; }

.section-title {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #999;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 8px;
  margin-bottom: 24px;
}

/* "About Me" Style Block (Used for Skills & Projects too) */
.clean-block p {
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 12px;
  color: #333;
}

.project-item { margin-bottom: 24px; }

/* Experience & Education Items */
.cv-item { margin-bottom: 35px; }

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 15px;
}

.bold { font-weight: 700; font-size: 1.15rem; }
.date { font-weight: 500; color: #888; font-size: 0.9rem; white-space: nowrap; }

.item-subhead {
  font-weight: 500;
  color: #555;
  margin: 2px 0 8px 0;
  font-size: 1rem;
}

/* Standard CV Indentation for details */
.indent-detail {
  padding-left: 20px;
  margin-top: 6px;
}

.indent-detail p {
  margin: 0 0 6px 0;
  font-size: 1rem;
  line-height: 1.5;
  color: #444;
}

/* Close Button */
.back-btn {
  position: fixed;
  top: 30px;
  right: 30px;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 18px;
  font-weight: 600;
  cursor: pointer;
  z-index: 110;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.75rem;
  transition: transform 0.2s;
}

.back-btn:hover { transform: scale(1.05); }

/* MOBILE / NARROW VIEW */
@media (max-width: 650px) {
  .portfolio-container {
    padding: 60px 20px 120px 20px;
  }

  .item-header {
    flex-direction: column; /* Stacks date under title */
    gap: 2px;
  }

  .date { text-align: left; font-size: 0.85rem; }

  .cv-header h1 { font-size: 2.2rem; }

  .back-btn {
    top: auto;
    bottom: 25px; /* Sticky to bottom for reachability on phones */
    right: 50%;
    transform: translateX(50%);
    width: auto;
    min-width: 140px;
    border-radius: 30px; /* Circular pill shape for mobile */
  }

  .indent-detail {
    padding-left: 12px; /* Less indentation to save screen width */
  }
}
</style>