from tabledata import periodic_table_values


def identify_numbers(word):
    numbers = ''
    for item in word:
        if item in '1234567890':
            numbers += item
        else:
            pass
    
    return int(numbers)




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
