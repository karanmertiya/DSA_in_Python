# Heaps Revision Table

<table border="1">
  <thead>
    <tr>
      <th rowspan="2" style="width: 5%;">S.No</th>
      <th rowspan="2" style="width: 15%;">Problem Name</th>
      <th rowspan="2" style="width: 25%;">Example & Constraints</th>
      <th rowspan="2" style="width: 10%;">Complexity</th>
      <th colspan="2" style="width: 20%;">Conditions & Edge Cases</th>
      <th rowspan="2" style="width: 25%;">Logic</th>
    </tr>
    <tr>
      <th>Dependencies / Setup</th>
      <th>Edge Case Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1">1</td>
      <td rowspan="1">Heap 01 Kth Largest Element In An Array<br><br></b> <a href='https://leetcode.com/problems/kth-largest-element-in-an-array/' target='_blank'>LeetCode 215</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [3,2,1,5,6,4], k = 2, Output: 5<br><br><b>Note (Constraint):</b> Can you solve it without sorting?</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td><code>std::priority_queue</code> / <code>heapq</code></td>
      <td><b>Min-Heap sizing:</b> By strictly keeping the size to `k`, the `k` largest elements are trapped inside, with the smallest of them right at the top.</td>
      <td><b>Explanation:</b> Use a Min-Heap of size K. When the heap exceeds size K, pop the minimum element. The top of the heap will be the Kth largest.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def find_kth_largest(nums: list[int], k: int) -&gt; int:&#10;    min_heap = []&#10;    for num in nums:&#10;        heapq.heappush(min_heap, num)&#10;        if len(min_heap) &gt; k:&#10;            heapq.heappop(min_heap)&#10;    return min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Heap 02 Merge K Sorted Lists<br><br></b> <a href='https://leetcode.com/problems/merge-k-sorted-lists/' target='_blank'>LeetCode 23</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: lists = [[1,4,5],[1,3,4],[2,6]], Output: [1,1,2,3,4,4,5,6]</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td>Custom Comparator</td>
      <td><b>Pointer Compare:</b> Priority queues need a custom comparator to sort `ListNode*` by their `val`.</td>
      <td><b>Explanation:</b> Push the head of each list into a Min-Heap. Repeatedly pop the smallest node, attach it to the result list, and push its `next` node into the heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def merge_k_lists(lists: list[ListNode]) -&gt; ListNode:&#10;    # To avoid comparing ListNodes directly in Python heapq, store (val, index, node)&#10;    heap = []&#10;    for i, lst in enumerate(lists):&#10;        if lst:&#10;            heapq.heappush(heap, (lst.val, i, lst))&#10;            &#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    &#10;    while heap:&#10;        val, i, node = heapq.heappop(heap)&#10;        tail.next = node&#10;        tail = tail.next&#10;        if node.next:&#10;            heapq.heappush(heap, (node.next.val, i, node.next))&#10;            &#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Heap 03 Top K Frequent Elements<br><br></b> <a href='https://leetcode.com/problems/top-k-frequent-elements/' target='_blank'>LeetCode 347</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,1,1,2,2,3], k = 2, Output: [1,2]</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(N)</td>
      <td><code>std::priority_queue</code>, <code>heapq</code></td>
      <td><b>Min-Heap capacity:</b> If heap size exceeds `k`, pop the top (which is the element with the lowest frequency currently in the heap).</td>
      <td><b>Explanation:</b> Use a Hash Map to count frequencies. Use a Min-Heap of size `k` to keep track of the top `k` elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;from collections import Counter&#10;def topKFrequent(nums: list[int], k: int) -&gt; list[int]:&#10;    count = Counter(nums)&#10;    return heapq.nlargest(k, count.keys(), key=count.get)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Heaps 04 Merge K Sorted Lists<br><br></b> <a href='https://leetcode.com/problems/merge-k-sorted-lists/' target='_blank'>LeetCode 23</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: lists=[[1,4,5],[1,3,4],[2,6]], Output: [1,1,2,3,4,4,5,6]</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td><b>Custom Comparator:</b> In C++, define a struct to compare ListNode* values.</td>
      <td><b>Explanation:</b> Use a Min-Heap. Push the head of each linked list into the Priority Queue. Continuously pop the smallest, append it to result, and push its `next` node into the PQ.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKLists(lists: List[Optional[ListNode]]) -&gt; Optional[ListNode]:&#10;    pq = []&#10;    for i, l in enumerate(lists):&#10;        if l: heapq.heappush(pq, (l.val, i, l))&#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    while pq:&#10;        val, i, node = heapq.heappop(pq)&#10;        tail.next = node&#10;        tail = tail.next&#10;        if node.next:&#10;            heapq.heappush(pq, (node.next.val, i, node.next))&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Heap 06 Kth Largest Element In An Array<br><br></b> <a href='https://leetcode.com/problems/kth-largest-element-in-an-array/' target='_blank'>LeetCode 215</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [3,2,1,5,6,4], k = 2. Output: 5</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a Min-Heap of size K. Push elements into the heap. If heap size exceeds K, pop the minimum element. The top of the heap at the end is the Kth largest element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def findKthLargest(nums: List[int], k: int) -&gt; int:&#10;    minH = []&#10;    for num in nums:&#10;        heapq.heappush(minH, num)&#10;        if len(minH) &gt; k:&#10;            heapq.heappop(minH)&#10;    return minH[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Heap 07 Kth Smallest Element In A Sorted Matrix<br><br></b> <a href='https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/' target='_blank'>LeetCode 378</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary search on range.</td>
      <td><b>Time:</b> O(N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on the value range `[matrix[0][0], matrix[n-1][n-1]]`. Count elements less than or equal to `mid` using two pointers (start from bottom-left). If count >= k, search left half, else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(matrix: List[List[int]], k: int) -&gt; int:&#10;    n = len(matrix)&#10;    def countLessOrEqual(mid):&#10;        count, r, c = 0, n - 1, 0&#10;        while r &gt;= 0 and c &lt; n:&#10;            if matrix[r][c] &lt;= mid:&#10;                count += r + 1&#10;                c += 1&#10;            else:&#10;                r -= 1&#10;        return count&#10;    low, high = matrix[0][0], matrix[-1][-1]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if countLessOrEqual(mid) &gt;= k:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Heap 08 Find Median From Data Stream<br><br></b> <a href='https://leetcode.com/problems/find-median-from-data-stream/' target='_blank'>LeetCode 295</a></td>
      <td rowspan="1"><b>Example 1:</b> Two heaps.</td>
      <td><b>Time:</b> O(log N) add, O(1) find<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain two heaps: a max-heap for the smaller half of numbers and a min-heap for the larger half. Balance them such that the max-heap has at most 1 more element than the min-heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class MedianFinder:&#10;    def __init__(self):&#10;        self.small = []&#10;        self.large = []&#10;    def addNum(self, num: int) -&gt; None:&#10;        heapq.heappush(self.small, -num)&#10;        heapq.heappush(self.large, -heapq.heappop(self.small))&#10;        if len(self.small) &lt; len(self.large):&#10;            heapq.heappush(self.small, -heapq.heappop(self.large))&#10;    def findMedian(self) -&gt; float:&#10;        if len(self.small) &gt; len(self.large): return -self.small[0]&#10;        return (-self.small[0] + self.large[0]) / 2.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Heap 09 Merge K Sorted Lists<br><br></b> <a href='https://leetcode.com/problems/merge-k-sorted-lists/' target='_blank'>LeetCode 23</a></td>
      <td rowspan="1"><b>Example 1:</b> Use Min-Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td><b>Empty lists:</b> Ignore nullptrs.</td>
      <td><b>Explanation:</b> Push the heads of all K lists into a Min-Heap. Pop the smallest node, append it to result, and if it has a next node, push the next node into the heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKLists(lists: List[Optional[ListNode]]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    pq = []&#10;    for i, head in enumerate(lists):&#10;        if head: heapq.heappush(pq, (head.val, i, head))&#10;    while pq:&#10;        val, i, node = heapq.heappop(pq)&#10;        tail.next = node&#10;        tail = node&#10;        if node.next:&#10;            heapq.heappush(pq, (node.next.val, i, node.next))&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Heap 10 Top K Frequent Elements<br><br></b> <a href='https://leetcode.com/problems/top-k-frequent-elements/' target='_blank'>LeetCode 347</a></td>
      <td rowspan="1"><b>Example 1:</b> Output: elements.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Count frequencies using a map. Use a Min-Heap of size K, storing pairs `(freq, num)`. If size > K, pop. Heap will contain the top K elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections, heapq&#10;def topKFrequent(nums: List[int], k: int) -&gt; List[int]:&#10;    count = collections.Counter(nums)&#10;    return heapq.nlargest(k, count.keys(), key=count.get)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Heap 11 Sort Characters By Frequency<br><br></b> <a href='https://leetcode.com/problems/sort-characters-by-frequency/' target='_blank'>LeetCode 451</a></td>
      <td rowspan="1"><b>Example 1:</b> `s = "tree"`. Output: `"eert"`.</td>
      <td><b>Time:</b> O(N log 26)<br><b>Space:</b> O(26)</td>
      <td><code>#include <unordered_map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Hash map to store frequencies, then max-heap to process them in descending order of frequency.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def frequencySort(s: str) -&gt; str:&#10;    counts = collections.Counter(s)&#10;    ans = &quot;&quot;&#10;    for char, freq in counts.most_common():&#10;        ans += char * freq&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Heap 12 Replace Each Array Element By Its Corresponding Rank<br><br></b> <a href='https://leetcode.com/problems/rank-transform-of-an-array/' target='_blank'>LeetCode 1331</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: [40,10,20,30], Output: [4,1,2,3]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map>\n#include <set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Create a copy of array, sort it, and remove duplicates. Use a hash map to map each unique value to its rank. Replace elements in original array using map.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arrayRankTransform(arr: List[int]) -&gt; List[int]:&#10;    st = sorted(list(set(arr)))&#10;    mpp = {num: rank + 1 for rank, num in enumerate(st)}&#10;    return [mpp[num] for num in arr]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Heap 13 Task Scheduler<br><br></b> <a href='https://leetcode.com/problems/task-scheduler/' target='_blank'>LeetCode 621</a></td>
      <td rowspan="1"><b>Example 1:</b> Greedy placement.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Find max frequency `max_f`. Calculate idle slots `(max_f - 1) * n`. Iterate remaining frequencies and subtract from idle slots. Return `tasks.length + max(0, idle_slots)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def leastInterval(tasks: List[str], n: int) -&gt; int:&#10;    counts = list(collections.Counter(tasks).values())&#10;    max_f = max(counts)&#10;    count_max = counts.count(max_f)&#10;    ans = (max_f - 1) * (n + 1) + count_max&#10;    return max(ans, len(tasks))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Heap 14 Hand Of Straights<br><br></b> <a href='https://leetcode.com/problems/hand-of-straights/' target='_blank'>LeetCode 846</a></td>
      <td rowspan="1"><b>Example 1:</b> Form consecutive sequences.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a map (TreeMap in C++) to store frequencies. Iterate through map. If a number has count > 0, we must form a group starting from it. Decrement counts of `num, num+1, ..., num+groupSize-1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def isNStraightHand(hand: List[int], groupSize: int) -&gt; bool:&#10;    if len(hand) % groupSize != 0: return False&#10;    count = collections.Counter(hand)&#10;    for card in sorted(count.keys()):&#10;        if count[card] &gt; 0:&#10;            c = count[card]&#10;            for i in range(groupSize):&#10;                if count[card + i] &lt; c: return False&#10;                count[card + i] -= c&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Heap 15 Design Twitter<br><br></b> <a href='https://leetcode.com/problems/design-twitter/' target='_blank'>LeetCode 355</a></td>
      <td rowspan="1"><b>Example 1:</b> Object oriented design.</td>
      <td><b>Time:</b> O(N log 10)<br><b>Space:</b> O(U + T)</td>
      <td><code>#include <unordered_map>\n#include <unordered_set>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a hash map to map user to their followees. Use another map to map user to their tweets. For news feed, use a Max-Heap to extract the 10 most recent tweets from the user and their followees.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;import collections&#10;class Twitter:&#10;    def __init__(self):&#10;        self.time = 0&#10;        self.tweets = collections.defaultdict(list)&#10;        self.followers = collections.defaultdict(set)&#10;    def postTweet(self, userId: int, tweetId: int) -&gt; None:&#10;        self.tweets[userId].append((self.time, tweetId))&#10;        self.time -= 1&#10;    def getNewsFeed(self, userId: int) -&gt; List[int]:&#10;        users = self.followers[userId] | {userId}&#10;        hq = []&#10;        for u in users:&#10;            for t in self.tweets[u][-10:]:&#10;                heapq.heappush(hq, t)&#10;        return [t[1] for t in heapq.nsmallest(10, hq)]&#10;    def follow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].add(followeeId)&#10;    def unfollow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].discard(followeeId)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Heap 24 Kth Largest Element In A Stream<br><br></b> <a href='https://leetcode.com/problems/kth-largest-element-in-a-stream/' target='_blank'>LeetCode 703</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-heap of size K.</td>
      <td><b>Time:</b> O(N log K) for init, O(log K) for add<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a min-heap of size exactly `k`. The top of the min-heap will always represent the kth largest element. For every new element added, if the heap size is less than `k`, push it. If the heap is of size `k` and the new element is greater than the top, pop the top and push the new element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class KthLargest:&#10;    def __init__(self, k: int, nums: List[int]):&#10;        self.k = k&#10;        self.min_heap = nums&#10;        heapq.heapify(self.min_heap)&#10;        while len(self.min_heap) &gt; k:&#10;            heapq.heappop(self.min_heap)&#10;    def add(self, val: int) -&gt; int:&#10;        heapq.heappush(self.min_heap, val)&#10;        if len(self.min_heap) &gt; self.k:&#10;            heapq.heappop(self.min_heap)&#10;        return self.min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Heap 25 Kth Largest Element In An Array<br><br></b> <a href='https://leetcode.com/problems/kth-largest-element-in-an-array/' target='_blank'>LeetCode 215</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-heap or Quickselect.</td>
      <td><b>Time:</b> O(N log K) Heap, O(N) avg Quickselect<br><b>Space:</b> O(K) Heap, O(1) Quickselect</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Min-heap: Keep a min-heap of size K. The root is the Kth largest. Quickselect: Partition the array like in Quicksort, recursively searching only the partition containing the target index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def findKthLargest(nums: List[int], k: int) -&gt; int:&#10;    return heapq.nlargest(k, nums)[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Heap 26 K Closest Points To Origin<br><br></b> <a href='https://leetcode.com/problems/k-closest-points-to-origin/' target='_blank'>LeetCode 973</a></td>
      <td rowspan="1"><b>Example 1:</b> Max-heap of pairs.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a max-heap of size `k` to store pairs of `(distance, point_index)`. Iterate over all points, push into heap. If heap size exceeds `k`, pop the max element. The heap will eventually hold the `k` points with minimum distance.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kClosest(points: List[List[int]], k: int) -&gt; List[List[int]]:&#10;    heap = []&#10;    for i, (x, y) in enumerate(points):&#10;        dist = -(x*x + y*y)&#10;        if len(heap) &lt; k:&#10;            heapq.heappush(heap, (dist, i))&#10;        else:&#10;            heapq.heappushpop(heap, (dist, i))&#10;    return [points[i] for _, i in heap]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Heap 27 Top K Frequent Elements<br><br></b> <a href='https://leetcode.com/problems/top-k-frequent-elements/' target='_blank'>LeetCode 347</a></td>
      <td rowspan="1"><b>Example 1:</b> Hash map + Min-heap or Bucket sort.</td>
      <td><b>Time:</b> O(N log K) Heap, O(N) Bucket Sort<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Count frequencies using a hash map. Use a min-heap of size `k` storing pairs of `(frequency, element)`. Or use bucket sort where index is frequency and value is list of elements with that frequency.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;import heapq&#10;def topKFrequent(nums: List[int], k: int) -&gt; List[int]:&#10;    counts = collections.Counter(nums)&#10;    return heapq.nlargest(k, counts.keys(), key=counts.get)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Heap 28 Sort Characters By Frequency<br><br></b> <a href='https://leetcode.com/problems/sort-characters-by-frequency/' target='_blank'>LeetCode 451</a></td>
      <td rowspan="1"><b>Example 1:</b> Hash map + Max-heap or Sort.</td>
      <td><b>Time:</b> O(N log M) where M is unique characters<br><b>Space:</b> O(M)</td>
      <td><code>#include <unordered_map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Count frequencies of each character. Store pairs of `(frequency, character)` in a max-heap (or sort an array). Construct the result string by popping from the heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def frequencySort(s: str) -&gt; str:&#10;    counts = collections.Counter(s)&#10;    return &quot;&quot;.join([char * count for char, count in counts.most_common()])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Heap 29 Find Median From Data Stream<br><br></b> <a href='https://leetcode.com/problems/find-median-from-data-stream/' target='_blank'>LeetCode 295</a></td>
      <td rowspan="1"><b>Example 1:</b> Two heaps (Max-heap for lower half, Min-heap for upper half).</td>
      <td><b>Time:</b> O(log N) add, O(1) find<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use two heaps: a max-heap for the smaller half of numbers, and a min-heap for the larger half. Keep the sizes balanced (either equal, or max-heap has 1 more). Median is root of max-heap (odd total) or average of both roots (even total).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class MedianFinder:&#10;    def __init__(self):&#10;        self.small, self.large = [], []&#10;    def addNum(self, num: int) -&gt; None:&#10;        heapq.heappush(self.large, num)&#10;        heapq.heappush(self.small, -heapq.heappop(self.large))&#10;        if len(self.small) &gt; len(self.large):&#10;            heapq.heappush(self.large, -heapq.heappop(self.small))&#10;    def findMedian(self) -&gt; float:&#10;        if len(self.large) &gt; len(self.small):&#10;            return self.large[0]&#10;        return (self.large[0] - self.small[0]) / 2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Heap 30 Merge K Sorted Lists<br><br></b> <a href='https://leetcode.com/problems/merge-k-sorted-lists/' target='_blank'>LeetCode 23</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-heap of list nodes.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Push the head of each list into a min-heap. Extract the minimum node, append it to the merged list, and push its next node (if any) into the min-heap. Repeat until heap is empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKLists(lists: List[Optional[ListNode]]) -&gt; Optional[ListNode]:&#10;    setattr(ListNode, &quot;__lt__&quot;, lambda self, other: self.val &lt; other.val)&#10;    heap = []&#10;    for node in lists:&#10;        if node:&#10;            heapq.heappush(heap, node)&#10;    dummy = tail = ListNode(0)&#10;    while heap:&#10;        curr = heapq.heappop(heap)&#10;        tail.next = curr&#10;        tail = tail.next&#10;        if curr.next:&#10;            heapq.heappush(heap, curr.next)&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Heap 31 Task Scheduler<br><br></b> <a href='https://leetcode.com/problems/task-scheduler/' target='_blank'>LeetCode 621</a></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry. See Greedy chapter.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> See greedy_37_task_scheduler.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Implementation provided in greedy chapter.</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Heap 32 Design Twitter<br><br></b> <a href='https://leetcode.com/problems/design-twitter/' target='_blank'>LeetCode 355</a></td>
      <td rowspan="1"><b>Example 1:</b> Heap to merge multiple sorted lists.</td>
      <td><b>Time:</b> O(K log K) for feed where K is 10.<br><b>Space:</b> O(Total Tweets + Follow Relations)</td>
      <td><code>#include <unordered_map>\n#include <unordered_set>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a timestamp for tweets. Each user has a list of tweets and a set of followed users. To get the news feed, gather the most recent tweets from the user and all followees using a max-heap (like merging K sorted lists).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;import heapq&#10;class Twitter:&#10;    def __init__(self):&#10;        self.time = 0&#10;        self.tweets = collections.defaultdict(list)&#10;        self.followees = collections.defaultdict(set)&#10;    def postTweet(self, userId: int, tweetId: int) -&gt; None:&#10;        self.tweets[userId].append((self.time, tweetId))&#10;        self.time += 1&#10;    def getNewsFeed(self, userId: int) -&gt; List[int]:&#10;        users = self.followees[userId] | {userId}&#10;        heap = []&#10;        for u in users:&#10;            if self.tweets[u]:&#10;                idx = len(self.tweets[u]) - 1&#10;                t, tweetId = self.tweets[u][idx]&#10;                heapq.heappush(heap, (-t, tweetId, u, idx - 1))&#10;        res = []&#10;        while heap and len(res) &lt; 10:&#10;            _, tweetId, u, idx = heapq.heappop(heap)&#10;            res.append(tweetId)&#10;            if idx &gt;= 0:&#10;                t, nxtTweetId = self.tweets[u][idx]&#10;                heapq.heappush(heap, (-t, nxtTweetId, u, idx - 1))&#10;        return res&#10;    def follow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followees[followerId].add(followeeId)&#10;    def unfollow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followees[followerId].discard(followeeId)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Heap 33 Reorganize String<br><br></b> <a href='https://leetcode.com/problems/reorganize-string/' target='_blank'>LeetCode 767</a></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry. See Greedy chapter.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> See greedy_38_reorganize_string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Implementation provided in greedy chapter.</code></pre></details></td>
    </tr>
  </tbody>
</table>
