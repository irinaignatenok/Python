def collect_user_input():
    user_input = input("Please enter a word: ")
    user_input = user_input.lower() #sets user input to lower case
    user_input = user_input.strip() # strip the input
    return user_input

class AnagramChecker():

    file = open("dictionary.txt", 'r')
    dictionary = []
    for word in file:
        stripped_word = word.strip("\n")
        stripped_word = stripped_word.lower()
        dictionary.append(stripped_word)

    file.close()

    def __init__(self):
        self.users_input = collect_user_input()
        if not self.is_valid_word():
            print("Word can only contain letters")
            self.users_input = collect_user_input()
        if not self.is_word_in_dictionary():
            print("Word not found. Please enter another word")
            self.users_input = collect_user_input()



    # def is_valid_word(self,word):
    #     AnagramChecker.is_valid_word = classmethod(AnagramChecker.is_valid_word)
    #     check_word = AnagramChecker.is_valid_word()
    #     for char in check_word:
    #         if char in check_word:
    #             return True
    #         return False
    def is_valid_word(self):
        valid_char = "abcdefghijklmnopqrstuvwxyz"
        for char in self.users_input:
            if char not in valid_char:
                return False
            else:
                return True

    def is_word_in_dictionary(self):
        if self.users_input in self.dictionary:
            return True
        else:
            return False

    def get_anagrams(self):
        anagrams = []
        for word in self.dictionary:
            if sorted(word) == sorted(self.users_input):
                anagrams.append(word)
        print(f"YOUR WORD:", self.users_input)
        print("this is a valid English word")
        print("Anagrams for your word: ", ','.join(anagrams))
        return anagrams

play = AnagramChecker()
print(play.get_anagrams())
