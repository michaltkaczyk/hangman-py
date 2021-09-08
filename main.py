import random

LIVES = 6

with open('words.txt') as f:
    words = f.read().splitlines()


class Game:

    def __init__(self, word):
        self.word = word
        self.used_letters = set()
        self.played_letter = ""
        self.lives_remaining = LIVES
        self.lost = False
        self.won = False

    def ask_for_letter(self):
        self.played_letter = input("Play a new letter: ")

        if len(self.played_letter) != 1:
            print("Play a SINGLE letter!")
        elif not self.played_letter.isalpha():
            print("Play a single LETTER!")
        elif self.played_letter in self.used_letters:
            print("Play a NEW letter!")
        else:
            self.used_letters.add(self.played_letter)
            if self.played_letter not in self.word:
                print("Wrong letter, life lost")
                self.lives_remaining -= 1

    def show_letters(self):
        print("You have already played:", ", ".join(sorted(self.used_letters)), "\n")

    def check_if_game_finished(self):
        if self.lives_remaining < 1:
            self.lost = True
            print("Game lost! The word was:", self.word)
        elif set(self.word).issubset(self.used_letters):
            self.won = True
            print("Game won!")

    def show_hashed_word(self):
        hashed_word = ""

        for letter in self.word:
            if letter in self.used_letters:
                hashed_word += letter
            else:
                hashed_word += "_"

        print("Secret word is:", hashed_word)

    def show_remaining_lives(self):
        print("Lives remaining:", "*" * self.lives_remaining)

    def play(self):
        while not game.lost and not game.won:
            self.show_hashed_word()
            self.show_remaining_lives()
            if len(self.used_letters) > 0:
                self.show_letters()
            self.ask_for_letter()
            self.check_if_game_finished()


if __name__ == '__main__':
    game = Game(random.choice(words))
    game.play()
