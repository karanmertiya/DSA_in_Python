# Time Complexity: O(1) for get and put
# Space Complexity: O(Capacity)
# Explanation: Use a hash map to store keys to Node pointers. Use a doubly linked list to track the usage history. The head of the DLL represents the most recently used, and the tail represents the least recently used. On `get` or `put`, move the accessed node to the head. If capacity is exceeded, remove the node before the tail.

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
    def addNode(self, newnode):
        temp = self.head.next
        newnode.next, newnode.prev = temp, self.head
        self.head.next, temp.prev = newnode, newnode
    def deleteNode(self, delnode):
        delprev, delnext = delnode.prev, delnode.next
        delprev.next, delnext.prev = delnext, delprev
    def get(self, key: int) -> int:
        if key in self.m:
            resnode = self.m[key]
            ans = resnode.val
            del self.m[key]
            self.deleteNode(resnode)
            self.addNode(resnode)
            self.m[key] = self.head.next
            return ans
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            existingnode = self.m[key]
            del self.m[key]
            self.deleteNode(existingnode)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        self.addNode(Node(key, value))
        self.m[key] = self.head.next

