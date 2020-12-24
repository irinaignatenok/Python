from anagram_checker import AnagramChecker

def show_menu():
    find_anagrams = input("Would you like to fins anagram?To find anagrams enter yes, otherwise exit")
    if find_anagrams == 'yes':
        show_anagrams = AnagramChecker()
    elif find_anagrams == 'exit':
        print('Exit')

show_menu()
