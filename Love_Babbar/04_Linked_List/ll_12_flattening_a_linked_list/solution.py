# Time Complexity: O(N * M)
# Space Complexity: O(N)
# Explanation: Recursively flatten the `next` list, then merge the current list (`bottom` pointers) with the flattened `next` list, similar to merging two sorted linked lists.

def flatten(root):
    def mergeTwoLists(a, b):
        temp = Node(0)
        res = temp
        while a and b:
            if a.data < b.data:
                temp.bottom = a; temp = temp.bottom; a = a.bottom
            else:
                temp.bottom = b; temp = temp.bottom; b = b.bottom
        if a: temp.bottom = a
        else: temp.bottom = b
        return res.bottom
    if not root or not root.next: return root
    root.next = flatten(root.next)
    root = mergeTwoLists(root, root.next)
    return root

