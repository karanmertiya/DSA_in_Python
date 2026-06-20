# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def searchRange(nums: list[int], target: int) -> list[int]:
    def findBound(isFirst):
        low, high, ans = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                if isFirst: high = mid - 1
                else: low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
    return [findBound(True), findBound(False)]

# Time Complexity: O(log N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).

def searchRange(nums: list[int], target: int) -> list[int]:
    def findBound(isFirst):
        low, high, ans = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                if isFirst: high = mid - 1
                else: low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
    return [findBound(True), findBound(False)]

