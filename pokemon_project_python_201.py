# 1. Ask for user input
# 2. Create a dynamic URL based on step 1
# 3. Fetch data from using url
# 4. Convert json to dictionary
# 5. Print Pokemon data
import requests

while True:
    # getting Pokemon name from the user
    user_pokemon_input = input(
        'Please type name of pokemon you want to learn about? ')

    # getting url with a name entered by user
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{user_pokemon_input.lower()}/'

    req = requests.get(pokemon_url)
    abilities = {}
    ability_name = []

    # checking if entered Pokemon name exists
    if req.status_code != 200:
        print('Incorrect Pokemon name, try again!')
        continue
    # if entered name exists, we get data and display some information about that Pokemon
    else:
        pokemon_character = req.json()
        pokemon_name = pokemon_character['name'].capitalize()
        print("******* DETAILS ABOUT POKEMON ******")
        print(f"Entered name: {pokemon_name}")
        print(f"{pokemon_name} weight: {pokemon_character['weight']}")
        print(f"{pokemon_name} height: {pokemon_character['height']}")
        # getting list of Pokemin abilities
        for value in pokemon_character['abilities']:
            # appending ability_name list
            ability_name.append(value['ability']['name'])
    # print(f"List of {pokemon_name} abilities: {ability_name}\n")
    print(f"List of {pokemon_name} abilities:")
    for index, ability in enumerate(ability_name):
        print(f'{index + 1}. {ability}')
    break
