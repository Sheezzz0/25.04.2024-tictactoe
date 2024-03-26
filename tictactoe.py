def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        row = int(input(f"Player {players[turn]} enter row (0, 1 or 2): "))
        col = int(input(f"Player {players[turn]} enter column (0, 1 or 2): "))
        if board[row][col] == " ":
            board[row][col] = players[turn]
            if check_winner(board, players[turn]):
                print(f"Player {players[turn]} wins!")
                break
            turn = (turn + 1) % 2
        else:
            print("Cell already occupied, try again.")

if __name__ == "__main__":
    main()
