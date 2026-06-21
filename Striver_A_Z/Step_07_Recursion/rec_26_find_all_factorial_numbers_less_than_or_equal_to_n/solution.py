# Time Complexity: O(K) where K! <= N
# Space Complexity: O(K)
# Explanation: Maintain a current factorial value and an index `i`. At each recursive step, compute the next factorial by multiplying by `i`. If the next factorial is `<= n`, add it to the list and recurse.

def factorialNumbers(N):
    ans = []
    def findFactorials(i, fact):
        if fact > N: return
        ans.append(fact)
        findFactorials(i + 1, fact * (i + 1))
    findFactorials(1, 1)
    return ans

