import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { routes } from "vue-router/auto-routes";
import App from "./App.vue";
import "./index.css";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(pinia).use(router).mount("#app");
