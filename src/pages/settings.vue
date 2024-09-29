<template>
  <h1>Settings</h1>
  <ul>
    <li
      v-for="pokemon in pokemonList"
      :key="pokemon"
      @click="selectPokemon(pokemon as PokemonName)"
    >
      {{ pokemon }}
    </li>
  </ul>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { PokemonName, pokemonNames, pokemonSprites } from "../pokemonData";
import { emit } from "@tauri-apps/api/event";

const pokemonList = ref(pokemonNames);

const selectPokemon = async (pokemon: PokemonName) => {
  emit("pokemon-selected", {
    name: pokemon,
    sprites: pokemonSprites[pokemon],
  });
};
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}

li {
  cursor: pointer;
}
</style>
