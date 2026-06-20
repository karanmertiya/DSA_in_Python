# Time Complexity: O(1) average, O(N) worst case
# Space Complexity: O(N)
# Explanation: Use a large array (e.g., size 10000) of linked lists or vectors. The hash function maps `key` to `key % 10000`. To add, if not present in the bucket, append it. To remove, find and erase. To contain, iterate through bucket.

class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]
    def add(self, key: int) -> None:
        i = key % self.size
        if key not in self.buckets[i]:
            self.buckets[i].append(key)
    def remove(self, key: int) -> None:
        i = key % self.size
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.size]

