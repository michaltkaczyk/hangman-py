MAX_LETTERS = 3


class Word:

    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word


class Game:

    def __init__(self, word):
        self.word = word
        self.used_letters = set()
        self.lost = False
        self.played_letter = ""

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

    def show_letters(self):
        print("You have already played:", ", ".join(sorted(self.used_letters)), "\n")

    def show_lost_game_screen(self):
        print("Game lost! The word was:", self.word)

    def check_if_lost(self):
        if len(self.used_letters) > MAX_LETTERS:
            self.lost = True
            self.show_lost_game_screen()

    def play(self):
        while not game.lost:
            if len(self.used_letters) > 0:
                self.show_letters()
            self.ask_for_letter()
            self.check_if_lost()


if __name__ == '__main__':
    game = Game(Word("password"))

    while not game.lost:
        game.play()
