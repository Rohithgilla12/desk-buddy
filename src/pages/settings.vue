<script setup lang="ts">
import { ref, computed } from "vue";
import { PokemonName, pokemonNames, pokemonSprites } from "../pokemonData";
import { emit } from "@tauri-apps/api/event";

const pokemonList = ref(pokemonNames);
const searchQuery = ref("");

const filteredPokemonList = computed(() => {
  return pokemonList.value.filter((pokemon) =>
    pokemon.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const selectPokemon = async (pokemon: PokemonName) => {
  emit("pokemon-selected", {
    name: pokemon,
    sprites: pokemonSprites[pokemon],
  });
};
</script>

<template>
  <div
    class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12"
  >
    <div class="relative py-3 sm:max-w-xl sm:mx-auto">
      <div
        class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20"
      >
        <h1 class="text-2xl font-semibold mb-6 text-center text-gray-900">
          Settings
        </h1>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search Pokémon"
          class="mb-4 p-2 border rounded"
        />
        <div class="grid grid-cols-4 gap-4">
          <!-- Increased columns to 4 -->
          <div
            v-for="pokemon in filteredPokemonList"
            :key="pokemon"
            @click="selectPokemon(pokemon as PokemonName)"
            class="p-2 hover:bg-gray-100 rounded cursor-pointer transition duration-150 ease-in-out flex flex-col items-center"
          >
            <img
              :src="pokemonSprites[pokemon as PokemonName][0]"
              alt=""
              class="w-16 h-16 mb-2"
            />
            <span>{{ pokemon }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}

li {
  cursor: pointer;
}
</style>
