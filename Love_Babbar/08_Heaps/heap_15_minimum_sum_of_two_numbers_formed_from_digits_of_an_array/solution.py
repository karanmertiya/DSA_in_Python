# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort the array. Build two strings representing the two numbers by picking digits alternately from the sorted array. Add the two large numbers as strings or build the result dynamically.

def solve(arr: List[int], n: int) -> str:
    arr.sort()
    a, b = "", ""
    for i in range(n):
        if i % 2 == 0:
            a += str(arr[i])
        else:
            b += str(arr[i])
    res = str(int(a) + int(b)) if a and b else str(int(a or '0') + int(b or '0'))
    return res

