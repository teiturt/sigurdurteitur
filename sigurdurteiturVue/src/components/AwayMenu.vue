<!-- AwayMenu.vue -->
<template>
  <div class="menu-container">
    <!-- Configuration Header -->
    <TestConfig
      :language="language"
      :mode="mode"
      :timeLimit="timeLimit"
      :wordCount="wordCount"
      @update:language="language = $event"
      @update:mode="mode = $event"
      @update:timeLimit="timeLimit = $event"
      @update:wordCount="wordCount = $event"
      @start-test="startTest"
    />

    <!-- Pass additional props to TypingDisplay -->
    <TypingDisplay 
      :words="words"
      :mode="mode"
      :timeLimit="timeLimit"
      :wordCount="wordCount"
    />
    
    <h2>Welcome to my Away Menu, It does not work</h2>
    <button @click="$emit('goBack')">Go Back Home</button>
  </div>
</template>

<script>
import TestConfig from "@/components/TestConfig.vue";
import TypingDisplay from "@/components/TypingDisplay.vue";

export default {
  name: "AwayMenu",
  components: {
    TestConfig,
    TypingDisplay 
  },
  emits: ["goBack"],
  data() {
    return {
      language: "english",
      mode: "time",       // default mode: 'time' or 'words'
      timeLimit: 10,      // default time limit in seconds for time mode
      wordCount: 15,      // default word count for words mode
      words: [
      "the", "of", "and", "a", "to", "in", "is", "you", "that", "it",
      "he", "was", "for", "on", "are", "as", "with", "his", "they", "I",
      "at", "be", "this", "have", "from", "or", "one", "had", "by", "word",
      "but", "not", "what", "all", "were", "we", "when", "your", "can", "said",
      "there", "use", "an", "each", "which", "she", "do", "how", "their", "if",
      "will", "up", "other", "about", "out", "many", "then", "them", "these", "so",
      "some", "her", "would", "make", "like", "him", "into", "time", "has", "look",
      "two", "more", "write", "go", "see", "number", "no", "way", "could", "people",
      "my", "than", "first", "water", "been", "call", "who", "oil", "its", "now",
      "find", "long", "down", "day", "did", "get", "come", "made", "may", "part",
      "over", "new", "sound", "take", "only", "little", "work", "know", "place", "year",
      "live", "me", "back", "give", "most", "very", "after", "thing", "our", "just",
      "name", "good", "sentence", "man", "think", "say", "great", "where", "help", "through",
      "much", "before", "line", "right", "too", "mean", "old", "any", "same", "tell",
      "boy", "follow", "came", "want", "show", "also", "around", "form", "three", "small",
      "set", "put", "end", "does", "another", "well", "large", "must", "big", "even",
      "such", "because", "turn", "here", "why", "ask", "went", "men", "read", "need",
      "land", "different", "home", "us", "move", "try", "kind", "hand", "picture", "again",
      "change", "off", "play", "spell", "air", "away", "animal", "house", "point", "page",
      "letter", "mother", "answer", "found", "study", "still", "learn", "should", "iceland", "world"
    ]
};
  },
  methods: {
    startTest() {
      console.log("Test started with configuration:", {
        language: this.language,
        mode: this.mode,
        timeLimit: this.timeLimit,
        wordCount: this.wordCount
      });
      // Add your test-start logic here.
    }
  }
};
</script>

<style scoped>
.menu-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
  text-align: center;
  z-index: 5;
  background: transparent;
  padding: 20px;
  width: 100vw;
  height: 100vh;
}
</style>
