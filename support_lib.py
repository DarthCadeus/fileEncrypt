__author__ = 'owen'
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
class Alphabet:
    def __init__(self, alpha=alphabet):
        self.alphabet = alpha

    def get_index(self, char, start=0):
        try:
            return self.alphabet.index(char)+start
        except ValueError:
            return False

    def get_char(self, index, start=0):
        try:
            return self.alphabet[index-start]
        except IndexError:
            return False

    def shift(self, shift, char, start=1):
        if isinstance(shift, str):
            ex_index = self.get_index(char)+self.get_index(shift)+start
        elif isinstance(shift, int):
            ex_index = self.get_index(char)+shift+start
            if shift > 0:
                ex_index += start
            elif shift == 0:
                pass
            else:
                ex_index -= start
        if ex_index > len(self.alphabet)-1:
            ex_index -= len(self.alphabet)
        return self.get_char(ex_index)

if __name__ == "__main__":
    a_query = Alphabet()
    print(a_query.shift(-1, "b"))
