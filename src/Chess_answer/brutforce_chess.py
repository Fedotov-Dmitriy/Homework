from itertools import permutations


def n_bruteforce(n):
    count = 0
    if n < 0:
        return 0
    for perm in permutations(range(n)):
        if is_valid(perm):
            count += 1
    return count


def is_valid(board):
    a = len(board)
    for i in range(a):
        for j in range(i + 1, a):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True


def main():
    n = int(input("Введите N\n"))
    print(n_bruteforce(n))


main()
