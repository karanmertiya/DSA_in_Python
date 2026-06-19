# Time Complexity: O(N * M)
# Space Complexity: O(N) for recursion
# Explanation: Recursively flatten the `next` list, then merge the current list (`bottom`) with the flattened `next` list using a `merge` function similar to merging two sorted linked lists.

def flatten(root: Node) -> Node:
    def merge(a, b):
        if not a: return b
        if not b: return a
        if a.data < b.data:
            res = a
            res.bottom = merge(a.bottom, b)
        else:
            res = b
            res.bottom = merge(a, b.bottom)
        res.next = None
        return res
    if not root or not root.next: return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root

