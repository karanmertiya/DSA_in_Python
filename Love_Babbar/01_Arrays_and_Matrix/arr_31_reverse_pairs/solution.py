# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Modified Merge Sort. Before merging, loop through left and right halves. If left[i] > 2 * right[j], increment j. Number of pairs is (j - (mid+1)).

def reversePairs(nums: List[int]) -> int:
    def merge(low, mid, high):
        temp, left, right = [], low, mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left]); left += 1
            else: temp.append(nums[right]); right += 1
        while left <= mid: temp.append(nums[left]); left += 1
        while right <= high: temp.append(nums[right]); right += 1
        for i in range(low, high + 1): nums[i] = temp[i - low]
    def countPairs(low, mid, high):
        right, cnt = mid + 1, 0
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]: right += 1
            cnt += (right - (mid + 1))
        return cnt
    def mergeSort(low, high):
        cnt = 0
        if low >= high: return cnt
        mid = (low + high) // 2
        cnt += mergeSort(low, mid)
        cnt += mergeSort(mid + 1, high)
        cnt += countPairs(low, mid, high)
        merge(low, mid, high)
        return cnt
    return mergeSort(0, len(nums) - 1)

