# Time Complexity: O(1) amortized
# Space Complexity: O(N)
# Explanation: Maintain a DLL where each node represents a specific frequency and contains a set of strings. Use a hash map mapping strings to their current bucket. On inc/dec, move the string to the adjacent bucket (create if necessary). Max is tail->prev, Min is head->next.

class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = self.next = None
class AllOne:
    def __init__(self):
        self.head, self.tail = Bucket(0), Bucket(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.m = {}
    def _add_bucket(self, prev_b, new_b):
        new_b.prev, new_b.next = prev_b, prev_b.next
        prev_b.next.prev = prev_b.next = new_b
    def _remove_bucket(self, b):
        b.prev.next, b.next.prev = b.next, b.prev
    def inc(self, key: str) -> None:
        if key in self.m:
            curr = self.m[key]
            nxt = curr.next
            if nxt == self.tail or nxt.count != curr.count + 1:
                self._add_bucket(curr, Bucket(curr.count + 1))
                nxt = curr.next
            nxt.keys.add(key)
            self.m[key] = nxt
            curr.keys.remove(key)
            if not curr.keys: self._remove_bucket(curr)
        else:
            nxt = self.head.next
            if nxt == self.tail or nxt.count != 1:
                self._add_bucket(self.head, Bucket(1))
                nxt = self.head.next
            nxt.keys.add(key)
            self.m[key] = nxt
    def dec(self, key: str) -> None:
        curr = self.m[key]
        if curr.count == 1:
            del self.m[key]
        else:
            prv = curr.prev
            if prv == self.head or prv.count != curr.count - 1:
                self._add_bucket(curr.prev, Bucket(curr.count - 1))
                prv = curr.prev
            prv.keys.add(key)
            self.m[key] = prv
        curr.keys.remove(key)
        if not curr.keys: self._remove_bucket(curr)
    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""
    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""

