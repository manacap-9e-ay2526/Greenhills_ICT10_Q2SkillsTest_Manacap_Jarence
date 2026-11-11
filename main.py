# Periodic Table Information Finder
from pyscript import display, document


# Dictionary of non-metal elements
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222)
}


def search_element(e):
    # Clears the previous result
    document.getElementById("result").innerHTML = " "

    # Gets the element symbol entered by the user
    element_symbol = document.getElementById("elementSymbol").value
    element_symbol = element_symbol.capitalize()

    # Checks if the element exists
    element_checker = element_symbol in non_metals

    # Retrieves the element information
    element_info = non_metals.get(element_symbol, ("N/A", "N/A", "N/A"))

    # Gets the individual element information using offsets
    element_name = element_info[0]
    atomic_number = element_info[1]
    atomic_mass = element_info[2]

    # Stores both possible messages
    display_message = (
        f"Sorry, {element_symbol} does not exist in the non-metals list.",
        f"Element Symbol: {element_symbol} | Element Name: {element_name} | Atomic Number: {atomic_number} | Atomic Mass: {atomic_mass} u"
    )

    # Displays the result
    display(display_message[element_checker], target="result")