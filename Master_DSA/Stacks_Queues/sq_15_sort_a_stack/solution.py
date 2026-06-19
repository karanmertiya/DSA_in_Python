# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Recursively pop elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `sortedInsert` to insert the element in its sorted position.

def sortedInsert(s: List[int], x: int):
    if not s or x > s[-1]:
        s.append(x)
        return
    temp = s.pop()
    sortedInsert(s, x)
    s.append(temp)
def sortStack(s: List[int]) -> None:
    if not s: return
    temp = s.pop()
    sortStack(s)
    sortedInsert(s, temp)

