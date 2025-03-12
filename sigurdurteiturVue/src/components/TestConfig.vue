<!-- TestConfig.vue -->
<template>
  <header class="test-config">
    <!-- Language Toggle (Always on the far left) -->
    <div class="language-toggle">
      <button @click="toggleLanguage" class="textButton language-btn" tabindex="-1">
        {{ language === 'english' ? 'English' : 'Icelandic' }}
      </button>
    </div>

    <!-- Mode & Setting Row: Centered -->
    <div class="mode-setting-row">
      <!-- Typing Mode Toggle -->
      <div class="typing-mode">
        <button
          @click="setMode('time')"
          :class="{ active: mode === 'time' }"
          class="textButton"
          tabindex="-1"
        >
          Time
        </button>
        <button
          @click="setMode('words')"
          :class="{ active: mode === 'words' }"
          class="textButton"
          tabindex="-1"
        >
          Words
        </button>
      </div>

      <!-- Options for the Selected Mode -->
      <div class="setting-options">
        <template v-if="mode === 'time'">
          <button
            @click="updateTimeLimit(10)"
            :class="{ active: timeLimit === 10 }"
            class="textButton"
            tabindex="-1"
          >
            10 Seconds
          </button>
          <button
            @click="updateTimeLimit(30)"
            :class="{ active: timeLimit === 30 }"
            class="textButton"
            tabindex="-1"
          >
            30 Seconds
          </button>
        </template>
        <template v-else>
          <button
            @click="updateWordCount(15)"
            :class="{ active: wordCount === 15 }"
            class="textButton"
            tabindex="-1"
          >
            15 Words
          </button>
          <button
            @click="updateWordCount(50)"
            :class="{ active: wordCount === 50 }"
            class="textButton"
            tabindex="-1"
          >
            50 Words
          </button>
        </template>
      </div>
    </div>

  </header>
</template>

<script>
export default {
  name: "TestConfig",
  props: {
    language: { type: String, default: "english" },
    mode: { type: String, default: "time" }, // 'time' or 'words'
    timeLimit: { type: Number, default: 10 },
    wordCount: { type: Number, default: 15 }
  },
  methods: {
    toggleLanguage() {
      const newLang = this.language === "english" ? "icelandic" : "english";
      this.$emit("update:language", newLang);
    },
    setMode(selectedMode) {
      this.$emit("update:mode", selectedMode);
    },
    updateTimeLimit(limit) {
      this.$emit("update:timeLimit", limit);
    },
    updateWordCount(count) {
      this.$emit("update:wordCount", count);
    },
    startTest() {
      this.$emit("start-test");
    }
  }
};
</script>

<style scoped>
.test-config {
  background: #f3f4f6;
  padding: 1rem;
  border-radius: 8px;
  width: 100%;
  position: relative;
  height: 20vh;
}

/* Language Toggle: positioned to the far left */
.language-toggle {
  position: absolute;
  left: 1rem;
  top: 1rem;
}
.language-btn {
  /* Always styled as active */
  background-color: #3182ce;
  color: rgb(0, 0, 0);
  padding: 0.5rem 1rem;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
}

/* Mode & Setting Row: centered horizontally */
.mode-setting-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  margin-top: 0rem; /* Enough space below the language toggle */
}
.typing-mode,
.setting-options {
  display: flex;
  gap: 0.5rem;
}

/* Base styles for buttons */
.textButton {
  border: none;
  background: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 4px;
  transition: background 0.2s, color 0.2s;
}
.textButton:hover {
  background-color: #e2e8f0;
}
.textButton.active {
  background-color: #3182ce;
  color: white;
}

/* Start Button styling */
.start-button-container {
  text-align: center;
  margin-top: 1rem;
}
.start-test-btn {
  background: #3182ce;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
