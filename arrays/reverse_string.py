# INPUT - list of characters
# OUTPUT - reversed in place list of characters

character_list = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']


def reverse_string(characters: list) -> list:
    for i in range(int(len(characters)/2)):
        characters[i], characters[len(characters) - i - 1] = characters[len(characters) - i - 1], characters[i]
    return characters


if __name__ == '__main__':
    print(reverse_string(character_list))
