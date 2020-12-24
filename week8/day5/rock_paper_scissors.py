def get_user_menu_choice():
    continue_choice = input("rock/paper/scissors? ")
        return continue_choice

def print_results(results):
    results = {}
    
def main():
    win = 0
    loss = 0
    draw = 0
    choice = (input("Would you like to exit(Yes or Not)?")).lower()
    if choice == "not":
        get_user_menu_choice()
        play()
    else:
        print_results()
        