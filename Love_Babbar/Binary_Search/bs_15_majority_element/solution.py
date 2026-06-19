# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use Moore's Voting Algorithm to find a candidate for majority element. Then count the occurrences of the candidate in the array to verify if it appears more than N/2 times.

def majorityElement(a, size):
    count = 0
    candidate = -1
    for num in a:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate: count += 1
        else: count -= 1
    count = 0
    for num in a:
        if num == candidate: count += 1
    return candidate if count > size // 2 else -1

