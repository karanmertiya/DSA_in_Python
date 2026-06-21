# Time Complexity: O(N + M)
# Space Complexity: O(N)
# Explanation: Monotonic Stack traversing `nums2` from right to left. Maintain stack of elements in decreasing order.

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    mpp = {}
    st = []
    for num in reversed(nums2):
        while st and st[-1] <= num: st.pop()
        mpp[num] = st[-1] if st else -1
        st.append(num)
    return [mpp[num] for num in nums1]

