# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: This translates to finding the longest subarray with at most 2 distinct elements. Use a hash map to keep track of fruit counts in the current window. Expand right, update map. If map size > 2, shrink from left until map size is 2.

def totalFruit(fruits):
    count = {}
    left = 0
    max_len = 0
    for right in range(len(fruits)):
        count[fruits[right]] = count.get(fruits[right], 0) + 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0: del count[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

