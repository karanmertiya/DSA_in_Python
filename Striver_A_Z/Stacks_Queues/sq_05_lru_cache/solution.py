# Time Complexity: O(1) per operation
# Space Complexity: O(Capacity)
# Explanation: Use a Hash Map and a Doubly Linked List. The Map stores `key -> Node*`. The DLL maintains recency (head is most recent, tail is least recent). Update DLL pointers on access/insert.

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.m = {}
    def addNode(self, newnode):
        temp = self.head.next
        newnode.next = temp; newnode.prev = self.head
        self.head.next = newnode; temp.prev = newnode
    def deleteNode(self, delnode):
        delprev, delnext = delnode.prev, delnode.next
        delprev.next = delnext; delnext.prev = delprev
    def get(self, key: int) -> int:
        if key in self.m:
            resnode = self.m[key]
            res = resnode.val
            del self.m[key]
            self.deleteNode(resnode)
            self.addNode(resnode)
            self.m[key] = self.head.next
            return res
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            existing = self.m[key]
            del self.m[key]; self.deleteNode(existing)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]; self.deleteNode(self.tail.prev)
        self.addNode(Node(key, value))
        self.m[key] = self.head.next

