class Guesser:

    def __init__(self, word_len):
        self.lives = 1
        self.word = ["_"] * word_len