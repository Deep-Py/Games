# creating a list to create a board using list comprehension
import os
board = ["   " for i in range(9)]


# To create a board in structure on shell create a function

def print_board():
    clear_screen()
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print("Welcome to game of TIC TAC TOE")
    print("--"*20)
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    

    
    
# function created to check user move
def player_move(icon):
    if icon == " X ":
        number = 1
    elif icon == " O ":
        number = 2

    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9):").strip())
    if board[choice - 1] == "   ":
        board[choice - 1]= icon
    else:
        print()
        print("That space is taken")
        print()
        player_move(icon)

    
# function created to check the WIN condition
def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon)or\
      (board[3]==icon and board[4]==icon and board[5]==icon)or\
      (board[6]==icon and board[7]==icon and board[8]==icon)or\
      (board[0]==icon and board[3]==icon and board[6]==icon)or\
      (board[1]==icon and board[4]==icon and board[7]==icon)or\
      (board[2]==icon and board[5]==icon and board[8]==icon)or\
      (board[0]==icon and board[4]==icon and board[8]==icon)or\
      (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False

    
# function created to clear the screen    
def clear_screen():
    os.system('cls')


# function created to check the draw condition
def is_draw():
    if "   " not in board:
        return True
    else:
        return False

    
# function created to end the game
def end_game():
    print("You are about to exit the game")
    choice=input("Press y to confirm exit: ").strip().lower()
    if choice == 'y':
        exit()

# function created to start the game
def start_game():
    choice = input("To Play game enter y/n: ").strip().lower()
    if choice == 'y':
        while True:
            print_board()
            player_move(" X ")
            print_board()
            if is_victory(" X "):
                print("X Wins!!. Congratulations!!!")
                break
            elif is_draw():
                print("Its Draw!!")
                break
            player_move(" O ")
            if is_victory(" O "):
                print_board()
                print("O Wins!!. Congratulations!!!")
                break
            elif is_draw():
                print("Its Draw !!")
                break
    elif choice == 'n':
        end_game()

# Game Starts by Calling this function :- START POINT        
print("Welcome to game of TIC TAC TOE")
print("--"*20)
start_game()  
    


    
