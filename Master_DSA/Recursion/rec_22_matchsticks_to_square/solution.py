# Time Complexity: O(4^N)
# Space Complexity: O(N)
# Explanation: Calculate sum. If sum % 4 != 0, return false. Target side length is sum / 4. Sort matchsticks in descending order to optimize. Create an array `sides` of size 4. For each matchstick, try adding it to one of the 4 sides. If a side equals the target or is less, recurse.

def makesquare(matchsticks: List[int]) -> bool:
    total = sum(matchsticks)
    if total % 4 != 0 or len(matchsticks) < 4: return False
    target = total // 4
    matchsticks.sort(reverse=True)
    sides = [0] * 4
    def solve(ind):
        if ind == len(matchsticks):
            return sides[0] == sides[1] == sides[2] == target
        for i in range(4):
            if sides[i] + matchsticks[ind] <= target:
                sides[i] += matchsticks[ind]
                if solve(ind + 1): return True
                sides[i] -= matchsticks[ind]
            if sides[i] == 0: break
        return False
    return solve(0)

