<script setup lang="ts">
import { ref } from "vue";

import { listen } from "@tauri-apps/api/event";
import { PokemonName } from "../pokemonData";

const selectedPokemon = ref<PokemonName | null>(null);

const sprites = ref<string[] | null>(null);
const selectedSprite = ref<string | null>(null);

listen("pokemon-selected", (event) => {
  const payload = JSON.parse(event.payload as string);
  try {
    selectedPokemon.value = payload.name;
    sprites.value = payload.sprites;
    selectedSprite.value = sprites.value[0];
  } catch (error) {
    console.error(error);
  }
});

listen("sprite-selected", (event) => {
  selectedSprite.value = event.payload as string;
});
</script>

<template>
  <div class="flex items-center justify-center h-screen">
    <div class="p-8">
      <img
        v-if="selectedSprite"
        :src="selectedSprite"
        alt="Desk Buddy"
        class="w-48 h-48 object-cover mx-auto"
      />
    </div>
  </div>
</template>
