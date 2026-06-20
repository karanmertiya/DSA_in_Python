# Time Complexity: O(1) amortized
# Space Complexity: O(N)
# Explanation: Use a stack of pairs `(price, span)`. When a new price comes in, initialize its span to 1. Pop elements from the stack while the top element's price is `<= price`, adding their spans to the current span. Push `(price, span)` to the stack.

class StockSpanner:
    def __init__(self):
        self.s = []
    def next(self, price: int) -> int:
        span = 1
        while self.s and self.s[-1][0] <= price:
            span += self.s.pop()[1]
        self.s.append((price, span))
        return span

