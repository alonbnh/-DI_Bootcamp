import random

a=""
class Game:
    def get_user_item(self):
        a= input("select (r)ock/(p)aper/(s)cissors : ")
        b="r" 
        c="p"
        d="s"
        if a==b or a==c or a==d:
            return a
        else :
            print("You didn't choose the good option, choose again:" )
            
      

    @staticmethod
    def get_computer_item():
        mylist = ["r","p","s"]
        e = random.choice(mylist)
        return e



    def get_game_result(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        if user_item==computer_item:
            print(f"You selected {user_item}. The computer selected {computer_item}. You drew!")
            return "draw"
        if user_item=="s" and computer_item=="p":
            print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
            return "win"
        if user_item=="p" and computer_item=="r":
            print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
            return "win"
        if user_item=="r" and computer_item=="s":
            print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
            return "win"
        if user_item=="p" and computer_item=="s":
            print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
            return "loss"
        if user_item=="r" and computer_item=="p":
            print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
            return "loss"
        if user_item=="s" and computer_item=="r":
            print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
            return "loss"
        
        


    
new_game = Game()    
def play():
    self=new_game.get_game_result()

play()

