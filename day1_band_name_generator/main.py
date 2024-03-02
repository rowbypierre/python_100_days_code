import os

def clear():
    # clear terminal window or unix
    os.system("cls" if os.name == "nt" else "clear")
    
def band_name_gen():
    # welcome prompt + get city name
    clear()
    os.system("cls" if os.name == "nt" else "clear")
    city = input(f"""\nBand Name Generator 
                \nWelcome User 
                \n"What's the name of the city you up in? \n""")
    city = city.capitalize()
    
    # get pet name
    clear()
    pet = input("\nEnter a great pet name? \n") 
    pet = pet.capitalize()
    
    # print options to user
    clear()
    print("\nHere are some options:")
    print(f"\nThe {pet} Beats of {city}")
    print(f"The {city} {pet} Chorus")
    print(f"Velvet {pet} of {city}")
    print(f"Midnight {pet} in {city}")
    print(f"{city} {pet} Rhapsody")
    print(f"Echoing {pet} of {city}")
    print(f"{city} {pet} Ensemble")
    print(f"Groovy {pet} of {city}")
    print(f"Sonic {pet} Serenade in {city}")
    
if __name__ == '__main__':
    band_name_gen()