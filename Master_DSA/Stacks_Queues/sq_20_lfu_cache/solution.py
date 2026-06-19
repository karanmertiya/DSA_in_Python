# Time Complexity: O(1) for get and put
# Space Complexity: O(Capacity)
# Explanation: Maintain a `minFreq` variable. Use one hash map to map `key` to its Node. Use another hash map to map `frequency` to a Doubly Linked List of Nodes with that frequency. When accessing an element, increase its frequency and move it to the corresponding DLL. If capacity is reached, remove the least recently used element from the DLL at `minFreq`.

class Node:
    def __init__(self, key, value):
        self.key, self.value, self.cnt = key, value, 1
        self.prev = self.next = None
class DLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
    def add_node(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        self.size += 1
    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
class LFUCache:
    def __init__(self, capacity: int):
        self.cap, self.size, self.min_freq = capacity, 0, 0
        self.node_map, self.freq_map = {}, {}
    def update(self, node):
        freq = node.cnt
        self.freq_map[freq].remove_node(node)
        if self.min_freq == freq and not self.freq_map[freq].size:
            self.min_freq += 1
        node.cnt += 1
        if node.cnt not in self.freq_map:
            self.freq_map[node.cnt] = DLinkedList()
        self.freq_map[node.cnt].add_node(node)
    def get(self, key: int) -> int:
        if key not in self.node_map: return -1
        node = self.node_map[key]
        self.update(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.update(node)
        else:
            if self.size == self.cap:
                node_to_remove = self.freq_map[self.min_freq].tail.prev
                self.freq_map[self.min_freq].remove_node(node_to_remove)
                del self.node_map[node_to_remove.key]
                self.size -= 1
            new_node = Node(key, value)
            self.node_map[key] = new_node
            if 1 not in self.freq_map: self.freq_map[1] = DLinkedList()
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size += 1

