// composables/useTimer.js
import { ref, onUnmounted } from 'vue';

export function useTimer() {
  const timeElapsed = ref(0);
  let timer = null;

  const startTimer = () => {
    if (timer) return;
    timer = setInterval(() => {
      timeElapsed.value++;
    }, 1000);
  };

  const stopTimer = () => {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  };

  onUnmounted(() => {
    stopTimer();
  });

  return { timeElapsed, startTimer, stopTimer };
}
