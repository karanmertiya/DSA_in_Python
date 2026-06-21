# Time Complexity: O(N * 4^N)
# Space Complexity: O(N)
# Explanation: Backtracking. Keep track of the evaluated sum so far, and the previous operand (for multiplication precedence). For '*', `newSum = sum - prev + prev * curr`. Handle leading zeros.

def addOperators(num: str, target: int) -> List[str]:
    ans = []
    def solve(ind, path, eval_sum, multed):
        if ind == len(num):
            if eval_sum == target: ans.append(path)
            return
        for i in range(ind, len(num)):
            if i != ind and num[ind] == '0': break
            cur_str = num[ind:i+1]
            cur_num = int(cur_str)
            if ind == 0:
                solve(i + 1, path + cur_str, cur_num, cur_num)
            else:
                solve(i + 1, path + "+" + cur_str, eval_sum + cur_num, cur_num)
                solve(i + 1, path + "-" + cur_str, eval_sum - cur_num, -cur_num)
                solve(i + 1, path + "*" + cur_str, eval_sum - multed + multed * cur_num, multed * cur_num)
    solve(0, "", 0, 0)
    return ans

