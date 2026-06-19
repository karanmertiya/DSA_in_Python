# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use three pointers: `low`, `mid`, `high`. If `arr[mid] < a`, swap `arr[low]` and `arr[mid]`, increment both. If `arr[mid] > b`, swap `arr[mid]` and `arr[high]`, decrement `high`. Else increment `mid`.

def threeWayPartition(array, a, b):
    low, mid, high = 0, 0, len(array) - 1
    while mid <= high:
        if array[mid] < a:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] > b:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        else:
            mid += 1

