<!-- TypingDisplay.vue -->
<template>
    <div class="typing-display">
      <!-- Progress / Timer Display -->
      <p class="progress-info">
        <template v-if="mode === 'time'">
          Time remaining: {{ timeLimit - timeElapsed }} seconds
        </template>
        <template v-else>
          {{ currentWordIndex }} / {{ effectiveWords.length }} words completed
        </template>
      </p>
  
      <!-- Typing Test Area -->
      <div v-if="!testCompleted" class="text-display" ref="typingContainer">
        <div v-for="(line, lineIndex) in visibleLines" :key="lineIndex" class="line">
            <div class="line-words">
            <span v-for="word in line" :key="word.index" class="word">
                <template v-if="word.index < currentWordIndex">
                <span :class="completedWordWrapperClass(word)">
                    <span
                    v-for="(letter, letterIndex) in word.text.split('')"
                    :key="letterIndex"
                    :class="completedLetterClass(word, letterIndex)"
                    >
                    {{ letter }}
                    </span>
                </span>
                </template>
                <template v-else-if="word.index === currentWordIndex">
                <span
                    v-for="(letter, letterIndex) in word.text.split('')"
                    :key="letterIndex"
                    :class="letterClass(word, letterIndex)"
                >
                    {{ letter }}
                </span>
                </template>
                <template v-else>
                <span class="static-word">{{ word.text }}</span>
                </template>
            </span>
            </div>
        </div>
       </div>


  
      <!-- Results Section -->
      <div v-else class="results-section">
        <div class="results-info">
          <h2>Results</h2>
          <p>Correct WPM: <span>{{ wpm }}</span></p>
          <p>Raw WPM: <span>{{ rawWpm }}</span></p>
          <p>Accuracy: <span>{{ accuracy }}%</span></p>
          <p>Time: <span>{{ timeElapsed }} seconds</span></p>
        </div>
      </div>
  
      <!-- Restart Button (always visible) -->
      <button @click="restartTest" class="restart-btn">Restart Test</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "TypingDisplay",
    props: {
      words: {
        type: Array,
        required: true
      },
      mode: { type: String, default: "words" },
      timeLimit: { type: Number, default: 15 },
      wordCount: { type: Number, default: 25 }
    },
    data() {
      return {
        currentWordIndex: 0,
        typedLetters: "",
        wordStatuses: [],
        extraCharacters: {},
        completedInputs: [],
        testInProgress: false,
        testCompleted: false,
        timeElapsed: 0,
        timer: null,
        wpm: 0,
        rawWpm: 0,
        accuracy: 0,
        visibleLines: []
      };
    },
    computed: {
      effectiveWords() {
        return this.mode === "words"
          ? this.words.slice(0, this.wordCount)
          : this.words;
      },
      activeLineIndex() {
        return this.visibleLines.findIndex(line =>
          line.some(word => word.index === this.currentWordIndex)
        );
      }
    },
    methods: {
      // For the active word letters (dynamic)
      letterClass(word, letterIndex) {
        if (letterIndex === this.typedLetters.length) {
          return "current"; // next letter: blue
        }
        if (letterIndex < this.typedLetters.length) {
          return this.typedLetters[letterIndex] === word.text[letterIndex]
            ? "correct"
            : "incorrect";
        }
        return "untyped";
      },
      
      startTest() {
        this.testInProgress = true;
        this.testCompleted = false;
        this.currentWordIndex = 0;
        this.typedLetters = "";
        this.wordStatuses = [];
        this.extraCharacters = {};
        this.completedInputs = [];
        this.timeElapsed = 0;
        this.startTimer();
        this.$nextTick(() => {
          this.updateVisibleLines();
        });
        console.log("Test started");
      },
      endTest() {
        this.testInProgress = false;
        this.testCompleted = true;
        this.stopTimer();
        const totalChars = this.effectiveWords.join("").length;
        let correctChars = 0;
        this.effectiveWords.forEach((word, index) => {
          if (this.wordStatuses[index] === "correct") {
            correctChars += word.length;
          }
        });
        this.accuracy =
          totalChars > 0 ? Math.round((correctChars / totalChars) * 100) : 0;
        const elapsedMinutes = this.timeElapsed / 60 || (1 / 60);
        this.wpm = Math.round((correctChars / 5) / elapsedMinutes);
        this.rawWpm = Math.round(
          ((this.effectiveWords.slice(0, this.currentWordIndex).join("").length +
            this.typedLetters.length) /
            5) /
            elapsedMinutes
        );
        console.log("Test ended");
      },
      startTimer() {
        if (this.timer) return;
        this.timer = setInterval(() => {
          this.timeElapsed++;
          if (this.mode === "time" && this.timeElapsed >= this.timeLimit) {
            this.endTest();
          }
        }, 1000);
      },
      stopTimer() {
        if (this.timer) {
          clearInterval(this.timer);
          this.timer = null;
        }
      },
      handleTyping(event) {
        if (event.key === "Tab") {
          event.preventDefault();
          this.restartTest();
          return;
        }
        if (!this.testInProgress && !this.testCompleted && event.key.length === 1 && /^[A-Za-z]$/.test(event.key)) {
          this.startTest();
        }
        if (!this.testInProgress) return;
        const key = event.key;
        if (key === " ") {
            if (this.typedLetters.trim() === "") return;
            const currentWord = this.effectiveWords[this.currentWordIndex];
            const isCorrect = this.typedLetters.trim() === currentWord;
            this.wordStatuses[this.currentWordIndex] = isCorrect ? "correct" : "incorrect";
            // Store the typed input for later letter-by-letter comparison.
            this.completedInputs = this.completedInputs || [];
            this.completedInputs[this.currentWordIndex] = this.typedLetters.trim();
            this.currentWordIndex++;
            this.typedLetters = "";
            this.updateVisibleLines();
            if (this.currentWordIndex >= this.effectiveWords.length) {
                this.endTest();
            }
            event.preventDefault();
            return;
            }


        if (key === "Backspace") {
          this.typedLetters = this.typedLetters.slice(0, -1);
          return;
        }
        if (key.length === 1) {
          this.typedLetters += key;
        }
      },
      updateVisibleLines() {
  const container = this.$refs.typingContainer;
  if (!container) return;
  const gap = 12; // gap between words in pixels
  const maxLineWidth = container.clientWidth * 0.8; // maximum width for a line
  const allLines = [];
  let currentLine = [];
  let currentLineWidth = 0;
  // Map effectiveWords to objects that include their index
  const wordObjects = this.effectiveWords.map((w, idx) => ({ text: w, index: idx }));
  wordObjects.forEach(word => {
    const wordWidth = this.measureWordWidth(word.text, container);
    if (currentLine.length === 0 || currentLineWidth + gap + wordWidth <= maxLineWidth) {
      if (currentLine.length > 0) {
        currentLineWidth += gap;
      }
      currentLine.push(word);
      currentLineWidth += wordWidth;
    } else {
      allLines.push(currentLine);
      currentLine = [word];
      currentLineWidth = wordWidth;
    }
  });
  if (currentLine.length) {
    allLines.push(currentLine);
  }
  
  // Limit display to a maximum of 3 lines
  const maxLines = 3;
  let currentWordLine = allLines.findIndex(line =>
    line.some(word => word.index === this.currentWordIndex)
  );
  let startLineIndex = 0;
  if (currentWordLine !== -1 && allLines.length > maxLines) {
    if (currentWordLine <= 1) {
      startLineIndex = 0;
    } else if (currentWordLine >= allLines.length - 2) {
      startLineIndex = allLines.length - maxLines;
    } else {
      startLineIndex = currentWordLine - 1;
    }
  }
  this.visibleLines = allLines.slice(startLineIndex, startLineIndex + maxLines);
},


      completedLetterClass(word, letterIndex) {
        // Use the stored completed input for the word (or an empty string if not available)
        const typed = this.completedInputs[word.index] || "";
        if (letterIndex < typed.length) {
            return typed[letterIndex] === word.text[letterIndex] ? "correct" : "incorrect";
        }
        return "untyped";
        },
        completedWordWrapperClass(word) {
        // If the completed input does not exactly match, add a red underline.
        const typed = this.completedInputs[word.index] || "";
        return typed === word.text ? "" : "incorrect-word";
        },


      measureWordWidth(text, container) {
        const font = window.getComputedStyle(container).font;
        const canvas = document.createElement("canvas");
        const context = canvas.getContext("2d");
        context.font = font;
        return context.measureText(text + "  ").width;
      },
      restartTest() {
        this.testInProgress = false;
        this.testCompleted = false;
        this.stopTimer();
        this.currentWordIndex = 0;
        this.typedLetters = "";
        this.wordStatuses = [];
        this.extraCharacters = {};
        this.completedInputs = [];
        this.timeElapsed = 0;
        this.updateVisibleLines();
        console.log("Test restarted");
      }
    },
    mounted() {
      this.updateVisibleLines();
      document.addEventListener("keydown", this.handleTyping);
      window.addEventListener("resize", this.updateVisibleLines);
    },
    beforeUnmount() {
      document.removeEventListener("keydown", this.handleTyping);
      window.removeEventListener("resize", this.updateVisibleLines);
      this.stopTimer();
    },
    watch: {
    wordCount() {
        this.updateVisibleLines();
    },
    mode() {
        this.updateVisibleLines();
    },
    words() {
        this.updateVisibleLines();
    }
    }

  };
  </script>
  
  <style scoped>
  .typing-display {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  .progress-info {
    margin-bottom: 1rem;
    font-size: 1.2rem;
  }
  .text-display {
    min-height: 120px;
    margin-bottom: 1rem;
    text-align: center;
    overflow: hidden;
  }
  .line {
    display: flex;
    justify-content: center;
    margin-bottom: 0.5rem;
  }
  .line-words {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .word {
    display: inline-block;
    margin-right: 12px;
    font-size: 1.5rem;
  }
  .static-word {
    color: gray;
  }
  .correct {
    color: black;
  }
  .incorrect {
    color: red;
  }
  .untyped {
    color: gray;
  }
  .current {
    color: blue;
  }
  .extra-characters {
    color: rgba(255, 0, 0, 0.5);
    font-size: 1.5rem;
  }
  .incorrect-word {
    border-bottom: 2px solid red;
  }
  .restart-btn {
    background: #3182ce;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
  }
  .results-section {
    margin-top: 1rem;
  }
  </style>
  