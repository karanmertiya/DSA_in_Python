# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)
# Explanation: If `num <= 1`, return false. Iterate up to `sqrt(num)`. If `i` divides `num`, add `i` and `num/i` to the sum. After the loop, compare sum with `num`.

def checkPerfectNumber(num: int) -> bool:
    if num <= 1: return False
    total = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i
            if i * i != num: total += num // i
    return total == num

