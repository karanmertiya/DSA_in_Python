# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Push all characters of the string into a stack. Then pop them out one by one. The popped characters will be in reversed order.

def reverse(S: str) -> str:
    st = []
    for c in S:
        st.append(c)
    res = ""
    while st:
        res += st.pop()
    return res

