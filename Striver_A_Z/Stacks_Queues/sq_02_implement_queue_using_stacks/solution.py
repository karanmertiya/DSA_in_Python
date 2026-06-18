# Time Complexity: O(1) Amortized
# Space Complexity: O(N)
# Explanation: Amortized O(1). Maintain an `input` stack for pushes and an `output` stack for pops. Only transfer elements when `output` is empty.

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x: int) -> None:
        self.input.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        
    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self) -> bool:
        return not self.input and not self.output

