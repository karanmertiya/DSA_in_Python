# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Create a copy of array, sort it, and remove duplicates. Use a hash map to map each unique value to its rank. Replace elements in original array using map.

def arrayRankTransform(arr: List[int]) -> List[int]:
    st = sorted(list(set(arr)))
    mpp = {num: rank + 1 for rank, num in enumerate(st)}
    return [mpp[num] for num in arr]

