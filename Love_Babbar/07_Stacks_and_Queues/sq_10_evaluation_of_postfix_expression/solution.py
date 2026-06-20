# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Iterate through the string. If it's a number, push it to stack. If it's an operator, pop two numbers from stack, apply the operator, and push the result back to stack.

def evaluatePostfix(S: str) -> int:
    st = []
    for c in S:
        if c.isdigit():
            st.append(int(c))
        else:
            op2 = st.pop()
            op1 = st.pop()
            if c == '+': st.append(op1 + op2)
            elif c == '-': st.append(op1 - op2)
            elif c == '*': st.append(op1 * op2)
            elif c == '/': st.append(int(op1 / op2))
    return st[-1]

