# Time Complexity: O(1) amortized
# Space Complexity: O(Number of elements)
# Explanation: Similar to HashSet, but each node stores a `(key, value)` pair. On Put, if key exists, update value. Else insert new node. On Get, return value if key found, else -1.

class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size = 10007
        self.buckets = [None] * self.size
    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        curr = self.buckets[idx]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
        newNode = ListNode(key, value)
        newNode.next = self.buckets[idx]
        self.buckets[idx] = newNode
    def get(self, key: int) -> int:
        idx = key % self.size
        curr = self.buckets[idx]
        while curr:
            if curr.key == key: return curr.val
            curr = curr.next
        return -1
    def remove(self, key: int) -> None:
        idx = key % self.size
        curr = self.buckets[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev: prev.next = curr.next
                else: self.buckets[idx] = curr.next
                return
            prev = curr
            curr = curr.next

