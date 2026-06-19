# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(1)
# Explanation: Repeatedly swap adjacent elements if they are in the wrong order. Push the maximum element to the end.

def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n - 1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if not did_swap: break

