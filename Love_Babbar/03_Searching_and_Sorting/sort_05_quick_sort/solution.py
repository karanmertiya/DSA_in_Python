# Time Complexity: O(N log N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.

def quick_sort(arr: list[int]) -> None:
    def partition(low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while i <= high - 1 and arr[i] <= pivot: i += 1
            while j >= low + 1 and arr[j] > pivot: j -= 1
            if i < j: arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
        
    def helper(low, high):
        if low < high:
            p_idx = partition(low, high)
            helper(low, p_idx - 1)
            helper(p_idx + 1, high)
            
    helper(0, len(arr) - 1)

