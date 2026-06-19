# Time Complexity: O(1) amortized
# Space Complexity: O(Number of elements)
# Explanation: Use an array of linked lists (chaining) for collision resolution. Hash function `key % capacity`. Add: Insert if not present. Remove: Delete node. Contains: Traverse list at `hash(key)`.

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
class MyHashSet:
    def __init__(self):
        self.size = 10007
        self.buckets = [None] * self.size
    def add(self, key: int) -> None:
        idx = key % self.size
        curr = self.buckets[idx]
        while curr:
            if curr.key == key: return
            curr = curr.next
        newNode = ListNode(key)
        newNode.next = self.buckets[idx]
        self.buckets[idx] = newNode
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
    def contains(self, key: int) -> bool:
        idx = key % self.size
        curr = self.buckets[idx]
        while curr:
            if curr.key == key: return True
            curr = curr.next
        return False

