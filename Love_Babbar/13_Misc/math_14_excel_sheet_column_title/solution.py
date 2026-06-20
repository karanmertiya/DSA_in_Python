# Time Complexity: O(log_26(N))
# Space Complexity: O(1)
# Explanation: This is essentially base 26 conversion, but 1-indexed (A=1, B=2, Z=26). To make it 0-indexed, decrement `columnNumber` by 1 at each step, get the remainder modulo 26, convert to character, and divide by 26.

def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        res.append(chr(ord('A') + (columnNumber % 26)))
        columnNumber //= 26
    return "".join(res[::-1])

