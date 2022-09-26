from tabledata import periodic_table_values


def identify_numbers(word):
    numbers = ''
    for item in word:
        if item in '1234567890':
            numbers += item
        else:
            pass
    if numbers == "":
        return 1
    return int(numbers)

def remove_numbers(word):
    letters = ''
    for item in word:
        if item not in '1234567890':
            letters += item
        else:
            pass
    return letters 

remove_numbers("mujeeb12345")



mass = 0
while True:
    print("Enter the element and the a full stop to end the compound of molecule (case sensitive) ")
    element = input("> ")
    if element == "." or element == " ":
        print(".....Molar mass is", mass)
        print()
        mass = 0
    else:
        mass += identify_numbers(element) * periodic_table_values[remove_numbers(element)]
