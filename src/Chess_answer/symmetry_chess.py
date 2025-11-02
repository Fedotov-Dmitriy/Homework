def n_queens_symmetry(n):

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
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
    
    if n == 0: 
        return 1
    if n == 1: 
        return 1
    
    total = 0
    # Используем симметрию
    for first_col in range(n // 2):
        board = [-1] * n
        board[0] = first_col
        total += 2 * solve(1, board) 
    
    # Центральный столбец для нечетных n
    if n % 2 == 1:
        board = [-1] * n
        board[0] = n // 2
        total += solve(1, board)
    
    return total

def main():
    n = int(input("Введите размер строки\n"))
    print(n_queens_symmetry(n))


main()