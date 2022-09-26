from tabledata import periodic_table_values

mass = 0
while True:
    print("Enter the element and the a full stop to end the compound of molecule (case sensitive) ")
    element = input("> ")
    if element == "." or element == " ":
        print(".....Molar mass is", mass)
        print()
        mass = 0
    else:
        mass += periodic_table_values[element]