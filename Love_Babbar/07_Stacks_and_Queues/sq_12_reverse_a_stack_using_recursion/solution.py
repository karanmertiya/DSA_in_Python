# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Recursively pop all elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `insertAtBottom` to push the elements at the bottom.

def Reverse(St: List[int]) -> None:
    def insertAtBottom(St, X):
        if not St:
            St.append(X)
            return
        top = St.pop()
        insertAtBottom(St, X)
        St.append(top)
    if not St: return
    top = St.pop()
    Reverse(St)
    insertAtBottom(St, top)

