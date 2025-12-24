<template>
  <main class="ueno-home">
    <!-- HERO SECTION: The Space Identity -->
    <section class="hero-section">
      <SpaceToggle class="hero-bg" />
      <div class="hero-content">
        <h1 class="huge-title">
          Sigurður <br />
          <span class="serif">Teitur.</span>
        </h1>
        <p class="hero-subtitle">Software & Autonomous Systems</p>
      </div>
    </section>

    <!-- EXPERIENCE STRIP: Company "Logos" in Ueno Style -->
    <section class="experience-strip">
      <div class="label">Experience</div>
      <div class="company-grid">
        <div class="company">NNE</div>
        <div class="company">Embla Medical</div>
        <div class="company">Reykjavík University</div>
        <div class="company">Iceland Revenue</div>
      </div>
    </section>

    <!-- MEDIA SECTION: Video / Project Gallery -->
    <section class="media-narrative">
      <div class="media-container">
        <!-- Placeholder for your project video or a large picture of you -->
        <div class="video-placeholder">
          <!-- <video autoplay muted loop playsinline src="@/assets/project-reel.mp4"></video> -->
          <div class="overlay-text">
            Visualizing <span class="serif">Automation</span>
          </div>
        </div>
      </div>

      <div class="media-description">
        <h2 class="serif">Performance.</h2>
        <p>
          I am driven by the intersection of humans and the technical world.
          From industrial robots to simple websites, I strive to deliver
          efficent solutions.
        </p>
        <router-link to="/experience" class="text-link"
          >View some projects →</router-link
        >
      </div>
    </section>

    <!-- FOOTER LINK -->
    <section class="home-footer">
      <router-link to="/about" class="huge-footer-link">
        Let’s <span class="serif">Talk</span>
      </router-link>
    </section>
  </main>
</template>

<script>
import SpaceToggle from "../components/SpaceToggle.vue";

export default {
  name: "HomeView",
  components: { SpaceToggle },
};
</script>

<style scoped>
.ueno-home {
  background: #fff;
  text-align: left;
}

/* 1. Hero Section */
.hero-section {
  position: relative;
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  padding: 0 8%;
  color: #fff; /* Hero is dark because of space bg */
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  pointer-events: none;
}

.huge-title {
  font-size: clamp(4rem, 15vw, 12rem);
  font-weight: 900;
  line-height: 0.8;
  letter-spacing: -6px;
  margin: 0;
}

.hero-subtitle {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-top: 40px;
  opacity: 0.6;
}

/* 2. Experience Strip */
.experience-strip {
  padding: 120px 8%;
  background: #fff;
}

.label {
  font-size: 0.75rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #999;
  margin-bottom: 60px;
}

.company-grid {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 40px;
}

.company {
  font-family: "Lora", serif;
  font-size: clamp(1.5rem, 4vw, 3rem);
  font-weight: 400;
  color: #ddd; /* Ghostly gray typical of Ueno */
  transition: color 0.3s;
}

.company:hover {
  color: #000;
}

/* 3. Media Narrative */
.media-narrative {
  padding: 100px 8% 200px;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 80px;
  align-items: center;
}

.video-placeholder {
  width: 100%;
  aspect-ratio: 16/9;
  background: #000;
  position: relative;
  overflow: hidden;
}

.overlay-text {
  position: absolute;
  bottom: 40px;
  left: 40px;
  color: #fff;
  font-size: 2rem;
  font-weight: 800;
}

.media-description h2 {
  font-size: 3.5rem;
  margin-bottom: 30px;
}

.media-description p {
  font-size: 1.4rem;
  line-height: 1.5;
  color: #555;
  margin-bottom: 40px;
}

.text-link {
  font-weight: 900;
  color: #000;
  text-decoration: none;
  border-bottom: 2px solid #000;
  padding-bottom: 5px;
}

/* 4. Footer Link */
.home-footer {
  padding-bottom: 200px;
  text-align: center;
}

.huge-footer-link {
  font-size: clamp(3rem, 10vw, 8rem);
  font-weight: 900;
  text-decoration: none;
  color: #000;
  letter-spacing: -4px;
}

.serif {
  font-family: "Lora", serif;
  font-style: italic;
}

@media (max-width: 1000px) {
  .media-narrative {
    grid-template-columns: 1fr;
  }
  .experience-strip {
    padding-top: 80px;
  }
}
</style>
