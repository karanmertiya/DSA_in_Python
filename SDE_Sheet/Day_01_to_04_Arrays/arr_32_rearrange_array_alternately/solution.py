# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def rearrange(arr, n):
    min_idx, max_idx = 0, n - 1
    max_elem = arr[n - 1] + 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(n):
        arr[i] = arr[i] // max_elem

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: To achieve O(1) space, encode two values into one using `arr[i] += (arr[max_idx] % max_elem) * max_elem`. Iterate with two pointers `max_idx` and `min_idx`. At the end, divide every element by `max_elem`.

def rearrange(arr, n):
    min_idx, max_idx = 0, n - 1
    max_elem = arr[n - 1] + 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(n):
        arr[i] = arr[i] // max_elem

