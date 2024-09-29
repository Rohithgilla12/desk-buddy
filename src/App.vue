<script setup lang="ts">
import { ref } from "vue";
import { PokemonName, pokemonSprites } from "./pokemonData";

const selectedPokemon = ref<PokemonName>("pikachu");

const sprites = pokemonSprites[selectedPokemon.value];
console.log(sprites);
</script>

<template>
  <div class="container">
    <img :src="sprites[1]" alt="Desk Buddy" />
  </div>
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
