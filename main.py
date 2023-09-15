import random

class GetRandomWord:
    def __init__(self):
        self.words = ['pepe', 'casa', 'padre', 'mario', 'mujer', 'hombre']

    def get_word(self):
        word = random.randint(0, len(words))
        return self.word

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []

    def guess(self, letter):
        print("You guessed the letter!")
        ###
        print("You guessed wrong!")
        ###
        print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for letter in self.word:
            if word == letter:
                print(word, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        if ():

class PlayGame:
    def __init__(self):
        self.word = GetRandomWord().get_word()
        self.hanged = Hangman(self.word)

    def play(self):
        while letter:
            self.hanged.word
            letter = input('Insert a letter: ')
            self.hanged.word
            if (self.hanged.word):
                print("You won!")
                break


if  == "__main__":
