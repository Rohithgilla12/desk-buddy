<script setup lang="ts">
import { ref } from "vue";
import { PokemonName, pokemonSprites } from "./pokemonData";
import { WebviewWindow } from "@tauri-apps/api/window";

const selectedPokemon = ref<PokemonName>("pikachu");

const sprites = pokemonSprites[selectedPokemon.value];
console.log(sprites);

const openSettings = () => {
  try {
    console.log("Opening settings");

    const webview = new WebviewWindow("settings", {
      // url: "/settings.html",
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
</script>

<template>
  <nav>
    <button @click="openSettings">Settings</button>
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
