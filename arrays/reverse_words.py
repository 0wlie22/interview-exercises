# INPUT - list of characters  (words separated by space)
# OUTPUT - reversed by words list of characters

message = ['l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ',
           'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e']


def reverse_characters(characters: list):
    for i in range(int(len(characters) / 2)):
        characters[i], characters[len(characters) - i - 1] = characters[len(characters) - i - 1], characters[i]
    return characters


def reverse_words(characters: list):
    reverse_characters(characters)
    index = 0
    for i in range(len(characters)):
        if characters[i] == ' ' or i == len(characters) - 1:
            if i == len(characters) - 1:
                i += 1
            characters[index: i] = reverse_characters(characters[index: i])
            index = i + 1
    return characters


if __name__ == '__main__':
    print(reverse_words(message))
