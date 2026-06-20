# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Optimal: Calculate the net amount for each person by subtracting incoming debts from outgoing debts. Find the person with maximum net credit and maximum net debit. Settle their amounts, and repeat recursively or iteratively until all net amounts are zero.

def minCashFlow(graph, n):
    amount = [0] * n
    for p in range(n):
        for i in range(n):
            amount[p] += (graph[i][p] - graph[p][i])
    ans = [[0]*n for _ in range(n)]
    def rec(amount):
        mxCredit = amount.index(max(amount))
        mxDebit = amount.index(min(amount))
        if amount[mxCredit] == 0 and amount[mxDebit] == 0: return
        minVal = min(-amount[mxDebit], amount[mxCredit])
        amount[mxCredit] -= minVal
        amount[mxDebit] += minVal
        ans[mxDebit][mxCredit] = minVal
        rec(amount)
    rec(amount)
    return ans

