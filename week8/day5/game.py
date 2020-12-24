import random

game_choice = ["paper", "scissors", "rock"]
class Game():
    
    def get_user_item(self):
        
        choose_item = (input("What will you choose? scissors, paper or rock")).lower()
        for item in game:
            if item != choose_item:
                choose_item = (input("Please choose something")).lower()
        return item        
    
    def get_computer_item(self):
        computer_choice = random.choice(game_choice)
        return computer_choice
    
    def get_game_result(self, user_item, computer_item)
        user_item = get_user_item()
        computer_item = get_computer_item
        
        return 
    
    def play(self):
        
        user_item = get_user_item()
        computer_item = get_computer_item
        if user_item = computer_item:
            draw += 1
            print(f"The computer selected {computer_item }. You selected {user_item}. You drew!")
            
        elif (computer_item = "scissors" and user_item = "rock") or 
        (computer_item = "paper" and user_item = "scissors") or 
        (computer_item = "rock" and user_item = "paper"):
            win +=1
            print(f"The computer selected {computer_item }. You selected {user_item}. You win!!!")
        else:
            loss +=1
            print("The computer selected {computer_item }. You selected {user_item}. You lose")
        
        return
        
    