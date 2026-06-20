# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: First count all elements <= k (let's say `cnt`). This will be the window size. Find elements > k in the first window. Then slide the window, updating the number of elements > k. The minimum among all windows is the answer.

def minSwap(arr, n, k):
    cnt = sum(1 for x in arr if x <= k)
    bad = sum(1 for i in range(cnt) if arr[i] > k)
    ans = bad
    for i in range(n - cnt):
        if arr[i] > k: bad -= 1
        if arr[i + cnt] > k: bad += 1
        ans = min(ans, bad)
    return ans

