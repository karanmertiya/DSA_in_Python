# Time Complexity: O(N log(Sum-Max))
# Space Complexity: O(1)
# Explanation: Binary search on max pages from `max(arr)` to `sum(arr)`. For a `mid` value, count how many students are needed. If `students > m`, we need to increase limit `low = mid + 1`. Else, `high = mid - 1`.

def findPages(arr: List[int], n: int, m: int) -> int:
    if m > n: return -1
    def count_students(pages):
        students, pages_student = 1, 0
        for p in arr:
            if pages_student + p <= pages:
                pages_student += p
            else:
                students += 1
                pages_student = p
        return students
    low, high = max(arr), sum(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if count_students(mid) > m: low = mid + 1
        else: high = mid - 1
    return low

