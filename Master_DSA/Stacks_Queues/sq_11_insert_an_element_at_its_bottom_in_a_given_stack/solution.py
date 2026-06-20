# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use recursion. If the stack is empty, push the element. Otherwise, pop the top element, recursively call the function, and then push the popped element back.

def insertAtBottom(St: List[int], X: int) -> List[int]:
    if not St:
        St.append(X)
        return St
    top = St.pop()
    insertAtBottom(St, X)
    St.append(top)
    return St

