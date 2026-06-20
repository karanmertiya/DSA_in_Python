# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use DFS. Keep track of the maximum length and the maximum sum. At each node, check if the current length is greater than max length. If so, update max length and max sum. If lengths are equal, update max sum if current sum is greater.

def sumOfLongRootToLeafPath(root):
    maxLen = [0]
    maxSum = [float('-inf')]
    def solve(node, sum_val, length):
        if not node:
            if length > maxLen[0]:
                maxLen[0] = length
                maxSum[0] = sum_val
            elif length == maxLen[0]:
                maxSum[0] = max(sum_val, maxSum[0])
            return
        sum_val += node.data
        solve(node.left, sum_val, length + 1)
        solve(node.right, sum_val, length + 1)
    solve(root, 0, 0)
    return maxSum[0] if maxSum[0] != float('-inf') else 0

