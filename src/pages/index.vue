<script setup lang="ts">
import { ref } from "vue";

import { listen } from "@tauri-apps/api/event";
import { PokemonName } from "../pokemonData";
import { usePokemonStore } from "../stores/pokemonStore";

const store = usePokemonStore();
const selectedPokemon = ref<PokemonName>(store.selectedPokemon);

const selectedSprite = ref<string | null>(store.selectedSprite);

listen("pokemon-selected", (event) => {
  const payload = JSON.parse(event.payload as string);
  try {
    selectedPokemon.value = payload.name;
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
        class="w-24 h-24 object-contain mx-auto"
      />
    </div>
  </div>
</template>
