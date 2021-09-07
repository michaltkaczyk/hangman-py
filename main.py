class Word:

    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word


class Game:

    def __init__(self, word):
        self.word = word
        self.used_letters = set()

    def ask_for_letter(self):
        played_letter = input("Play a new letter: ")
        self.used_letters.add(played_letter)

    def show_letters(self):
        print("You have already played:", ", ".join(sorted(self.used_letters)))


if __name__ == '__main__':
    game = Game("password")

    for x in range(3):
        game.ask_for_letter()

    game.show_letters()
    print(game.word)

