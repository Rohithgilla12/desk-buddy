<script setup lang="ts">
import { ref, computed } from "vue";
import { PokemonName, pokemonNames, pokemonSprites } from "../pokemonData";
import { usePokemonStore } from "../stores/pokemonStore";
import { emit } from "@tauri-apps/api/event";

const pokemonStore = usePokemonStore();

const pokemonList = ref(pokemonNames);
const searchQuery = ref("");
const selectedPokemon = ref<PokemonName | null>(null); // Track selected Pokémon

const filteredPokemonList = computed(() => {
  return pokemonList.value.filter((pokemon) =>
    pokemon.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const selectPokemon = async (pokemon: PokemonName) => {
  selectedPokemon.value = pokemon; // Update selected Pokémon
  pokemonStore.selectPokemon(pokemon);
  emit("pokemon-selected", {
    name: pokemon,
    sprites: pokemonSprites[pokemon],
  });
};

const selectSprite = (sprite: string) => {
  pokemonStore.selectSprite(sprite);
  emit("sprite-selected", sprite);
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
        <div class="mb-4">
          <span class="font-semibold">Current Pokemon:</span>
          <span class="ml-2">{{ selectedPokemon }}</span>
        </div>

        <div class="mb-4">
          <span class="font-semibold">Sprite:</span>
          <div class="flex flex-wrap">
            <img
              v-for="sprite in pokemonStore.sprites"
              :key="sprite"
              :src="sprite"
              alt="Sprite"
              @click="selectSprite(sprite)"
              class="w-16 h-16 mb-2 cursor-pointer"
              :class="{
                'border-2 border-blue-500 rounded-lg p-1':
                  pokemonStore.selectedSprite === sprite,
              }"
            />
          </div>
        </div>

        <!-- Search for Pokémon -->
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search Pokémon"
          class="mb-4 p-2 border rounded"
        />
        <div class="grid grid-cols-4 gap-4">
          <div
            v-for="pokemon in filteredPokemonList"
            :key="pokemon"
            @click="selectPokemon(pokemon as PokemonName)"
            :class="[
              'p-2 rounded cursor-pointer transition duration-150 ease-in-out flex flex-col items-center',
              {
                'border-2 border-blue-500 rounded-lg':
                  selectedPokemon === pokemon,
              },
            ]"
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
