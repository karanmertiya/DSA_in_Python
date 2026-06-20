# Time Complexity: O(1) visit, O(steps) back/forward
# Space Complexity: O(N) for URLs
# Explanation: Use a Doubly Linked List. Each visit creates a new node, clearing forward history. Back and forward operations just traverse the pointers up to `steps` times.

class Node:
    def __init__(self, url):
        self.url = url
        self.prev = self.next = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)
    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

