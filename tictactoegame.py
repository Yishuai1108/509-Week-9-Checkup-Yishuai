def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Check if there's a winner or a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # Check for draw
    for row in board:
        if " " in row:
            return None
    return "Draw"


def tic_tac_toe():
    """Run the Tic Tac Toe game."""
    print("Welcome to the Tic Tac Toe Game!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = "X"

    while True:
        print_board(board)
        print(f"Player {player_turn}'s turn.")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = player_turn
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    if winner == "Draw":
                        print("It's a draw!")
                    else:
                        print(f"Player {winner} wins!")
                    break
                # Switch player
                player_turn = "O" if player_turn == "X" else "X"
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
