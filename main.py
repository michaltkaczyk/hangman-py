MAX_LETTERS = 3


class Word:

    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word


def is_input_single_character(x):
    return len(x) == 1


def is_input_letter(x):
    return x.isalpha()


def is_input_used(x, used_elements):
    return x in used_elements


class Game:

    def __init__(self, word):
        self.word = word
        self.used_letters = set()
        self.lost = False

    def ask_for_letter(self):
        played_letter = input("Play a new letter: ")

        if not is_input_single_character(played_letter):
            print("Play a SINGLE letter!")
            self.ask_for_letter()

        if not is_input_letter(played_letter):
            print("Play a single LETTER!")
            self.ask_for_letter()

        if is_input_used(played_letter, self.used_letters):
            print("Play a NEW letter!")
            self.ask_for_letter()

        self.used_letters.add(played_letter)

    def show_letters(self):
        print("You have already played:", ", ".join(sorted(self.used_letters)))

    def check_if_lost(self):
        if len(self.used_letters) > MAX_LETTERS:
            self.lost = True


if __name__ == '__main__':
    game = Game("password")

    while not game.lost:
        game.ask_for_letter()
        game.check_if_lost()

    game.show_letters()
    print("Game lost!")
    print("The word was:", game.word)
