# Time Complexity: O(N! / (N-K)!)
# Space Complexity: O(N)
# Explanation: Use backtracking to try swapping each digit with every digit that appears after it and is greater than it. Keep track of the maximum string seen so far. Prune if swaps == 0.

def findMaximumNum(str_val, k):
    max_str = [str_val]
    def solve(curr, k_left, idx):
        if k_left == 0 or idx == len(curr) - 1: return
        max_char = curr[idx]
        for i in range(idx + 1, len(curr)):
            if curr[i] > max_char: max_char = curr[i]
        if max_char != curr[idx]: k_left -= 1
        for i in range(len(curr) - 1, idx - 1, -1):
            if curr[i] == max_char:
                curr_list = list(curr)
                curr_list[idx], curr_list[i] = curr_list[i], curr_list[idx]
                new_str = "".join(curr_list)
                if new_str > max_str[0]: max_str[0] = new_str
                solve(new_str, k_left, idx + 1)
    solve(str_val, k, 0)
    return max_str[0]

