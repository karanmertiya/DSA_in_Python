# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Iterative approach. Construct each row from the previous row. First and last elements are 1. Middle elements are sum of elements right above them.

def generate(numRows: int) -> List[List[int]]:
    res = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(res[i-1][j-1] + res[i-1][j])
        row.append(1)
        res.append(row)
    return res

