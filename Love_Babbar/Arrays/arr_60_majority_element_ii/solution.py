# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Since at most two elements can appear more than n/3 times, maintain two potential candidates (`num1`, `num2`) and their counts. Iterate through the array updating candidates and counts. After finding the candidates, iterate again to count their actual occurrences and check if they exceed n/3.

def majorityElement(nums):
    num1, num2, c1, c2 = -1, -1, 0, 0
    for x in nums:
        if x == num1: c1 += 1
        elif x == num2: c2 += 1
        elif c1 == 0: num1, c1 = x, 1
        elif c2 == 0: num2, c2 = x, 1
        else: c1 -= 1; c2 -= 1
    ans = []
    c1, c2 = 0, 0
    for x in nums:
        if x == num1: c1 += 1
        elif x == num2: c2 += 1
    if c1 > len(nums) // 3: ans.append(num1)
    if c2 > len(nums) // 3: ans.append(num2)
    return ans

