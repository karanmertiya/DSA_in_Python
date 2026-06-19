# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use Merge Sort. Before merging, iterate through the left half and right half. For each element in left, find the number of elements in right such that `left[i] > 2 * right[j]`. Add this count.

def reversePairs(nums: List[int]) -> int:
    def merge(low, mid, high):
        count = 0
        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
        temp = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left]); left += 1
            else:
                temp.append(nums[right]); right += 1
        while left <= mid:
            temp.append(nums[left]); left += 1
        while right <= high:
            temp.append(nums[right]); right += 1
        for i in range(len(temp)):
            nums[low + i] = temp[i]
        return count
    def mergeSort(low, high):
        if low >= high: return 0
        mid = (low + high) // 2
        inv = mergeSort(low, mid)
        inv += mergeSort(mid + 1, high)
        inv += merge(low, mid, high)
        return inv
    return mergeSort(0, len(nums) - 1)

