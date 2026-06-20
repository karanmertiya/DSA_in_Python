# Time Complexity: O(log10(N))
# Space Complexity: O(1)
# Explanation: Extract each digit, cube it, and sum them up. If the sum equals the original number, it's an Armstrong number.

def armstrongNumber(n):
    return "Yes" if sum(int(d)**3 for d in str(n)) == n else "No"

