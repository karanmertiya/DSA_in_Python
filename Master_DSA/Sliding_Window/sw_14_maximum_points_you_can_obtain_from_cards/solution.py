# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Instead of picking cards from the ends, find the subarray of length `N - K` that has the minimum sum. Subtract this minimum sum from the total sum of the array. That gives the maximum score.

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    window_size = n - k
    window_sum = sum(cardPoints[:window_size])
    min_window_sum = window_sum
    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, window_sum)
    return total_sum - min_window_sum

