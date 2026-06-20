# Time Complexity: O(2^N * k)
# Space Complexity: O(k * x)
# Explanation: Sort the array. Recursive function iterates from `ind` to `n`. Skip duplicates (`if i > ind and arr[i] == arr[i-1]`). If `arr[i] > target`, break. Else add to path, subtract from target, and recurse.

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    candidates.sort()
    def findCombinations(ind, target, ds):
        if target == 0:
            ans.append(list(ds))
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]: continue
            if candidates[i] > target: break
            ds.append(candidates[i])
            findCombinations(i + 1, target - candidates[i], ds)
            ds.pop()
    findCombinations(0, target, [])
    return ans

