import { defineStore } from "pinia";
import { ref } from "vue";
import { PokemonName, pokemonSprites } from "../pokemonData";

export const usePokemonStore = defineStore(
  "pokemon",
  () => {
    const selectedPokemon = ref<PokemonName>("pikachu");
    const sprites = ref(pokemonSprites[selectedPokemon.value]);
    const selectedSprite = ref(sprites.value[0]);

    function selectPokemon(pokemon: PokemonName) {
      selectedPokemon.value = pokemon;
      sprites.value = pokemonSprites[pokemon];
      selectedSprite.value = sprites.value[0];
    }

    function selectSprite(sprite: string) {
      selectedSprite.value = sprite;
    }

    return {
      selectedPokemon,
      sprites,
      selectedSprite,
      selectPokemon,
      selectSprite,
    };
  },
  {
    persist: true,
  }
);
