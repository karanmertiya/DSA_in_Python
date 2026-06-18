# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Build a frequency map, then iterate through the map to find the max and min frequencies.

def find_high_low_freq(arr: list[int]) -> tuple:
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_f, min_f = 0, float('inf')
    max_ele, min_ele = 0, 0
    
    for ele, count in freq.items():
        if count > max_f:
            max_f, max_ele = count, ele
        if count < min_f:
            min_f, min_ele = count, ele
    return max_ele, min_ele

