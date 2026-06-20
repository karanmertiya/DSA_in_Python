# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# Explanation: Create a new array by appending the two arrays. Then call `heapify` starting from the last non-leaf node `(n/2 - 1)` down to the root `0`.

def mergeHeaps(a, b, n, m):
    ans = a + b
    total = n + m
    def heapify(i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < total and ans[l] > ans[largest]: largest = l
        if r < total and ans[r] > ans[largest]: largest = r
        if largest != i:
            ans[i], ans[largest] = ans[largest], ans[i]
            heapify(largest)
    for i in range(total // 2 - 1, -1, -1):
        heapify(i)
    return ans

