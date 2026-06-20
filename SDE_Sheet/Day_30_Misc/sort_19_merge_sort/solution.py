# Time Complexity: O(N log N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Recursively split array in half, sort them, and merge the sorted halves.

def merge_sort(arr: list[int]) -> None:
    def merge(low, mid, high):
        temp = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left]); left += 1
        while right <= high:
            temp.append(arr[right]); right += 1
        for i in range(len(temp)):
            arr[low + i] = temp[i]
            
    def helper(low, high):
        if low >= high: return
        mid = (low + high) // 2
        helper(low, mid)
        helper(mid + 1, high)
        merge(low, mid, high)
        
    helper(0, len(arr) - 1)

