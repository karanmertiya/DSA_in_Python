# Time Complexity: O(N)
# Space Complexity: O(log N) for recursion
# Explanation: Apply the standard max-heapify process starting from the last non-leaf node `(N/2 - 1)` down to the root. This takes O(N) time.

def convertMinToMaxHeap(arr: List[int], N: int):
    def maxHeapify(i):
        largest, left, right = i, 2 * i + 1, 2 * i + 2
        if left < N and arr[left] > arr[largest]: largest = left
        if right < N and arr[right] > arr[largest]: largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            maxHeapify(largest)
    for i in range((N - 2) // 2, -1, -1):
        maxHeapify(i)

