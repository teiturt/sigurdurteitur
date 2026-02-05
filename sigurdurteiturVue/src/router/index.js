import { createRouter, createWebHistory } from "vue-router";
import AboutView from "../views/AboutView.vue";
import ExperienceView from "../views/ExperienceView.vue";
import FocusView from "../views/FocusView.vue";
import GameHubView from "../views/GameHubView.vue";
import VoidPilot from "../views/VoidPilot.vue";
import HomeView from "../views/HomeView.vue";
import ContactView from "../views/ContactView.vue";
import ConsoleView from "../views/ConsoleView.vue";
import DayGuesser from "../components/DayGuesser.vue";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  { path: "/about", name: "About", component: AboutView },
  { path: "/experience", name: "Work", component: ExperienceView },
  { path: "/focus", name: "Focus", component: FocusView },
  { path: "/games", name: "Play", component: GameHubView },
  { path: "/games/void-pilot", name: "VoidPilot", component: VoidPilot },
  { path: "/games/console", name: "Console", component: ConsoleView },
  { path: "/contact", name: "Contact", component: ContactView },
  { path: "/games/day-guesser", name: "DayGuesser", component: DayGuesser },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

export default router;
