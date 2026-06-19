# Time Complexity: O(2^N)
# Space Complexity: O(N * X) where X is number of combinations
# Explanation: Sort candidates. Recursively pick combinations. If `i > ind` and `candidates[i] == candidates[i-1]`, skip to avoid duplicates. If `target - candidates[i] >= 0`, pick it.

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    ans = []
    def find(ind, target, ds):
        if target == 0:
            ans.append(list(ds))
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]: continue
            if candidates[i] > target: break
            ds.append(candidates[i])
            find(i + 1, target - candidates[i], ds)
            ds.pop()
    find(0, target, [])
    return ans

