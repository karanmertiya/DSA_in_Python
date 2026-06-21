# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Keep track of the number of opening and closing brackets, and an `imbalance` counter. When encountering `[`, decrease imbalance. When encountering `]`, increase imbalance. The number of swaps is updated when an imbalance is found and we find the next `[`.

def minimumNumberOfSwaps(S):
    open_count = 0
    close_count = 0
    fault = 0
    ans = 0
    for char in S:
        if char == ']':
            close_count += 1
            fault = close_count - open_count
        else:
            open_count += 1
            if fault > 0:
                ans += fault
                fault -= 1
    return ans

