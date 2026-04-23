def solve_n_queens(n):

    board = [[0 for _ in range(n)] for _ in range(n)]

    rows = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    def solve(col):

        if col >= n:
            return True

        for i in range(n):

            if not rows[i] and not diag1[i + col] and not diag2[i - col + n]:

                board[i][col] = 1

                rows[i] = True
                diag1[i + col] = True
                diag2[i - col + n] = True

                if solve(col + 1):
                    return True

                board[i][col] = 0

                rows[i] = False
                diag1[i + col] = False
                diag2[i - col + n] = False

        return False

    if solve(0):
        print("Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists")


solve_n_queens(4)
