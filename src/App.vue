<script setup lang="ts">
import { listen } from "@tauri-apps/api/event";
import { WebviewWindow } from "@tauri-apps/api/window";
import { appWindow } from "@tauri-apps/api/window";

const openSettings = () => {
  try {
    const webview = new WebviewWindow("settings", {
      url: "/settings",
      title: "Settings",
      center: true,
    });
    // since the webview window is created asynchronously,
    // Tauri emits the `tauri://created` and `tauri://error` to notify you of the creation response
    webview.once("tauri://created", function () {
      // webview window successfully created
    });
    webview.once("tauri://error", function (e) {
      // an error occurred during webview window creation
      console.error(e);
    });
  } catch (error) {
    console.error(error);
  }
};

const toggleDecoration = async () => {
  try {
    const isDecorated = await appWindow.isDecorated();
    appWindow.setDecorations(!isDecorated);
  } catch (error) {
    console.error(error);
  }
};

const unlisten = listen("toggle-decoration", async (event) => {
  console.log(event);
  await toggleDecoration();
});
</script>

<template>
  <nav>
    <button class="absolute top-0 right-0 m-4 text-white" @click="openSettings">
      Settings
    </button>
  </nav>
  <RouterView />
</template>

<style scoped>
:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;

  color: #0f0f0f;
}
</style>
