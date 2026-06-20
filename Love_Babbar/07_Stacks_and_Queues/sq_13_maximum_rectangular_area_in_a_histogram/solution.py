# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a stack to find Next Smaller Element (NSE) and Previous Smaller Element (PSE) for each bar. Then, the width of the rectangle with bar `i` as the minimum height is `NSE[i] - PSE[i] - 1`. The area is `height[i] * width`.

def getMaxArea(arr: List[int], n: int) -> int:
    st = []
    max_area = 0
    for i in range(n + 1):
        while st and (i == n or arr[st[-1]] >= arr[i]):
            height = arr[st.pop()]
            width = i if not st else i - st[-1] - 1
            max_area = max(max_area, height * width)
        st.append(i)
    return max_area

