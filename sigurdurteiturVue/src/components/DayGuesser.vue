<template>
  <main class="savant-container">
    <header class="savant-header">
      <div class="header-left">
        <router-link to="/" class="back-link">← Return to Hub</router-link>
        <h1 class="savant-title">The <span class="serif">Savant.</span></h1>
      </div>

      <div class="mode-switcher">
        <button
          v-for="m in modes"
          :key="m.id"
          class="mode-btn"
          :class="{ active: currentMode === m.id }"
          @click="switchMode(m.id)"
        >
          {{ m.label }}
        </button>
      </div>

      <button class="rules-btn" @click="showRules = !showRules">
        {{ showRules ? "Hide Rules" : "Reference & Rules" }}
      </button>
    </header>

    <div class="content-wrapper">
      <transition name="slide-fade">
        <div v-if="showRules" class="rules-panel">
          <div class="rules-grid">
            <div class="rule-block">
              <h3>The 12 Method</h3>
              <p>For last 2 digits of year (YY):</p>
              <ol>
                <li><strong>12s:</strong> YY ÷ 12</li>
                <li><strong>Rem:</strong> YY % 12</li>
                <li><strong>4s:</strong> Rem ÷ 4</li>
                <li><strong>Sum:</strong> 12s + Rem + 4s</li>
              </ol>
            </div>
            <div class="rule-block">
              <h3>Month Doomsdays</h3>
              <ul class="code-list">
                <li><span>Jan</span> 3 (4 Leap)</li>
                <li><span>Feb</span> 28 (29 Leap)</li>
                <li><span>Mar</span> 14</li>
                <li><span>Apr</span> 4</li>
                <li><span>May</span> 9</li>
                <li><span>Jun</span> 6</li>
                <li><span>Jul</span> 11</li>
                <li><span>Aug</span> 8</li>
                <li><span>Sep</span> 5</li>
                <li><span>Oct</span> 10</li>
                <li><span>Nov</span> 7</li>
                <li><span>Dec</span> 12</li>
              </ul>
            </div>
            <div class="rule-block">
              <h3>Century Anchors</h3>
              <ul class="code-list">
                <li><span>1800s</span> Fri (5)</li>
                <li><span>1900s</span> Wed (3)</li>
                <li><span>2000s</span> Tue (2)</li>
                <li><span>2100s</span> Sun (0)</li>
              </ul>
            </div>
            <div class="rule-block">
              <h3>Weekdays</h3>
              <ul class="code-list">
                <li><span>Sun</span> 0</li>
                <li><span>Mon</span> 1</li>
                <li><span>Tue</span> 2</li>
                <li><span>Wed</span> 3</li>
                <li><span>Thu</span> 4</li>
                <li><span>Fri</span> 5</li>
                <li><span>Sat</span> 6</li>
              </ul>
            </div>
          </div>
        </div>
      </transition>

      <section v-if="currentMode === 'practice'" class="mode-section">
        <div class="setup-controls" v-if="!practiceActive">
          <h2>Lab Configuration</h2>
          <p>Select exactly which mental steps you want to verify.</p>

          <div class="config-columns">
            <div class="col">
              <h3>Year Calculation</h3>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.year12" />
                <span>Step 1: 12s</span>
              </label>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.yearRem" />
                <span>Step 2: Remainder</span>
              </label>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.year4" />
                <span>Step 3: 4s</span>
              </label>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.century" />
                <span>Century Anchor</span>
              </label>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.yearDoom" />
                <span>Year Doomsday</span>
              </label>
            </div>

            <div class="col">
              <h3>Month Data</h3>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.monthDoom" />
                <span>Month Anchor Date</span>
              </label>
            </div>

            <div class="col">
              <h3>Final Calculation</h3>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.dist" />
                <span>Distance (Day - Anchor)</span>
              </label>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.sum" />
                <span>Final Sum</span>
              </label>
              <label class="checkbox-card highlight">
                <input type="checkbox" v-model="practiceConfig.finalName" />
                <span>Result (The Day)</span>
              </label>
            </div>
          </div>

          <div class="action-row">
            <button class="action-btn large" @click="startPractice">
              Start Session
            </button>
          </div>
        </div>

        <div v-else class="practice-session">
          <div class="target-date">
            <span class="label">Solve For</span>
            <span class="huge-date">{{ practiceDateFormatted }}</span>
          </div>

          <div class="history-list">
            <transition-group name="list">
              <div
                v-for="(item, i) in practiceHistory"
                :key="i"
                class="step-card completed"
              >
                <div class="step-header">
                  <span class="step-num">✓</span>
                  <h3 class="step-title">{{ item.title }}</h3>
                </div>
                <div class="completed-view">
                  <div class="math-display small" v-if="item.math">
                    {{ item.math }}
                  </div>
                  <div class="result-badge">
                    {{ item.displayAnswer || item.answer }}
                  </div>
                </div>
              </div>
            </transition-group>
          </div>

          <div
            class="step-card active practice-card"
            v-if="currentPracticeStep && !sessionComplete"
          >
            <div class="step-header">
              <span class="step-num">?</span>
              <h3 class="step-title">{{ currentPracticeStep.title }}</h3>
            </div>
            <div class="interaction-area">
              <div class="math-display text-hint">
                {{ currentPracticeStep.hint }}
              </div>
              <div class="input-row">
                <input
                  v-if="currentPracticeStep.type !== 'dayName'"
                  type="number"
                  v-model.number="practiceInput"
                  @keyup.enter="checkPractice"
                  placeholder="..."
                  ref="pracInput"
                />
                <select
                  v-else
                  v-model="practiceInput"
                  class="day-select"
                  @change="checkPractice"
                  ref="pracInput"
                >
                  <option disabled value="">Select Day</option>
                  <option v-for="d in weekdays" :key="d" :value="d">
                    {{ d }}
                  </option>
                </select>

                <button @click="checkPractice" class="action-btn">
                  Submit
                </button>
              </div>
              <div class="feedback" :class="feedbackType">
                {{ feedbackMsg }}
              </div>
            </div>
          </div>

          <div v-if="sessionComplete" class="complete-area">
            <div class="success-banner">Calculation Complete.</div>
            <div class="review-actions">
              <button class="action-btn large" @click="startPractice">
                Next Random Date →
              </button>
              <button class="reset-link" @click="stopPractice">
                Change Settings
              </button>
            </div>
          </div>

          <button
            v-if="!sessionComplete"
            class="reset-link"
            @click="stopPractice"
          >
            Quit & Configure
          </button>
        </div>
      </section>

      <section v-if="currentMode === 'test'" class="mode-section">
        <div class="test-setup" v-if="!testActive && !testGameOver">
          <h2>Speed Test Settings</h2>
          <div class="test-options">
            <div class="option-group">
              <h3>Game Mode</h3>
              <div class="pill-selector">
                <button
                  :class="{ active: testSettings.mode === 'streak' }"
                  @click="testSettings.mode = 'streak'"
                >
                  🔥 Streak (Survival)
                </button>
                <button
                  :class="{ active: testSettings.mode === 'timed' }"
                  @click="testSettings.mode = 'timed'"
                >
                  ⏱️ Timed
                </button>
              </div>
            </div>

            <div class="option-group" v-if="testSettings.mode === 'timed'">
              <h3>Duration</h3>
              <div class="pill-selector">
                <button
                  :class="{ active: testSettings.duration === 60 }"
                  @click="testSettings.duration = 60"
                >
                  1 Min
                </button>
                <button
                  :class="{ active: testSettings.duration === 180 }"
                  @click="testSettings.duration = 180"
                >
                  3 Min
                </button>
                <button
                  :class="{ active: testSettings.duration === 300 }"
                  @click="testSettings.duration = 300"
                >
                  5 Min
                </button>
              </div>
            </div>
          </div>
          <button class="action-btn large" @click="startTest">
            Start Engine
          </button>
        </div>

        <div v-if="testActive" class="test-header">
          <div class="hud-container">
            <div class="hud-item">
              <span class="hud-label">Score</span>
              <span class="hud-value">{{ testScore }}</span>
            </div>
            <div class="hud-item">
              <span class="hud-label">Streak</span>
              <span class="hud-value fire" :class="{ lit: currentStreak > 0 }">
                {{ currentStreak }} 🔥
              </span>
            </div>
            <div class="hud-item" v-if="testSettings.mode === 'timed'">
              <span class="hud-label">Time</span>
              <span class="hud-value" :class="{ low: timerSeconds < 10 }">
                {{ formattedTimer }}
              </span>
            </div>
          </div>
        </div>

        <div v-if="testActive" class="test-area">
          <div class="huge-date center">{{ testDateFormatted }}</div>
          <p class="prompt">What day of the week is this?</p>

          <div class="weekday-grid">
            <button
              v-for="(day, index) in weekdays"
              :key="day"
              class="day-btn"
              @click="submitTest(index)"
            >
              {{ day }}
            </button>
          </div>
          <div class="feedback center" :class="feedbackType">
            {{ feedbackMsg }}
          </div>
        </div>

        <div v-if="testGameOver" class="complete-area">
          <div class="success-banner">Session Finished</div>
          <div class="stats-grid">
            <div class="stat-box">
              <label>Final Score</label>
              <div class="val">{{ testScore }}</div>
            </div>
            <div class="stat-box">
              <label>Best Streak</label>
              <div class="val">{{ bestStreak }}</div>
            </div>
          </div>

          <div class="review-actions">
            <button class="action-btn large" @click="startTest">
              Try Again
            </button>
            <button class="reset-link" @click="resetTestSetup">
              Change Mode
            </button>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<script>
export default {
  name: "DayGuesserView",
  data() {
    return {
      currentMode: "practice",
      showRules: false,
      modes: [
        { id: "practice", label: "Practice Lab" },
        { id: "test", label: "Speed Test" },
      ],
      weekdays: [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ],
      months: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],

      // --- Practice State ---
      practiceActive: false,
      sessionComplete: false,
      practiceDate: null,
      practiceConfig: {
        year12: true,
        yearRem: true,
        year4: true,
        century: false,
        yearDoom: false,
        monthDoom: true,
        dist: true,
        sum: true,
        finalName: true,
      },
      practiceQueue: [],
      practiceHistory: [],
      practiceInput: "",
      feedbackMsg: "",
      feedbackType: "",

      // --- Test (Speed) State ---
      testActive: false,
      testGameOver: false,
      testDate: null,
      testScore: 0,
      currentStreak: 0,
      bestStreak: 0,
      timerSeconds: 0,
      timerInterval: null,

      // Settings
      testSettings: {
        mode: "streak", // 'streak' or 'timed'
        duration: 60, // seconds
      },
    };
  },
  computed: {
    practiceDateFormatted() {
      if (!this.practiceDate) return "";
      return this.practiceDate.toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    testDateFormatted() {
      if (!this.testDate) return "";
      return this.testDate.toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    currentPracticeStep() {
      if (!this.practiceQueue.length) return null;
      return this.practiceQueue[0];
    },
    formattedTimer() {
      const m = Math.floor(this.timerSeconds / 60);
      const s = this.timerSeconds % 60;
      return `${m}:${s < 10 ? "0" : ""}${s}`;
    },
  },
  methods: {
    getLogicValues(date) {
      const year = date.getFullYear();
      const month = date.getMonth();
      const day = date.getDate();
      const yy = year % 100;

      const step1 = Math.floor(yy / 12);
      const step2 = yy % 12;
      const step3 = Math.floor(step2 / 4);

      // Century Anchor logic
      const c = Math.floor(year / 100);
      let anchor = 2;
      if (c === 19) anchor = 3;
      if (c === 18) anchor = 5;
      if (c === 21) anchor = 0;

      const yearDoomsday = (step1 + step2 + step3 + anchor) % 7;

      // Month Doomsdays
      const isLeap = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
      const mCodes = [
        isLeap ? 4 : 3, // Jan
        isLeap ? 29 : 28, // Feb
        14,
        4,
        9,
        6,
        11,
        8,
        5,
        10,
        7,
        12, // Mar-Dec
      ];
      const monthDoomDate = mCodes[month];

      return {
        yy,
        step1,
        step2,
        step3,
        centuryAnchor: anchor,
        yearDoomsday,
        monthDoomDate,
        day,
        month,
      };
    },

    switchMode(mode) {
      this.currentMode = mode;
      this.stopPractice();
      this.resetTestSetup();
    },

    // --- PRACTICE LOGIC ---
    startPractice() {
      // 1. Generate Date
      const year = 1900 + Math.floor(Math.random() * 200);
      const month = Math.floor(Math.random() * 12);
      const day = Math.floor(Math.random() * 28) + 1;
      this.practiceDate = new Date(year, month, day);

      const v = this.getLogicValues(this.practiceDate);

      // 3. Reset State
      this.practiceQueue = [];
      this.practiceHistory = [];
      this.feedbackMsg = "";
      this.practiceInput = "";
      this.sessionComplete = false;

      const c = this.practiceConfig;

      // --- UPDATED: Verbose/Wordy Hints ---

      // Step 1
      if (c.year12) {
        this.practiceQueue.push({
          title: `Step 1: 12s`,
          hint: `How many times does 12 fit into ${v.yy}? (Ignore decimals)`,
          answer: v.step1,
          math: `${v.yy} ÷ 12 =`,
        });
      }

      // Step 2
      if (c.yearRem) {
        this.practiceQueue.push({
          title: `Step 2: Remainder`,
          hint: `What is the remainder after dividing ${v.yy} by 12?`,
          answer: v.step2,
          math: `Remainder =`,
        });
      }

      // Step 3
      if (c.year4) {
        this.practiceQueue.push({
          title: `Step 3: 4s`,
          hint: `How many times does 4 fit into the remainder (${v.step2})?`,
          answer: v.step3,
          math: `${v.step2} ÷ 4 =`,
        });
      }

      if (c.century) {
        this.practiceQueue.push({
          title: `Century Anchor`,
          hint: `What is the anchor for the ${Math.floor(
            year / 100,
          )}00s? (1800s=Fri, 1900s=Wed, 2000s=Tue)`,
          answer: v.centuryAnchor,
          math: `Anchor =`,
        });
      }

      if (c.yearDoom) {
        this.practiceQueue.push({
          title: `Year Doomsday`,
          hint: `Add the previous numbers (${v.step1} + ${v.step2} + ${v.step3} + Anchor). Then take the remainder of 7.`,
          answer: v.yearDoomsday,
          math: `Year Index =`,
        });
      }

      // Month
      if (c.monthDoom) {
        this.practiceQueue.push({
          title: `Month Doomsday Date`,
          hint: `What is the always-same doomsday date for ${this.months[month]}?`,
          answer: v.monthDoomDate,
          math: `${this.months[month]} Date =`,
        });
      }

      // Final Steps Logic
      const distance = v.day - v.monthDoomDate;
      const rawSum = v.yearDoomsday + distance;
      const finalDayIndex = ((rawSum % 7) + 7) % 7;

      if (c.dist) {
        this.practiceQueue.push({
          title: `Distance`,
          hint: `Subtract the Month Anchor (${v.monthDoomDate}) from the actual Day (${v.day}).`,
          answer: distance,
          math: `${v.day} - ${v.monthDoomDate} =`,
        });
      }

      if (c.sum) {
        this.practiceQueue.push({
          title: `Final Sum`,
          hint: `Add the Year Index (${v.yearDoomsday}) to the Distance (${distance}).`,
          answer: rawSum,
          math: `Total =`,
        });
      }

      if (c.finalName) {
        this.practiceQueue.push({
          title: `Final Weekday`,
          hint: `What day of the week corresponds to that total?`,
          answer: this.weekdays[finalDayIndex],
          type: "dayName",
          math: `Day =`,
        });
      }

      if (this.practiceQueue.length === 0) {
        alert("Please select at least one step to practice.");
        this.practiceActive = false;
        return;
      }

      this.practiceActive = true;
      this.$nextTick(() => {
        if (this.$refs.pracInput) this.$refs.pracInput.focus();
      });
    },

    checkPractice() {
      if (this.practiceInput === "" || this.practiceInput === null) return;
      const current = this.practiceQueue[0];

      let correct = false;
      if (current.type === "dayName") {
        correct = this.practiceInput === current.answer;
      } else {
        correct = parseInt(this.practiceInput) === current.answer;
      }

      if (correct) {
        this.feedbackMsg = "Correct";
        this.feedbackType = "success";

        setTimeout(() => {
          const done = this.practiceQueue.shift();
          done.displayAnswer = done.answer;
          this.practiceHistory.push(done);
          this.practiceInput = "";
          this.feedbackMsg = "";

          if (this.practiceQueue.length > 0) {
            this.$nextTick(() => {
              const el = this.$refs.pracInput;
              if (el) el.focus();
            });
          } else {
            this.sessionComplete = true;
          }
        }, 300);
      } else {
        this.feedbackType = "error";
        this.feedbackMsg = "Incorrect, try again.";
      }
    },

    stopPractice() {
      this.practiceActive = false;
      this.sessionComplete = false;
      this.practiceQueue = [];
      this.practiceHistory = [];
    },

    // --- TEST LOGIC ---
    resetTestSetup() {
      this.testActive = false;
      this.testGameOver = false;
      this.testScore = 0;
      this.currentStreak = 0;
      this.bestStreak = 0;
      clearInterval(this.timerInterval);
    },

    startTest() {
      this.testActive = true;
      this.testGameOver = false;
      this.testScore = 0;
      this.currentStreak = 0;
      this.bestStreak = 0;
      this.feedbackMsg = "";

      // Set Timer if mode is timed
      if (this.testSettings.mode === "timed") {
        this.timerSeconds = this.testSettings.duration;
        this.timerInterval = setInterval(() => {
          this.timerSeconds--;
          if (this.timerSeconds <= 0) {
            this.finishTest();
          }
        }, 1000);
      }

      this.generateTestQuestion();
    },

    finishTest() {
      clearInterval(this.timerInterval);
      this.testActive = false;
      this.testGameOver = true;
    },

    generateTestQuestion() {
      this.feedbackMsg = "";
      const start = new Date(1950, 0, 1);
      const end = new Date(2050, 11, 31);
      this.testDate = new Date(
        start.getTime() + Math.random() * (end.getTime() - start.getTime()),
      );
    },

    submitTest(dayIndex) {
      const correct = dayIndex === this.testDate.getDay();
      const isStreakMode = this.testSettings.mode === "streak";

      if (correct) {
        this.testScore++;
        this.currentStreak++;
        if (this.currentStreak > this.bestStreak) {
          this.bestStreak = this.currentStreak;
        }

        this.feedbackType = "success";
        this.feedbackMsg = "Correct!";

        setTimeout(() => this.generateTestQuestion(), 200);
      } else {
        // WRONG ANSWER
        if (isStreakMode) {
          // Streak Mode: Immediate Game Over
          this.finishTest();
        } else {
          // Timed Mode: Break streak, show error, move to next
          this.currentStreak = 0;
          this.feedbackType = "error";
          this.feedbackMsg = `Wrong! It was ${
            this.weekdays[this.testDate.getDay()]
          }`;
          setTimeout(() => this.generateTestQuestion(), 1000);
        }
      }
    },
  },
  beforeUnmount() {
    clearInterval(this.timerInterval);
  },
};
</script>

<style scoped>
/* BASE LAYOUT */
.savant-container {
  padding: 120px 10% 100px;
  max-width: 1400px;
  margin: 0 auto;
  min-height: 100vh;
  background: white;
  color: #111;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif;
}

.savant-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 60px;
  border-bottom: 1px solid #eee;
  padding-bottom: 40px;
}

.savant-title {
  font-size: clamp(3rem, 5vw, 5rem);
  font-weight: 900;
  line-height: 0.9;
  letter-spacing: -2px;
  margin: 0;
}

.serif {
  font-family: "Playfair Display", serif;
  font-style: italic;
}
.back-link {
  display: block;
  color: #999;
  text-decoration: none;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 0.8rem;
  margin-bottom: 20px;
}

/* MODES & RULES */
.mode-switcher {
  display: flex;
  gap: 10px;
  background: #f5f5f5;
  padding: 5px;
  border-radius: 50px;
}
.mode-btn {
  background: transparent;
  border: none;
  padding: 10px 25px;
  border-radius: 40px;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 1px;
  cursor: pointer;
  color: #999;
  transition: all 0.3s;
}
.mode-btn.active {
  background: white;
  color: #111;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.rules-btn {
  background: none;
  border: none;
  border-bottom: 1px solid #111;
  font-family: "Playfair Display", serif;
  font-style: italic;
  font-size: 1.1rem;
  cursor: pointer;
}

/* RULES PANEL */
.rules-panel {
  background: #111;
  color: white;
  padding: 40px;
  border-radius: 8px;
  margin-bottom: 60px;
}
.rules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
}
.rules-grid h3 {
  color: #888;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 20px;
}
.code-list {
  list-style: none;
  padding: 0;
}
.code-list li {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #333;
  padding: 8px 0;
  font-size: 0.9rem;
}
.code-list span {
  font-weight: 700;
  color: #ccc;
}

/* SHARED COMPONENTS */
.mode-section {
  max-width: 900px;
  margin: 0 auto;
}
.setup-controls h2 {
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 10px;
}
.action-btn {
  background: #111;
  color: white;
  border: none;
  padding: 15px 30px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  border-radius: 4px;
}
.action-btn:hover {
  background: #ff4444;
  transform: translateY(-2px);
}

/* CARDS & HISTORY */
.history-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.step-card {
  background: white;
  border: 1px solid #eee;
  padding: 25px;
  border-radius: 8px;
  transition: all 0.3s ease;
  position: relative;
}
.step-card.active {
  border-left: 5px solid #ff4444;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transform: scale(1.02);
  margin: 20px 0;
}
.step-card.completed {
  background: #fcfcfc;
  color: #555;
  border-left: 5px solid #8bac0f;
}

.step-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 10px;
}
.step-num {
  background: #111;
  color: white;
  width: 25px;
  height: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-size: 0.8rem;
  font-weight: 700;
}
.step-card.completed .step-num {
  background: #8bac0f;
}
.step-title {
  margin: 0;
  font-size: 1.2rem;
}

.interaction-area {
  margin-top: 20px;
}
.input-row {
  display: flex;
  gap: 20px;
  align-items: center;
  margin: 15px 0;
}
.input-row input,
.day-select {
  font-size: 1.5rem;
  width: 200px;
  border: none;
  border-bottom: 3px solid #111;
  background: transparent;
  font-weight: 700;
  text-align: center;
  padding: 5px;
}
.input-row input:focus,
.day-select:focus {
  outline: none;
  border-color: #ff4444;
}

.math-display {
  font-family: -apple-system, sans-serif;
  font-size: 1.1rem;
  color: #444;
  background: #eee;
  display: inline-block;
  padding: 4px 12px;
  border-radius: 4px;
}
.math-display.text-hint {
  font-family: -apple-system, sans-serif;
  background: #f0f7ff;
  color: #0056b3;
  line-height: 1.4;
}
.math-display.small {
  font-size: 0.9rem;
}

.completed-view {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 40px;
}
.result-badge {
  font-weight: 900;
  color: #111;
  font-size: 1.2rem;
}

/* CONFIG LAYOUT (3 Columns) */
.config-columns {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 30px;
  margin: 40px 0;
}
.col h3 {
  font-size: 0.9rem;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.checkbox-card {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 12px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: 0.2s;
  margin-bottom: 5px;
}
.checkbox-card:hover {
  background: #f9f9f9;
}
.checkbox-card input {
  width: 18px;
  height: 18px;
  accent-color: #111;
}
.checkbox-card span {
  font-weight: 600;
  font-size: 0.95rem;
}
.checkbox-card.highlight {
  background: #fff5f5;
  border: 1px solid #ffdcdc;
  border-radius: 4px;
}

/* COMPLETE STATE */
.complete-area {
  margin-top: 40px;
  text-align: center;
  animation: fadeIn 0.5s ease;
}
.success-banner {
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 20px;
  color: #8bac0f;
}
.review-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
  align-items: center;
}

.huge-date {
  font-family: "Playfair Display", serif;
  font-size: 2.5rem;
  font-weight: 700;
  display: block;
  margin-bottom: 30px;
}
.feedback {
  height: 20px;
  font-weight: 700;
  margin-top: 5px;
}
.feedback.success {
  color: #8bac0f;
}
.feedback.error {
  color: #ff4444;
}

/* TEST MODE & SETTINGS */
.test-setup {
  text-align: center;
  padding: 40px;
  background: #fafafa;
  border-radius: 12px;
}
.test-options {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin: 30px 0 40px;
}
.option-group h3 {
  font-size: 0.8rem;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 15px;
}
.pill-selector {
  display: flex;
  gap: 5px;
  background: #eee;
  padding: 5px;
  border-radius: 8px;
}
.pill-selector button {
  border: none;
  background: transparent;
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
}
.pill-selector button.active {
  background: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.hud-container {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-bottom: 40px;
}
.hud-item {
  text-align: center;
}
.hud-label {
  display: block;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #999;
}
.hud-value {
  font-size: 2rem;
  font-weight: 900;
}
.hud-value.fire.lit {
  color: #ff4444;
}
.hud-value.low {
  color: #ff4444;
  animation: pulse 1s infinite;
}

.weekday-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 30px;
}
.day-btn {
  padding: 15px 25px;
  background: white;
  border: 1px solid #eee;
  font-weight: 700;
  cursor: pointer;
  transition: 0.2s;
}
.day-btn:hover {
  background: #111;
  color: white;
  transform: translateY(-3px);
}

.stats-grid {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-bottom: 30px;
}
.stat-box {
  background: #f9f9f9;
  padding: 20px;
  min-width: 120px;
  border-radius: 8px;
}
.stat-box label {
  display: block;
  font-size: 0.8rem;
  text-transform: uppercase;
  color: #999;
}
.stat-box .val {
  font-size: 2rem;
  font-weight: 900;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes pulse {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    opacity: 1;
  }
}

.reset-link {
  background: none;
  border: none;
  text-decoration: underline;
  color: #999;
  margin-top: 30px;
  cursor: pointer;
}

@media (max-width: 800px) {
  .config-columns {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .test-options {
    flex-direction: column;
    gap: 20px;
  }
  .savant-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
  .mode-switcher {
    width: 100%;
    overflow-x: auto;
  }
}
</style>
