#Chloe 
#11/20/24
#Pokemon evolution game
#init
pokemonlvl=0
pokemon_name1 = "Ralts"
pokemon_name2 = "Kirlia"
pokemon_name3 = "Gardevior"
import random

#func
def draw_ralts():
    print("""
⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟥🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬛🟥🟥🟥🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬛🟥🟥🟥🟥🟩🟩⬛⬛⬜⬜
⬜⬛🟥🟥🟥🟩🟩🟩🟩🟩⬛⬜
⬛🟩⬛🟥🟩🟩🟩🟩🟩🟩⬛⬜
⬛🟩🟩⬛🟩🟩🟩🟩🟩🟩🟩⬛
⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟩⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜
⬜⬜⬜⬛🌫️⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜🌫️⬜⬛⬜⬜⬜
⬜⬜⬛⬜🌫️⬜🏽⬜⬛⬛⬜⬜
⬜⬜⬛⬜🏽⬜⬜⬛⬜⬜⬛⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜""")
def draw_kirlia():
    print("""
⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟥⬛⬛🟩🟩🟩🟩🟩⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟥🟩🟩🟩🟩🟩🟩⬛🟥🟥⬛⬜⬜⬜
⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬛🟥🟥🟥⬛⬜⬜⬜
⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬛🟥⬛⬛⬛⬜⬜⬜
⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩🟩🟩⬛⬜⬜
⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩🟩🟩⬛⬜⬜
⬜⬛🟩⬛🟩🟩🟩🟩🟩🟩⬛⬛🟩🟩🟩🟩⬛⬜
⬛🟩🟩⬛🟩🟩🟩🟩⬛⬛⬜⬛🟩🟩🟩🟩⬛⬜
⬛🟩🟩🟩⬛🟩🟩⬛🌫️🟥⬜🌫️⬛🟩🟩🟩⬛⬜
⬜⬛🟩🟩⬛⬛⬛🌫️🌫️🌫️🌫️⬛⬛🟩🟩🟩🟩⬛
⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬜⬛🟩🟩🟩🟩⬛
⬜⬜⬜⬜⬜⬛⬜⬜🌫️🌫️🌫️⬛⬛🟩🟩🟩⬛⬜
⬜⬜⬜⬜⬛⬜⬛⬛🌫️⬜⬜⬜⬛⬛⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜🌫️🌫️🌫️⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🌫️🌫️🌫️⬛🌫️🌫️🌫️⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟩⬛🌫️🌫️⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟩⬛⬜⬜🌫️⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_gardevior():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣿⣷⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣻⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⡻⣿⣿⣿⣷⡹⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣦⡉⠙⠻⢿⣿⣿⣿⣿⡌⢿⣿⣿⣧⢿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣟⡓⠀⠀⠀⡉⢻⣿⣿⣿⡸⣿⣿⡿⣸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡆⡀⠐⢄⣼⣿⣿⣿⡇⣿⡿⢣⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⣄⠉⣁⣈⡿⠸⣋⡵⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠿⠀⠻⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣇⠀⠀⠈⢿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⣿⣿⡀⠀⢰⣾⣷⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠘⣿⣷⣤⣸⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠈⢿⠿⠿⣿⣿⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⢙⠇⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠞⡄⠀⢻⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠈⠜⢄⠀⢻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠘⡌⢢⠀⢻⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⢱⠀⠱⡀⠹⣿⣿⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠱⡀⠘⢿⣿⣿⣷⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⢱⠀⠀⠉⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠚⠁⠀⠀⢀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣤⠤⠶⠚⠉⠁⠀⠀⣀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠶⠒⠒⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⣀⣀⣀⠤⠤⠤⠔⠒⠊⠁⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡴⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠴⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠃⡆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⢀⠃⠀⠀⠀⠀⠀
⠀⢠⠖⠁⠀⠀⢀⣀⡀⠤⠤⠄⠒⠒⠒⠒⠓⠊⠉⠉⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⡿⠁⡜⠀⠀⠀⠀⠀⠀
⣰⡣⠤⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⢀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠁⡜⠀⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⡤⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠟⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⠟⠁⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⣀⠴⠚⠛⠻⣿⣿⡿⠛⢁⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡠⠖⠉⠀⠀⠀⠀⠀⠈⠓⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
#Increases pokemon level by 1
def train():
    global pokemonlvl
    pokemonlvl= pokemonlvl+1
    print("Level " + str(pokemonlvl))
def win():
    global pokemonlvl
    pokemonlvl = pokemonlvl+2
    print("Level " + str(pokemonlvl))
def lose():
    global pokemonlvl
    pokemonlvl = pokemonlvl+0
    print("Level " + str(pokemonlvl))
#Plays a chance game and if won, levels up the pokemon by 2
def battle():
    if random.randint(1, 2) == 1:
        print("Oh no! Your pokemon was too weak, train more and try again!")
        lose()
    else:
        print("Your pokemon won! Good job and keep getting stronger!")
        win()
def win():
    global pokemonlvl
    pokemonlvl = pokemonlvl+2
    print("Level " + str(pokemonlvl))
#tells if pokemon is ready to evolve
def evolve_pokemon():
    if pokemonlvl<5:
        print("Your pokemon is not ready to evolve yet")
    if 5<=pokemonlvl<10:
        print("Your pokemon is not ready to evolve yet")
    if pokemonlvl>=10:
        print("Your pokemon is fully evolved")
#shows pokemon name, level, and looks of current evolution
def display_pokemon():
    if pokemonlvl<5:
        print(str(pokemon_name1) + ":" + "Level " + str(pokemonlvl))
        evolve_pokemon()
        print
        draw_ralts()
    if 5<=pokemonlvl<10:
        print(str(pokemon_name2) + ":" + "Level " + str(pokemonlvl))
        evolve_pokemon()
        draw_kirlia()
    if pokemonlvl>=10:
        print(str(pokemon_name3) + ":" + "Level " + str(pokemonlvl))
        evolve_pokemon()
        draw_gardevior()

def pokemon_game():
    print("Welcome to Pokemon Evolution Simulator")
while True:
    print("""Please chose what to do with your pokemon.
    1. Train: increases pokemon level by 1
    2. Gym Battle: increases pokemon level by 2 if pokemon wins
    3. Information: pokemon evolution and level
    4. Quit""")
    action = input("(1-4) Option: ")
    if action == "1":
        train()
    if action == "2":
        battle()
    if action== "3":
        display_pokemon()
    if action== "4":
        break
#main
pokemon_game()
