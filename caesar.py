def encrypt(word, number):
    secretWord = ""
    for i, eachChar in enumerate(word):
        if word[i].isalpha():
            secretWord = secretWord + rotate_character(word[i], number)
        else:
            secretWord = secretWord + word[i]

    return secretWord

def alphabet_position(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i, eachChar in enumerate(alphabet):
        if letter.upper() == eachChar:
            strPosition = i
            return int(strPosition)

def rotate_character(letter, number):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charPosition = alphabet_position(letter)
    movePos = number % 26
    newPos = movePos + charPosition

    if newPos > 25:
        newPos = newPos - 26

    newChar = alphabet[newPos]

    if ord(letter) > 96:
        return newChar.lower()
    else:

        return newChar
