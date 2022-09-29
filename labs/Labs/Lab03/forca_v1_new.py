# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import sys

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


with open('palavras.txt', 'r') as bank:
    bank = bank.readlines()
    word = bank[random.randint(0, len(bank))]


class Hangman():
    def __init__(self):
        print()
        self.wrong_letters = list()
        self.right_letters = list()
        self.fase = 0
        self.new_word = list()

    def guess(self):
        self.letter = input('\nTry a letter: ')
        if self.letter in word:
            self.right_letters.append(self.letter)
            for letter in self.right_letters:
                self.new_word[word.index(letter)] = letter

        else:
            self.wrong_letters.append(self.letter)
            self.fase += 1

    def wrongs(self):
        print('Wrong Words:')
        for letter in self.wrong_letters:
            print(letter)

    def rights(self):
        print('Right Words:')
        for letter in self.right_letters:
            print(letter)

    def hangman(self):
        print(board[self.fase])

    def word_discover(self):
        vez =1
        if vez == 1:
            for letter in word:
                self.new_word.append('_')
            print(f'Word: ', end='')
        for item in self.new_word:
            print(item, end='')
        vez+=1



game = Hangman()

while game.fase < 6:
    if len(game.right_letters) == len(word):
        print('Congratulations, you won the game!')
        break
    else:
        game.hangman()
        game.word_discover()
        game.guess()
        game.rights()
        game.wrongs()

game.hangman()

if game.fase == 6:
    print('\nGame over! You lose.')
    sys.exit()

print('The word was ' + word)
print('\nWas great play with you! Now go study!\n')


# word

