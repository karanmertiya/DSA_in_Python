# Time Complexity: O(N log M)
# Space Complexity: O(1)
# Explanation: Since rows are sorted, use binary search (`lower_bound` of 1) to find the first index of 1 in each row. The number of 1s is `m - index`. Keep track of the row with the maximum 1s.

def rowWithMax1s(arr, n, m):
    def lowerBound(a, m, x):
        low, high, ans = 0, m - 1, m
        while low <= high:
            mid = (low + high) // 2
            if a[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    max_cnt = 0
    index = -1
    for i in range(n):
        cnt_ones = m - lowerBound(arr[i], m, 1)
        if cnt_ones > max_cnt:
            max_cnt = cnt_ones
            index = i
    return index

