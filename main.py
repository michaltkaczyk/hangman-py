class Word:

    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

    @property
    def length(self):
        return len(self.word)

    def hide(self):
        hashed_word = ""

        for letter in self.word:
            hashed_word += "_"

        return hashed_word

    def show(self):
        return self.hide()


if __name__ == '__main__':
    word = Word("password")
    print(word)
    word.show()
