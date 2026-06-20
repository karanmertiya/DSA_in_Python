# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: The inorder traversal of a BST is sorted. First, get the inorder traversal of the given complete binary tree using array indices. Then, the problem reduces to finding the minimum swaps to sort an array. Use graph cycles to find min swaps.

def minSwaps(A, n):
    v = []
    def inorder(index):
        if index >= n: return
        inorder(2 * index + 1)
        v.append(A[index])
        inorder(2 * index + 2)
    inorder(0)
    t = [(val, idx) for idx, val in enumerate(v)]
    t.sort()
    ans = 0
    vis = {i: False for i in range(n)}
    for i in range(n):
        if vis[i] or t[i][1] == i: continue
        cycle_size, j = 0, i
        while not vis[j]:
            vis[j] = True
            j = t[j][1]
            cycle_size += 1
        if cycle_size > 0: ans += (cycle_size - 1)
    return ans

