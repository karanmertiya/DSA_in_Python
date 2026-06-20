# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Recursively pop elements until the stack is empty. When returning from the recursive call, use another recursive function `sortedInsert` to insert the popped element into its correct sorted position in the stack.

def sortedInsert(s, element):
    if not s or element > s[-1]:
        s.append(element)
        return
    num = s.pop()
    sortedInsert(s, element)
    s.append(num)
def sortStack(s):
    if not s: return
    num = s.pop()
    sortStack(s)
    sortedInsert(s, num)

