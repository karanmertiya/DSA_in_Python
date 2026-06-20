# Time Complexity: O(N * log(sum(A) - max(A)))
# Space Complexity: O(1)
# Explanation: Binary Search on Answer. The search space for pages is from `max(A)` to `sum(A)`. For a given `mid`, check if books can be allocated to `<= M` students without any student exceeding `mid` pages.

def findPages(A: List[int], N: int, M: int) -> int:
    if M > N: return -1
    def isPossible(maxPages):
        students, currentPages = 1, 0
        for pages in A:
            if pages > maxPages: return False
            if currentPages + pages > maxPages:
                students += 1
                currentPages = pages
            else:
                currentPages += pages
        return students <= M
    low, high = max(A), sum(A)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid; high = mid - 1
        else: low = mid + 1
    return ans

