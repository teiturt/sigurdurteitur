<template>
  <main class="savant-container">
    <!-- Header / Navigation -->
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

    <!-- CONTENT AREA -->
    <div class="content-wrapper">
      <!-- RULES OVERLAY -->
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

      <!-- MODE: PRACTICE LAB (Default) -->
      <section v-if="currentMode === 'practice'" class="mode-section">
        <!-- Configuration Menu -->
        <div class="setup-controls" v-if="!practiceActive">
          <h2>Lab Configuration</h2>
          <p>Select exactly which mental steps you want to verify.</p>

          <div class="config-columns">
            <!-- Column 1: YEAR -->
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

            <!-- Column 2: MONTH -->
            <div class="col">
              <h3>Month Data</h3>
              <label class="checkbox-card">
                <input type="checkbox" v-model="practiceConfig.monthDoom" />
                <span>Month Anchor Date</span>
              </label>
            </div>

            <!-- Column 3: DAY (Final) -->
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

        <!-- Active Practice Session -->
        <div v-else class="practice-session">
          <div class="target-date">
            <span class="label">Solve For</span>
            <span class="huge-date">{{ practiceDateFormatted }}</span>
          </div>

          <!-- History (Notebook) -->
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

          <!-- Current Input Question -->
          <div
            class="step-card active practice-card"
            v-if="currentPracticeStep && !sessionComplete"
          >
            <div class="step-header">
              <span class="step-num">?</span>
              <h3 class="step-title">{{ currentPracticeStep.title }}</h3>
            </div>
            <div class="interaction-area">
              <div class="math-display">{{ currentPracticeStep.hint }}</div>
              <div class="input-row">
                <!-- Standard Number Input -->
                <input
                  v-if="currentPracticeStep.type !== 'dayName'"
                  type="number"
                  v-model.number="practiceInput"
                  @keyup.enter="checkPractice"
                  placeholder="..."
                  ref="pracInput"
                />
                <!-- Day Name Selector -->
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

          <!-- Session Complete -->
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

      <!-- MODE: TEST -->
      <section v-if="currentMode === 'test'" class="mode-section">
        <div class="test-header">
          <div class="score-board">
            Score: {{ testScore }} / {{ testTotal }}
          </div>
          <button class="action-btn" @click="generateTestQuestion">
            New Date
          </button>
        </div>

        <div v-if="testDate" class="test-area">
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

      // Practice State
      practiceActive: false,
      sessionComplete: false,
      practiceDate: null,

      // Granular Configuration
      practiceConfig: {
        // Year
        year12: true,
        yearRem: true,
        year4: true,
        century: false,
        yearDoom: false,
        // Month
        monthDoom: true,
        // Final
        dist: true, // Distance
        sum: true, // Final Sum
        finalName: true, // The Name (Sunday, etc)
      },

      practiceQueue: [],
      practiceHistory: [],
      practiceInput: "",
      feedbackMsg: "",
      feedbackType: "",

      // Test State
      testDate: null,
      testScore: 0,
      testTotal: 0,
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
      this.testDate = null;
      this.feedbackMsg = "";
    },

    // --- PRACTICE LOGIC ---
    startPractice() {
      // 1. Generate Date
      const year = 1900 + Math.floor(Math.random() * 200);
      const month = Math.floor(Math.random() * 12);
      const day = Math.floor(Math.random() * 28) + 1;
      this.practiceDate = new Date(year, month, day);

      // 2. Calculate Logic Values
      const v = this.getLogicValues(this.practiceDate);

      // 3. Reset State
      this.practiceQueue = [];
      this.practiceHistory = [];
      this.feedbackMsg = "";
      this.practiceInput = "";
      this.sessionComplete = false;

      // 4. Build Queue based on granular Checkboxes
      const c = this.practiceConfig;

      // Year Steps
      if (c.year12)
        this.practiceQueue.push({
          title: `Year: 12s`,
          hint: `${v.yy} ÷ 12`,
          answer: v.step1,
          math: `${v.yy} ÷ 12 =`,
        });
      if (c.yearRem)
        this.practiceQueue.push({
          title: `Year: Remainder`,
          hint: `Remainder of above`,
          answer: v.step2,
          math: `${v.yy} % 12 =`,
        });
      if (c.year4)
        this.practiceQueue.push({
          title: `Year: 4s`,
          hint: `(${v.step2} ÷ 4)`,
          answer: v.step3,
          math: `${v.step2} ÷ 4 =`,
        });
      if (c.century)
        this.practiceQueue.push({
          title: `Century Anchor (${Math.floor(year / 100)}00s)`,
          hint: `18=5, 19=3, 20=2`,
          answer: v.centuryAnchor,
          math: `Anchor =`,
        });
      if (c.yearDoom)
        this.practiceQueue.push({
          title: `Year Doomsday`,
          hint: `Sum all above % 7`,
          answer: v.yearDoomsday,
          math: `Year Doom =`,
        });

      // Month Step
      if (c.monthDoom)
        this.practiceQueue.push({
          title: `Month Doomsday Date`,
          hint: `For ${this.months[month]}`,
          answer: v.monthDoomDate,
          math: `${this.months[month]} Doom =`,
        });

      // Final Steps Logic
      const distance = v.day - v.monthDoomDate;
      const rawSum = v.yearDoomsday + distance;
      const finalDayIndex = ((rawSum % 7) + 7) % 7;

      if (c.dist)
        this.practiceQueue.push({
          title: `Distance`,
          hint: `Day (${v.day}) - Month Doom (${v.monthDoomDate})`,
          answer: distance,
          math: `Dist =`,
        });

      if (c.sum)
        this.practiceQueue.push({
          title: `Calculation Sum`,
          hint: `Year Doom (${v.yearDoomsday}) + Distance (${distance})`,
          answer: rawSum,
          math: `Sum =`,
        });

      if (c.finalName)
        this.practiceQueue.push({
          title: `Final Weekday`,
          hint: `Convert to Day Name`,
          answer: this.weekdays[finalDayIndex],
          type: "dayName",
          math: `Day =`,
        });

      // Validation
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
        this.feedbackMsg = "Incorrect";
      }
    },

    stopPractice() {
      this.practiceActive = false;
      this.sessionComplete = false;
      this.practiceQueue = [];
      this.practiceHistory = [];
    },

    // --- TEST LOGIC ---
    generateTestQuestion() {
      this.feedbackMsg = "";
      const start = new Date(1950, 0, 1);
      const end = new Date(2050, 11, 31);
      this.testDate = new Date(
        start.getTime() + Math.random() * (end.getTime() - start.getTime()),
      );
    },
    submitTest(dayIndex) {
      this.testTotal++;
      if (dayIndex === this.testDate.getDay()) {
        this.testScore++;
        this.feedbackType = "success";
        this.feedbackMsg = "Correct!";
        setTimeout(() => this.generateTestQuestion(), 800);
      } else {
        this.feedbackType = "error";
        this.feedbackMsg = `Incorrect. It was ${
          this.weekdays[this.testDate.getDay()]
        }`;
      }
    },
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
}
.action-btn:hover {
  background: var(--ueno-orange, #ff4444);
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
  border-left: 5px solid var(--ueno-orange, #ff4444);
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
  width: 150px;
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
  border-color: var(--ueno-orange, #ff4444);
}

.math-display {
  font-family: monospace;
  font-size: 1.1rem;
  color: #666;
  background: #eee;
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
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

/* TEST MODE */
.test-area {
  text-align: center;
  margin-top: 60px;
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
