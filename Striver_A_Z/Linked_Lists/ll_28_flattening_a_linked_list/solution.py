# Time Complexity: O(N * M) total nodes
# Space Complexity: O(N) aux space for recursion
# Explanation: Recursively go to the end of the `next` pointers. Merge the last two lists using the `bottom` pointers, just like merging two sorted linked lists. Return the merged head upwards.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None
def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp
    while a is not None and b is not None:
        if a.data < b.data:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    if a: temp.bottom = a
    else: temp.bottom = b
    return res.bottom
def flatten(root):
    if root is None or root.next is None: return root
    root.next = flatten(root.next)
    root = mergeTwoLists(root, root.next)
    return root

