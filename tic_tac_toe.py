"""
Tic-Tac-Toe
Author: Marcus Blanc
"""

# Instructions
def instructions():
 """Display game instructions."""
 print(
 """
 Welcome to the greatest intellectual challenge
 of all time: Tic-Tac-Toe.
 You will make your move known by entering
 a number, 0 - 8. And the number
 will correspond to the board position as illustrated:
 0 | 1 | 2
 ---------
 3 | 4 | 5
 ---------
 6 | 7 | 8
 Prepare yourself, human.
 The ultimate battle
 is about to begin. \n
 """
 )
# main
print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()
print("Here they are again:")

# Receive and Return
# Demonstrates parameters and return values
def display(message):
 print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
 """Ask a yes or no question."""
 response = None
 while response not in ("y", "n"):
    response = input(question).lower()
 return response
# main
display("Here's a message for you.\n")
number = give_me_five()
print("Here's what I got from give_me_five():", number)
answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s please pick a square between (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()