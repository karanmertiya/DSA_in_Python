# Time Complexity: O(N!) (Constraint)
# Space Complexity: O(N) (Constraint)
# Explanation: Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.

def solve_n_queens(n: int) -> list[list[str]]:
    ans = []
    board = [["."] * n for _ in range(n)]
    left_row = [0] * n
    upper_diag = [0] * (2 * n - 1)
    lower_diag = [0] * (2 * n - 1)
    
    def solve(col):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
            
        for row in range(n):
            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:
                board[row][col] = 'Q'
                left_row[row] = 1
                lower_diag[row + col] = 1
                upper_diag[n - 1 + col - row] = 1
                
                solve(col + 1)
                
                board[row][col] = '.'
                left_row[row] = 0
                lower_diag[row + col] = 0
                upper_diag[n - 1 + col - row] = 0
                
    solve(0)
    return ans

