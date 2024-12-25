from tkinter import *
from tkinter import messagebox

# Global variables
current_player = "X"
board = [""] * 9

# Reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", state=NORMAL)

# Check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return None

# Handle button click
def handle_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state=DISABLED)
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Tkinter GUI setup
root = Tk()
root.geometry("400x450")
root.title("Tic Tac Toe")

# Heading
Label(root, text="Tic Tac Toe", font=("Helvetica", 16, "bold"), pady=10).pack()

# Game buttons
frame = Frame(root)
frame.pack()
buttons = []
for i in range(9):
    button = Button(frame, text="", font=("Helvetica", 20), width=5, height=2, command=lambda i=i: handle_click(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# Reset button
Button(root, text="Reset", command=reset_game, font=("Helvetica", 12), bg="lightblue").pack(pady=10)

# Run the application
root.mainloop()