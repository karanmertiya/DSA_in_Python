# Time Complexity: O(log N) (Constraint)
# Space Complexity: O(1)
# Explanation: Perform two separate binary searches: one for the first occurrence (bias left) and one for the last (bias right).

def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first):
        low, high, res = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                res = mid
                if is_first: high = mid - 1
                else: low = mid + 1
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
        return res
    return [find_bound(True), find_bound(False)]

