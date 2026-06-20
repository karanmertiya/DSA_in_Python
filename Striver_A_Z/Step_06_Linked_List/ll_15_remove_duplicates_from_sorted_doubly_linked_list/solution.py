# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the DLL. While `next` node has the same value, bypass it by updating `curr->next` and `curr->next->prev`.

def removeDuplicates(head):
    curr = head
    while curr:
        nextNode = curr.next
        while nextNode and nextNode.data == curr.data:
            nextNode = nextNode.next
        curr.next = nextNode
        if nextNode:
            nextNode.prev = curr
        curr = curr.next
    return head

