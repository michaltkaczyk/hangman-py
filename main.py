import random

LIVES = 6

with open('words.txt') as f:
    words = f.read().splitlines()


class Game:

    def __init__(self, word):
        self.word = word.upper()
        self.used_letters = set()
        self.played_letter = ""
        self.lives_remaining = LIVES
        self.lost = False
        self.won = False

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

    def show_used_letters(self):
        if len(self.used_letters) > 0:
            print("You have already played:", ", ".join(sorted(self.used_letters)), "\n")

    def ask_for_letter(self):
        self.played_letter = input("Play a new letter: ").upper()

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

    def check_if_game_finished(self):
        if self.lives_remaining < 1:
            self.lost = True
            print("Game lost! The word was:", self.word)
        elif set(self.word).issubset(self.used_letters):
            self.won = True
            print("Game won!")

    def play(self):
        while not game.lost and not game.won:
            self.show_hashed_word()
            self.show_remaining_lives()
            self.show_used_letters()
            self.ask_for_letter()
            self.check_if_game_finished()


def ask_play_again():
    while True:
        choice = input("Would you like to play again? [Y/N] ").upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            pass


if __name__ == '__main__':

    play_again_on = True

    while play_again_on:
        game = Game(random.choice(words))
        game.play()
        play_again_on = ask_play_again()
