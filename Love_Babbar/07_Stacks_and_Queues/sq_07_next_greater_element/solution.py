# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Iterate from right to left. Use a stack to keep track of elements. Pop from the stack while the top element is less than or equal to the current element. If stack is empty, NGE is -1, else it's the stack top. Push current element.

def nextLargerElement(arr: List[int], n: int) -> List[int]:
    res = [-1] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and st[-1] <= arr[i]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(arr[i])
    return res

