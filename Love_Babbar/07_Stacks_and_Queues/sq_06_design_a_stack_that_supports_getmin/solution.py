# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: To achieve O(1) space, when pushing `x < minEle`, push `2 * x - minEle` and update `minEle = x`. When popping `y`, if `y < minEle`, then `minEle = 2 * minEle - y`.

class SpecialStack:
    def __init__(self):
        self.s = []
        self.minEle = float('inf')
    def push(self, a):
        if not self.s:
            self.s.append(a)
            self.minEle = a
        elif a < self.minEle:
            self.s.append(2 * a - self.minEle)
            self.minEle = a
        else:
            self.s.append(a)
    def pop(self):
        if not self.s: return -1
        top = self.s.pop()
        if top < self.minEle:
            prevMin = self.minEle
            self.minEle = 2 * self.minEle - top
            return prevMin
        return top
    def getMin(self):
        if not self.s: return -1
        return self.minEle

