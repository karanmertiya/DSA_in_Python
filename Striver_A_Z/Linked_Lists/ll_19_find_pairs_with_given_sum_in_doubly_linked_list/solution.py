# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Since it is a sorted DLL, set one pointer at the head and one at the tail. If sum == x, add to result and move both. If sum < x, move left pointer next. Else, move right pointer prev.

def findPairsWithGivenSum(head, target):
    ans = []
    if not head: return ans
    left = head
    right = head
    while right.next: right = right.next
    while left and right and left.data < right.data:
        if left.data + right.data == target:
            ans.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif left.data + right.data < target:
            left = left.next
        else:
            right = right.prev
    return ans

