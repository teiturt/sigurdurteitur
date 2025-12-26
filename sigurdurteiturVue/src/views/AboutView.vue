<template>
  <main class="ueno-letter-view">
    <div class="letter-container">
      <div class="letter-body" ref="container">
        <!-- BATCH 1: THE BASICS -->
        <p class="reveal">Hi.</p>
        <p class="reveal">
          I’m Teitur, a 24-year-old from Iceland currently completing my M.Sc.
          in Autonomous Systems at DTU. I’m a fierce believer in merit-based
          success. I’m also someone who can’t remember a doctor's appointment to
          save my life, but I can tell you exactly how to optimize a robot's
          path through a factory.
        </p>

        <p class="reveal">
          I haven't decided what I'm going to write, so I will rewrite this at a
          later date so it makes sense, currently it's just a bunch of facts
          about something I've done or felt throughout my journey as a student.
        </p>
        <!-- BATCH 2: THE START -->
        <p class="reveal">
          When I chose to study
          <span class="serif">Hátækniverkfræði</span> (Mechatronics), I chose it
          because robots sounded cool. Early on, I realized I had a knack for
          the logic behind the math, but a total distaste for rote memorization.
        </p>

        <p class="reveal">
          In my first semester, I finished my Physics final an hour early,
          terrified I’d missed a page. It turned out I was one of only two
          students out of 200 to get a perfect score. I succeeded because I was
          deeply engaged with the material, but also because I found a system
          that finally matched my brain: a professor who prioritized the
          architecture of the solution over trivial arithmetic. By focusing on
          the logic rather than the calculation, I could move at my own speed.
          And that’s how I operate:
          <span class="serif">logic first, everything else second.</span>
        </p>

        <!-- BATCH 3: THE COMPETITION -->
        <p class="reveal">
          During a robotics competition, while everyone else was obsessing over
          fine-tuning line-following sensors, I took a different path. I
          measured the radius of the track’s turns and just turned left if the
          robot was on the right side of the track and vice versa. We won the
          race in 9 seconds. The next closest team took over 20.
        </p>

        <!-- BATCH 4: THE PIVOT TO SOFTWARE -->
        <p class="reveal">
          For my B.Sc. thesis, we built an AMR (Autonomous Mobile Robot) for
          Marel. We had to use cheap scooter motors because our order was
          delayed, which made the robot wiggle uncontrollably at high speeds.
          That project taught me two things: I love high-bandwidth navigation
          logic, and <span class="serif">I hate debugging hardware.</span>
          Hardware takes months to ship; Software takes a day to deploy. I chose
          the latter.
        </p>

        <!-- BATCH 5: THE LOW POINT -->
        <p class="reveal">
          I once spent a summer manually changing passwords on pharmaceutical
          equipment. It was the most boring work of my life. A task that a
          five-year-old could do, stretched into ten-hour days. During that same
          summer on a rainy day in July, I had a seizure and was diagnosed with
          epilepsy, which was cool. It also explained the intense headaches and
          blackouts I’d been having for years.
        </p>

        <!-- BATCH 6: THE FUTURE -->
        <p class="reveal">
          I recently received a startup grant for a template-based education
          platform. I’ve realized that the traditional 9-5 grind, where the
          reward for good work is just more work, isn't for me. I’m moving into
          my final semester excited by a simple truth: I’m ready to spend my
          life focusing on what I want to do.
        </p>
        <p class="reveal sign-off">
          Summary:
          <span class="serif"
            >I am bad at what I don't want to do, and great at what I
            love.</span
          >
        </p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "AboutView",
  mounted() {
    this.initReveal();
  },
  methods: {
    initReveal() {
      const targets = this.$refs.container.querySelectorAll(".reveal");
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
        // If it's already on screen at load, pop it in
        if (rect.top < window.innerHeight * 0.95) {
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
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&display=swap");

.ueno-letter-view {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  background-color: #ffffff;
  /* Balanced top padding to allow for the navbar, generous bottom for scrolling */
  padding: 180px 30px 150px;
  box-sizing: border-box;
}

.letter-container {
  max-width: 600px; /* Editorial column width */
  width: 100%;
  text-align: left;
}

.letter-body p {
  font-family: "Lora", serif;
  font-size: clamp(1.2rem, 2.2vw, 1.6rem);
  font-weight: 500;
  line-height: 1.6;
  color: #000;
  margin-bottom: 2em; /* Large gaps between paragraphs for breathing room */
  letter-spacing: -0.01em;
  -webkit-font-smoothing: antialiased;
}

.serif {
  font-style: italic;
  font-weight: 600;
  color: #555; /* Subtle color change for the serif emphasis */
}

/* REVEAL LOGIC */
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

.sign-off {
  margin-top: 80px;
  font-family: "Lora", serif;
  font-style: italic;
  font-weight: 600;
  font-size: 1.2rem;
  color: #000;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .ueno-letter-view {
    padding-top: 140px;
  }
  .letter-body p {
    font-size: 1.3rem;
  }
}
</style>
