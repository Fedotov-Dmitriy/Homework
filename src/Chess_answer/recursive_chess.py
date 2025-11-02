def count_n_queens_solutions(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or (abs(board[i] - col) == abs(i - row)):
                return False
        return True
    
    def solve(row, board):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += solve(row + 1, board)
                board[row] = -1  
        return count
    
    board = [-1] * n
    return solve(0, board)


def main():
    n = int(input("Введите количество столбцов доски\n"))
    print(count_n_queens_solutions(n))


main()