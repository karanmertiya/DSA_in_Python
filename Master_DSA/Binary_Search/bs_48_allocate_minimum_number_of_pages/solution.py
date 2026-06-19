# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Search space for max pages is `max(arr)` to `sum(arr)`. Use binary search. For a `mid` value, count how many students are needed. If `students > M`, we need to increase max pages (`low = mid + 1`), else we can try to decrease (`high = mid - 1`).

def findPages(A: List[int], N: int, M: int) -> int:
    if M > N: return -1
    def isPossible(mid):
        students, curr_sum = 1, 0
        for x in A:
            if curr_sum + x > mid:
                students += 1
                curr_sum = x
                if students > M or x > mid: return False
            else:
                curr_sum += x
        return True
    low, high = max(A), sum(A)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

