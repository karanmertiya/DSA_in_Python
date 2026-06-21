# Heaps Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 20%;">Example & Constraints</th>
      <th style="width: 10%;">Complexity</th>
      <th style="width: 20%;">Approach & Dependencies</th>
      <th style="width: 30%;">Logic & Edge Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1">1</td>
      <td rowspan="1">Heap 01 Kth Largest Element In An Array<br><br></b> <a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank">LeetCode 215</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [3,2,1,5,6,4], k = 2<br><b>Output:</b> 5<br><br><b>Note (Constraint):</b> Can you solve it without sorting?</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td>Use a Min-Heap of size K. When the heap exceeds size K, pop the minimum element. The top of the heap will be the Kth largest.<br><br><b>Dependencies:</b> <code>std::priority_queue</code> / <code>heapq</code></td>
      <td><b>Edge Cases:</b> <b>Min-Heap sizing:</b> By strictly keeping the size to `k`, the `k` largest elements are trapped inside, with the smallest of them right at the top.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def find_kth_largest(nums: list[int], k: int) -&gt; int:&#10;    min_heap = []&#10;    for num in nums:&#10;        heapq.heappush(min_heap, num)&#10;        if len(min_heap) &gt; k:&#10;            heapq.heappop(min_heap)&#10;    return min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Heap 02 Merge K Sorted Lists<br><br></b> <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">LeetCode 23</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> lists = [[1,4,5],[1,3,4],[2,6]]<br><b>Output:</b> [1,1,2,3,4,4,5,6]</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td>Push the head of each list into a Min-Heap. Repeatedly pop the smallest node, attach it to the result list, and push its `next` node into the heap.<br><br><b>Dependencies:</b> Custom Comparator</td>
      <td><b>Edge Cases:</b> <b>Pointer Compare:</b> Priority queues need a custom comparator to sort `ListNode*` by their `val`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def merge_k_lists(lists: list[ListNode]) -&gt; ListNode:&#10;    # To avoid comparing ListNodes directly in Python heapq, store (val, index, node)&#10;    heap = []&#10;    for i, lst in enumerate(lists):&#10;        if lst:&#10;            heapq.heappush(heap, (lst.val, i, lst))&#10;            &#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    &#10;    while heap:&#10;        val, i, node = heapq.heappop(heap)&#10;        tail.next = node&#10;        tail = tail.next&#10;        if node.next:&#10;            heapq.heappush(heap, (node.next.val, i, node.next))&#10;            &#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Heap 03 Top K Frequent Elements<br><br></b> <a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank">LeetCode 347</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,1,1,2,2,3], k = 2<br><b>Output:</b> [1,2]</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(N)</td>
      <td>Use a Hash Map to count frequencies. Use a Min-Heap of size `k` to keep track of the top `k` elements.<br><br><b>Dependencies:</b> <code>std::priority_queue</code>, <code>heapq</code></td>
      <td><b>Edge Cases:</b> <b>Min-Heap capacity:</b> If heap size exceeds `k`, pop the top (which is the element with the lowest frequency currently in the heap).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;from collections import Counter&#10;def topKFrequent(nums: list[int], k: int) -&gt; list[int]:&#10;    count = Counter(nums)&#10;    return heapq.nlargest(k, count.keys(), key=count.get)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Heap 04 Kth Smallest Element In A Sorted Matrix<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/" target="_blank">LeetCode 378</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Binary search on range.</td>
      <td><b>Time:</b> O(N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>Binary search on the value range `[matrix[0][0], matrix[n-1][n-1]]`. Count elements less than or equal to `mid` using two pointers (start from bottom-left). If count >= k, search left half, else search right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(matrix: List[List[int]], k: int) -&gt; int:&#10;    n = len(matrix)&#10;    def countLessOrEqual(mid):&#10;        count, r, c = 0, n - 1, 0&#10;        while r &gt;= 0 and c &lt; n:&#10;            if matrix[r][c] &lt;= mid:&#10;                count += r + 1&#10;                c += 1&#10;            else:&#10;                r -= 1&#10;        return count&#10;    low, high = matrix[0][0], matrix[-1][-1]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if countLessOrEqual(mid) &gt;= k:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Heap 05 Find Median From Data Stream<br><br></b> <a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank">LeetCode 295</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Two heaps.</td>
      <td><b>Time:</b> O(log N) add, O(1) find<br><b>Space:</b> O(N)</td>
      <td>Maintain two heaps: a max-heap for the smaller half of numbers and a min-heap for the larger half. Balance them such that the max-heap has at most 1 more element than the min-heap.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class MedianFinder:&#10;    def __init__(self):&#10;        self.small = []&#10;        self.large = []&#10;    def addNum(self, num: int) -&gt; None:&#10;        heapq.heappush(self.small, -num)&#10;        heapq.heappush(self.large, -heapq.heappop(self.small))&#10;        if len(self.small) &lt; len(self.large):&#10;            heapq.heappush(self.small, -heapq.heappop(self.large))&#10;    def findMedian(self) -&gt; float:&#10;        if len(self.small) &gt; len(self.large): return -self.small[0]&#10;        return (-self.small[0] + self.large[0]) / 2.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Heap 06 Replace Each Array Element By Its Corresponding Rank<br><br></b> <a href="https://leetcode.com/problems/rank-transform-of-an-array/" target="_blank">LeetCode 1331</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> [40,10,20,30]<br><b>Output:</b> [4,1,2,3]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Create a copy of array, sort it, and remove duplicates. Use a hash map to map each unique value to its rank. Replace elements in original array using map.<br><br><b>Dependencies:</b> <code>#include <unordered_map>\n#include <set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arrayRankTransform(arr: List[int]) -&gt; List[int]:&#10;    st = sorted(list(set(arr)))&#10;    mpp = {num: rank + 1 for rank, num in enumerate(st)}&#10;    return [mpp[num] for num in arr]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Heap 07 Task Scheduler<br><br></b> <a href="https://leetcode.com/problems/task-scheduler/" target="_blank">LeetCode 621</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Greedy placement.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Find max frequency `max_f`. Calculate idle slots `(max_f - 1) * n`. Iterate remaining frequencies and subtract from idle slots. Return `tasks.length + max(0, idle_slots)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def leastInterval(tasks: List[str], n: int) -&gt; int:&#10;    counts = list(collections.Counter(tasks).values())&#10;    max_f = max(counts)&#10;    count_max = counts.count(max_f)&#10;    ans = (max_f - 1) * (n + 1) + count_max&#10;    return max(ans, len(tasks))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Heap 08 Hand Of Straights<br><br></b> <a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">LeetCode 846</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Form consecutive sequences.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Use a map (TreeMap in C++) to store frequencies. Iterate through map. If a number has count > 0, we must form a group starting from it. Decrement counts of `num, num+1, ..., num+groupSize-1`.<br><br><b>Dependencies:</b> <code>#include <map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def isNStraightHand(hand: List[int], groupSize: int) -&gt; bool:&#10;    if len(hand) % groupSize != 0: return False&#10;    count = collections.Counter(hand)&#10;    for card in sorted(count.keys()):&#10;        if count[card] &gt; 0:&#10;            c = count[card]&#10;            for i in range(groupSize):&#10;                if count[card + i] &lt; c: return False&#10;                count[card + i] -= c&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Heap 09 Design Twitter<br><br></b> <a href="https://leetcode.com/problems/design-twitter/" target="_blank">LeetCode 355</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Object oriented design.</td>
      <td><b>Time:</b> O(N log 10)<br><b>Space:</b> O(U + T)</td>
      <td>Use a hash map to map user to their followees. Use another map to map user to their tweets. For news feed, use a Max-Heap to extract the 10 most recent tweets from the user and their followees.<br><br><b>Dependencies:</b> <code>#include <unordered_map>\n#include <unordered_set>\n#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;import collections&#10;class Twitter:&#10;    def __init__(self):&#10;        self.time = 0&#10;        self.tweets = collections.defaultdict(list)&#10;        self.followers = collections.defaultdict(set)&#10;    def postTweet(self, userId: int, tweetId: int) -&gt; None:&#10;        self.tweets[userId].append((self.time, tweetId))&#10;        self.time -= 1&#10;    def getNewsFeed(self, userId: int) -&gt; List[int]:&#10;        users = self.followers[userId] | {userId}&#10;        hq = []&#10;        for u in users:&#10;            for t in self.tweets[u][-10:]:&#10;                heapq.heappush(hq, t)&#10;        return [t[1] for t in heapq.nsmallest(10, hq)]&#10;    def follow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].add(followeeId)&#10;    def unfollow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].discard(followeeId)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Heap 10 Kth Largest Element In A Stream<br><br></b> <a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank">LeetCode 703</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Min-heap of size K.</td>
      <td><b>Time:</b> O(N log K) for init, O(log K) for add<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size exactly `k`. The top of the min-heap will always represent the kth largest element. For every new element added, if the heap size is less than `k`, push it. If the heap is of size `k` and the new element is greater than the top, pop the top and push the new element.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class KthLargest:&#10;    def __init__(self, k: int, nums: List[int]):&#10;        self.k = k&#10;        self.min_heap = nums&#10;        heapq.heapify(self.min_heap)&#10;        while len(self.min_heap) &gt; k:&#10;            heapq.heappop(self.min_heap)&#10;    def add(self, val: int) -&gt; int:&#10;        heapq.heappush(self.min_heap, val)&#10;        if len(self.min_heap) &gt; self.k:&#10;            heapq.heappop(self.min_heap)&#10;        return self.min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Heap 11 K Closest Points To Origin<br><br></b> <a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank">LeetCode 973</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Max-heap of pairs.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a max-heap of size `k` to store pairs of `(distance, point_index)`. Iterate over all points, push into heap. If heap size exceeds `k`, pop the max element. The heap will eventually hold the `k` points with minimum distance.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kClosest(points: List[List[int]], k: int) -&gt; List[List[int]]:&#10;    heap = []&#10;    for i, (x, y) in enumerate(points):&#10;        dist = -(x*x + y*y)&#10;        if len(heap) &lt; k:&#10;            heapq.heappush(heap, (dist, i))&#10;        else:&#10;            heapq.heappushpop(heap, (dist, i))&#10;    return [points[i] for _, i in heap]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Heap 12 Reorganize String<br><br></b> <a href="https://leetcode.com/problems/reorganize-string/" target="_blank">LeetCode 767</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry. See Greedy chapter.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26)</td>
      <td>See greedy_38_reorganize_string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Implementation provided in greedy chapter.</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Heap 13 Smallest Range In K Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N * K * log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K, storing the first element of each list along with its list index and element index. Keep track of the `max_val` currently in the heap. The current range is `[heap_min, max_val]`. Extract the min, update the smallest range if needed, and insert the next element from the extracted element's list. Update `max_val` with the new element.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def findSmallestRange(KSortedArray: List[List[int]], n: int, k: int) -&gt; List[int]:&#10;    pq = []&#10;    mx = float(&#x27;-inf&#x27;)&#10;    for i in range(k):&#10;        heapq.heappush(pq, (KSortedArray[i][0], i, 0))&#10;        mx = max(mx, KSortedArray[i][0])&#10;    ans_range = float(&#x27;inf&#x27;)&#10;    start, end = -1, -1&#10;    while pq:&#10;        mn, row, col = heapq.heappop(pq)&#10;        if mx - mn &lt; ans_range:&#10;            ans_range = mx - mn&#10;            start, end = mn, mx&#10;        if col + 1 &lt; n:&#10;            next_val = KSortedArray[row][col+1]&#10;            heapq.heappush(pq, (next_val, row, col+1))&#10;            mx = max(mx, next_val)&#10;        else:&#10;            break&#10;    return [start, end]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Heap 14 Kth Largest Sum Contiguous Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N^2 log K)<br><b>Space:</b> O(K)</td>
      <td>Iterate all subarrays using two nested loops. Maintain a min-heap of size K to store the top K sums. If the heap size < K, push the current sum. If the heap size == K and current sum > heap top, pop and push current sum. The top of the heap is the Kth largest sum.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargest(Arr: List[int], N: int, K: int) -&gt; int:&#10;    pq = []&#10;    for i in range(N):&#10;        s = 0&#10;        for j in range(i, N):&#10;            s += Arr[j]&#10;            if len(pq) &lt; K:&#10;                heapq.heappush(pq, s)&#10;            elif s &gt; pq[0]:&#10;                heapq.heappop(pq)&#10;                heapq.heappush(pq, s)&#10;    return pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Heap 15 Minimum Sum Of Two Numbers Formed From Digits Of An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-sum4058/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Sort or Min-Heap.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Sort the array. Build two strings representing the two numbers by picking digits alternately from the sorted array. Add the two large numbers as strings or build the result dynamically.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(arr: List[int], n: int) -&gt; str:&#10;    arr.sort()&#10;    a, b = &quot;&quot;, &quot;&quot;&#10;    for i in range(n):&#10;        if i % 2 == 0:&#10;            a += str(arr[i])&#10;        else:&#10;            b += str(arr[i])&#10;    res = str(int(a) + int(b)) if a and b else str(int(a or &#x27;0&#x27;) + int(b or &#x27;0&#x27;))&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Heap 16 Is Binary Tree Heap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Tree Traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>First, check if the tree is complete by counting nodes and ensuring no node's index `i > count`. Then check if every node satisfies the max-heap property (`node.val >= left.val` and `node.val >= right.val`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isHeap(tree: Node) -&gt; bool:&#10;    def countNodes(node):&#10;        if not node: return 0&#10;        return 1 + countNodes(node.left) + countNodes(node.right)&#10;    def isCBT(node, index, count):&#10;        if not node: return True&#10;        if index &gt;= count: return False&#10;        return isCBT(node.left, 2 * index + 1, count) and isCBT(node.right, 2 * index + 2, count)&#10;    def isMaxOrder(node):&#10;        if not node.left and not node.right: return True&#10;        if not node.right: return node.data &gt;= node.left.data&#10;        return (node.data &gt;= node.left.data and node.data &gt;= node.right.data and&#10;                isMaxOrder(node.left) and isMaxOrder(node.right))&#10;    count = countNodes(tree)&#10;    return isCBT(tree, 0, count) and isMaxOrder(tree)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Heap 17 Convert Min Heap To Max Heap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666738710/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Heapify.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(log N) for recursion</td>
      <td>Apply the standard max-heapify process starting from the last non-leaf node `(N/2 - 1)` down to the root. This takes O(N) time.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertMinToMaxHeap(arr: List[int], N: int):&#10;    def maxHeapify(i):&#10;        largest, left, right = i, 2 * i + 1, 2 * i + 2&#10;        if left &lt; N and arr[left] &gt; arr[largest]: largest = left&#10;        if right &lt; N and arr[right] &gt; arr[largest]: largest = right&#10;        if largest != i:&#10;            arr[i], arr[largest] = arr[largest], arr[i]&#10;            maxHeapify(largest)&#10;    for i in range((N - 2) // 2, -1, -1):&#10;        maxHeapify(i)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Heap 18 Minimum Cost Of Ropes<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap Greedy.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Use a min-heap. Pop two minimum length ropes, add them up, add sum to total cost, and push the merged rope back to the heap. Repeat until one rope remains.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def minCost(arr: List[int], n: int) -&gt; int:&#10;    pq = list(arr)&#10;    heapq.heapify(pq)&#10;    cost = 0&#10;    while len(pq) &gt; 1:&#10;        a = heapq.heappop(pq)&#10;        b = heapq.heappop(pq)&#10;        cost += a + b&#10;        heapq.heappush(pq, a + b)&#10;    return cost</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Heap 19 K Th Largest Element In A Stream<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap of size K.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K. While processing the stream, if heap size is < K, push current element. If heap size == K and current element is > heap top, pop and push current element. Append heap top to result if size is K, else append -1.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargest(k: int, arr: List[int], n: int) -&gt; List[int]:&#10;    res = []&#10;    pq = []&#10;    for i in range(n):&#10;        if len(pq) &lt; k:&#10;            heapq.heappush(pq, arr[i])&#10;        elif arr[i] &gt; pq[0]:&#10;            heapq.heappop(pq)&#10;            heapq.heappush(pq, arr[i])&#10;        if len(pq) &lt; k:&#10;            res.append(-1)&#10;        else:&#10;            res.append(pq[0])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Heap 20 Merge K Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(K^2 log K)<br><b>Space:</b> O(K)</td>
      <td>Create a min-heap that stores a tuple: (value, array_index, element_index). Push the first element of each of the K arrays into the heap. While the heap is not empty, pop the minimum element, add it to the result, and if the array from which it was popped has more elements, push the next element to the heap.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKArrays(arr: List[List[int]], K: int) -&gt; List[int]:&#10;    pq = []&#10;    res = []&#10;    for i in range(K):&#10;        heapq.heappush(pq, (arr[i][0], i, 0))&#10;    while pq:&#10;        val, row, col = heapq.heappop(pq)&#10;        res.append(val)&#10;        if col + 1 &lt; len(arr[row]):&#10;            heapq.heappush(pq, (arr[row][col + 1], row, col + 1))&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Heap 21 Smallest Range Covering Elements From K Lists<br><br></b> <a href="https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/" target="_blank">LeetCode 632</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a min-heap storing `(value, list_idx, elem_idx)`. Also maintain the `current_max` of the elements currently in the heap. The current range is `[heap_top, current_max]`. Pop the min, push the next element from its list, and update `current_max`. Continue until any list is exhausted.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def smallestRange(nums: List[List[int]]) -&gt; List[int]:&#10;    pq = []&#10;    currMax = float(&#x27;-inf&#x27;)&#10;    for i in range(len(nums)):&#10;        heapq.heappush(pq, (nums[i][0], i, 0))&#10;        currMax = max(currMax, nums[i][0])&#10;    ans = [pq[0][0], currMax]&#10;    while True:&#10;        val, r, c = heapq.heappop(pq)&#10;        if currMax - val &lt; ans[1] - ans[0]:&#10;            ans = [val, currMax]&#10;        if c + 1 == len(nums[r]):&#10;            break&#10;        next_val = nums[r][c + 1]&#10;        heapq.heappush(pq, (next_val, r, c + 1))&#10;        currMax = max(currMax, next_val)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Heap 22 K Largest Elements<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K. Iterate through the array. If the heap has < K elements, push. Else if the current element > heap's top, pop the top and push the current element. The heap will contain the K largest elements.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kLargest(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    pq = []&#10;    for i in range(n):&#10;        heapq.heappush(pq, arr[i])&#10;        if len(pq) &gt; k:&#10;            heapq.heappop(pq)&#10;    return sorted(pq, reverse=True)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Heap 23 Kth Smallest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Max Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a Max Heap of size K. Iterate through the array. For the first K elements, insert them into the heap. For the remaining elements, if the element is smaller than the top of the heap, pop the top and insert the element. The top of the heap will be the Kth smallest element.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthSmallest(arr, l, r, k):&#10;    pq = []&#10;    for i in range(l, r + 1):&#10;        if len(pq) &lt; k: heapq.heappush(pq, -arr[i])&#10;        elif arr[i] &lt; -pq[0]:&#10;            heapq.heappop(pq)&#10;            heapq.heappush(pq, -arr[i])&#10;    return -pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Heap 24 Merge Two Binary Max Heaps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Append and Heapify.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td>Create a new array by appending the two arrays. Then call `heapify` starting from the last non-leaf node `(n/2 - 1)` down to the root `0`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeHeaps(a, b, n, m):&#10;    ans = a + b&#10;    total = n + m&#10;    def heapify(i):&#10;        largest = i&#10;        l = 2 * i + 1&#10;        r = 2 * i + 2&#10;        if l &lt; total and ans[l] &gt; ans[largest]: largest = l&#10;        if r &lt; total and ans[r] &gt; ans[largest]: largest = r&#10;        if largest != i:&#10;            ans[i], ans[largest] = ans[largest], ans[i]&#10;            heapify(largest)&#10;    for i in range(total // 2 - 1, -1, -1):&#10;        heapify(i)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Heap 25 Kth Largest Sum Contiguous Subarray<br><br></b> <a href="https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Prefix sum + Min Heap.</td>
      <td><b>Time:</b> O(N^2 log K)<br><b>Space:</b> O(N + K)</td>
      <td>Iterate through all possible subarrays and calculate their sums using a prefix sum array. Maintain a Min Heap of size K to keep track of the top K sums. At the end, the top of the Min Heap is the K-th largest sum.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargestSum(arr, n, k):&#10;    sum_arr = [0] * (n + 1)&#10;    for i in range(1, n + 1): sum_arr[i] = sum_arr[i - 1] + arr[i - 1]&#10;    pq = []&#10;    for i in range(1, n + 1):&#10;        for j in range(i, n + 1):&#10;            x = sum_arr[j] - sum_arr[i - 1]&#10;            if len(pq) &lt; k: heapq.heappush(pq, x)&#10;            elif x &gt; pq[0]:&#10;                heapq.heappop(pq)&#10;                heapq.heappush(pq, x)&#10;    return pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Heap 26 Convert BST To Min Heap<br><br></b> <a href="https://www.geeksforgeeks.org/convert-bst-min-heap/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Inorder + Preorder.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since a BST inorder gives sorted values, store the inorder traversal in an array. The requirement says left subtree elements < right subtree elements, which matches a Preorder traversal (Root, Left, Right) since we want the smallest element at the root. So do a Preorder traversal of the tree and replace nodes with array elements.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertToMinHeapUtil(root):&#10;    arr = []&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        arr.append(node.data)&#10;        inorder(node.right)&#10;    def preorderFill(node, idx):&#10;        if not node: return&#10;        node.data = arr[idx[0]]&#10;        idx[0] += 1&#10;        preorderFill(node.left, idx)&#10;        preorderFill(node.right, idx)&#10;    inorder(root)&#10;    preorderFill(root, [0])</code></pre></details></td>
    </tr>
  </tbody>
</table>
