# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a Stack. Push open brackets. If a closed bracket is found, verify it matches the top of the stack and pop.

def isValid(s: str) -> bool:
    st = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = st.pop() if st else '#'
            if mapping[char] != top: return False
        else:
            st.append(char)
    return not st

