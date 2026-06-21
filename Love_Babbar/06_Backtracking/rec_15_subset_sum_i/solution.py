# Time Complexity: O(2^N)
# Space Complexity: O(2^N)
# Explanation: Recursively either include `arr[ind]` in sum, or exclude it. If `ind == N`, add `sum` to result array.

def subsetSums(arr: List[int], N: int) -> List[int]:
    sumSubset = []
    def func(ind, current_sum):
        if ind == N:
            sumSubset.append(current_sum)
            return
        func(ind + 1, current_sum + arr[ind])
        func(ind + 1, current_sum)
    func(0, 0)
    sumSubset.sort()
    return sumSubset

