import os
import re
import json

# Directory containing your Pokémon GIFs
ASSETS_DIR = "../public/pokemon-assets"

# Output assets directory
OUTPUT_DIR = "/pokemon-assets"

# Output JSON file
OUTPUT_FILE = "../public/pokemonData.json"


def get_base_pokemon_name(filename):
    """
    Extracts the base Pokémon name from a filename by removing variant suffixes.
    """
    # Remove file extension
    name = os.path.splitext(filename)[0]

    # Regular expression to match variant suffixes
    variant_pattern = re.compile(
        r"(-mega.*|-gmax|-alola.*|-galar.*|-hisui.*|-2|-3|-4|-5|-f|-[a-z]+)$",
        re.IGNORECASE,
    )

    # Remove variant suffixes to get the base name
    base_name = variant_pattern.sub("", name)

    # Replace underscores with hyphens if necessary
    base_name = base_name.replace("_", "-")

    return base_name.lower()


def organize_pokemon_assets():
    # Dictionary to hold the Pokémon data
    pokemon_data = {}

    # List all files in the assets directory
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith(".gif"):
            # Get the full path of the file
            filepath = os.path.join(OUTPUT_DIR, filename)

            # Get the base Pokémon name
            base_name = get_base_pokemon_name(filename)

            # Initialize the list for this Pokémon if not already present
            if base_name not in pokemon_data:
                pokemon_data[base_name] = []

            # Add the file path to the list of variants
            pokemon_data[base_name].append(filepath)

    # Output the data to a JSON file
    with open(OUTPUT_FILE, "w") as f:
        json.dump(pokemon_data, f, indent=2)

    print(f"Pokémon data has been organized and saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    organize_pokemon_assets()
