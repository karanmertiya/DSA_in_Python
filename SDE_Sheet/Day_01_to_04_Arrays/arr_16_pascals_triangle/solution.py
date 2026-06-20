# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def generate(numRows: int) -> list[list[int]]:
    ans = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = ans[i-1][j-1] + ans[i-1][j]
        ans.append(row)
    return ans

# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(N<sup>2</sup>) (Constraint)
# Explanation: Optimal: Generate row by row. Each element `val[i][j]` is the sum of `val[i-1][j-1]` and `val[i-1][j]`.

def generate(numRows: int) -> list[list[int]]:
    ans = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = ans[i-1][j-1] + ans[i-1][j]
        ans.append(row)
    return ans

