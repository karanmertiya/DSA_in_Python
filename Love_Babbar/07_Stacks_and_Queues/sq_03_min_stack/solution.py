# Time Complexity: O(1) per operation
# Space Complexity: O(N)
# Explanation: Store pairs of `(value, current_minimum)` in the stack. Alternatively, use math to encode the difference between the value and the minimum to achieve O(1) space auxiliary, but a stack of pairs is standard.

class MinStack:
    def __init__(self):
        self.st = []
    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            self.st.append((val, min(val, self.st[-1][1])))
    def pop(self) -> None:
        self.st.pop()
    def top(self) -> int:
        return self.st[-1][0]
    def getMin(self) -> int:
        return self.st[-1][1]

