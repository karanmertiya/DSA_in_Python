# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Push all elements (0 to N-1) into a stack. Pop two elements `A` and `B`. If `A` knows `B`, `A` cannot be a celebrity, push `B` back. If `A` does not know `B`, `B` cannot be a celebrity, push `A` back. The remaining element is a potential celebrity. Verify it by checking if everyone knows it and it knows no one.

def celebrity(M: List[List[int]], n: int) -> int:
    st = list(range(n))
    while len(st) > 1:
        a = st.pop()
        b = st.pop()
        if M[a][b] == 1:
            st.append(b)
        else:
            st.append(a)
    if not st: return -1
    pot = st[0]
    for i in range(n):
        if i != pot and (M[pot][i] == 1 or M[i][pot] == 0):
            return -1
    return pot

