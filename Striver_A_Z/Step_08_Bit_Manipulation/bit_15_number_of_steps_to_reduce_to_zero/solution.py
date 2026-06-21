# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: If `num` is odd, subtract 1 (equivalent to clearing rightmost bit). If even, divide by 2 (equivalent to right shift).

def numberOfSteps(num: int) -> int:
    if num == 0: return 0
    steps = 0
    while num > 0:
        if num & 1: num -= 1
        else: num >>= 1
        steps += 1
    return steps

