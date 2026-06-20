# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def countDistinct(arr, n, k):
    m = {}
    ans = []
    for i in range(k):
        m[arr[i]] = m.get(arr[i], 0) + 1
    ans.append(len(m))
    for i in range(k, n):
        m[arr[i - k]] -= 1
        if m[arr[i - k]] == 0: del m[arr[i - k]]
        m[arr[i]] = m.get(arr[i], 0) + 1
        ans.append(len(m))
    return ans

# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Optimal: Use a hash map to keep track of element frequencies in the window of size K. The number of distinct elements is the size of the hash map. As window slides, increment frequency of new element, decrement frequency of outgoing element. If frequency becomes 0, remove it from map.

def countDistinct(arr, n, k):
    m = {}
    ans = []
    for i in range(k):
        m[arr[i]] = m.get(arr[i], 0) + 1
    ans.append(len(m))
    for i in range(k, n):
        m[arr[i - k]] -= 1
        if m[arr[i - k]] == 0: del m[arr[i - k]]
        m[arr[i]] = m.get(arr[i], 0) + 1
        ans.append(len(m))
    return ans

