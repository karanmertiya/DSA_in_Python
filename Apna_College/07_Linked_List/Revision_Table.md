# 07 Linked List Revision Table

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
      <td rowspan="1">Ll 01 Intersection Of Two Linked Lists<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-linked-lists/" target="_blank">LeetCode 160</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3<br><b>Output:</b> Intersected at '8'</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Two pointers `a` and `b`. Traverse `A` then `B`, and `B` then `A`. They will meet at the intersection node or `NULL`.</td>
      <td><b>Edge Cases:</b> <b>No Intersection:</b> If no intersection, both pointers will simultaneously hit `NULL` at the end of their second traversal.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getIntersectionNode(headA: ListNode, headB: ListNode) -&gt; ListNode:&#10;    a, b = headA, headB&#10;    while a != b:&#10;        a = a.next if a else headB&#10;        b = b.next if b else headA&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Ll 02 Reverse Nodes In K Group<br><br></b> <a href="https://leetcode.com/problems/reverse-nodes-in-k-group/" target="_blank">LeetCode 25</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], k = 2<br><b>Output:</b> [2,1,4,3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Find length of list. Traverse groups of size k. For each group, perform standard linked list reversal. Link the prev group's tail to the current reversed head.</td>
      <td><b>Edge Cases:</b> <b>Remaining nodes < K:</b> The loop terminates early, leaving the remaining list intact.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    cur, pre, count = head, dummy, 0&#10;    while cur: &#10;        count += 1; cur = cur.next&#10;    while count &gt;= k:&#10;        cur = pre.next&#10;        nex = cur.next&#10;        for _ in range(1, k):&#10;            cur.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = cur.next&#10;        pre = cur&#10;        count -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
  </tbody>
</table>
