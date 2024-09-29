<script setup lang="ts">
import { ref, watch } from "vue";

import { listen } from "@tauri-apps/api/event";
import { PokemonName, pokemonSprites } from "../pokemonData";

const selectedPokemon = ref<PokemonName | null>(null);

const sprites = ref<string[] | null>(null);

listen("pokemon-selected", (event) => {
  const payload = JSON.parse(event.payload as string);
  try {
    selectedPokemon.value = payload.name;
    sprites.value = payload.sprites;
  } catch (error) {
    console.error(error);
  }
});

watch(selectedPokemon, (newVal) => {
  console.log(newVal);
  if (newVal) {
    sprites.value = pokemonSprites[newVal];
  }
});
</script>

<template>
  <div class="flex items-center justify-center h-screen">
    <div class="p-8">
      <img
        v-if="sprites"
        :src="sprites[0]"
        alt="Desk Buddy"
        class="w-48 h-48 object-contain mx-auto"
      />
    </div>
  </div>
</template>
