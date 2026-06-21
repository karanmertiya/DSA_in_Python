# Linked Lists Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 30%;">Example & Constraints</th>
      <th style="width: 15%;">Complexity</th>
      <th style="width: 35%;">Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Ll 01 Reverse Linked List<br><br></b> <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">LeetCode 206</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5]<br><b>Output:</b> [5,4,3,2,1]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Iterative approach: Maintain three pointers (`prev`, `curr`, `next_node`). Re-point `curr->next` to `prev` and slide forward.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_list(head: ListNode) -&gt; ListNode:&#10;    prev = None&#10;    curr = head&#10;    while curr:&#10;        next_node = curr.next&#10;        curr.next = prev&#10;        prev = curr&#10;        curr = next_node&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Ll 02 Middle Of The Linked List<br><br></b> <a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank">LeetCode 876</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5,6]<br><b>Output:</b> [4,5,6]</td>
      <td><b>Time:</b> O(N/2) &cong; O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). When fast reaches the end, slow is exactly at the middle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def middle_node(head: ListNode) -&gt; ListNode:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Ll 03 Linked List Cycle<br><br></b> <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">LeetCode 141</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [3,2,0,-4], pos = 1<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Tortoise and Hare algorithm. If there is a cycle, the fast pointer will eventually "lap" and collide with the slow pointer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_cycle(head: ListNode) -&gt; bool:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Ll 04 Merge Two Sorted Lists<br><br></b> <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">LeetCode 21</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> list1 = [1,2,4], list2 = [1,3,4]<br><b>Output:</b> [1,1,2,3,4,4]</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Use a dummy node to easily handle the head of the new list. Compare `list1` and `list2`, attaching the smaller node to `tail`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeTwoLists(list1: ListNode, list2: ListNode) -&gt; ListNode:&#10;    dummy = tail = ListNode()&#10;    while list1 and list2:&#10;        if list1.val &lt; list2.val:&#10;            tail.next = list1&#10;            list1 = list1.next&#10;        else:&#10;            tail.next = list2&#10;            list2 = list2.next&#10;        tail = tail.next&#10;    tail.next = list1 or list2&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Ll 05 Remove Nth Node From End Of List<br><br></b> <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">LeetCode 19</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], n = 2<br><b>Output:</b> [1,2,3,5]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Two-pointer approach. Move `fast` pointer `n` steps ahead. Then move both `slow` and `fast` until `fast` reaches the end. `slow` will be right before the target node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeNthFromEnd(head: ListNode, n: int) -&gt; ListNode:&#10;    fast = slow = head&#10;    for _ in range(n):&#10;        fast = fast.next&#10;    if not fast: return head.next&#10;    while fast.next:&#10;        fast = fast.next&#10;        slow = slow.next&#10;    slow.next = slow.next.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Ll 06 Add Two Numbers<br><br></b> <a href="https://leetcode.com/problems/add-two-numbers/" target="_blank">LeetCode 2</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> l1 = [2,4,3], l2 = [5,6,4]<br><b>Output:</b> [7,0,8]</td>
      <td><b>Time:</b> O(max(N, M))<br><b>Space:</b> O(max(N, M))</td>
      <td><b>Explanation:</b> Iterate through both lists, keeping a `carry`. Create new nodes for the `sum % 10`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: ListNode, l2: ListNode) -&gt; ListNode:&#10;    dummy = temp = ListNode()&#10;    carry = 0&#10;    while l1 or l2 or carry:&#10;        s = carry&#10;        if l1: s += l1.val; l1 = l1.next&#10;        if l2: s += l2.val; l2 = l2.next&#10;        carry = s // 10&#10;        temp.next = ListNode(s % 10)&#10;        temp = temp.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Ll 07 Intersection Of Two Linked Lists<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-linked-lists/" target="_blank">LeetCode 160</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Apna College, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3<br><b>Output:</b> Intersected at '8'</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two pointers `a` and `b`. Traverse `A` then `B`, and `B` then `A`. They will meet at the intersection node or `NULL`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getIntersectionNode(headA: ListNode, headB: ListNode) -&gt; ListNode:&#10;    a, b = headA, headB&#10;    while a != b:&#10;        a = a.next if a else headB&#10;        b = b.next if b else headA&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Ll 08 Reverse Nodes In K Group<br><br></b> <a href="https://leetcode.com/problems/reverse-nodes-in-k-group/" target="_blank">LeetCode 25</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Apna College, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], k = 2<br><b>Output:</b> [2,1,4,3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Find length of list. Traverse groups of size k. For each group, perform standard linked list reversal. Link the prev group's tail to the current reversed head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    cur, pre, count = head, dummy, 0&#10;    while cur: &#10;        count += 1; cur = cur.next&#10;    while count &gt;= k:&#10;        cur = pre.next&#10;        nex = cur.next&#10;        for _ in range(1, k):&#10;            cur.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = cur.next&#10;        pre = cur&#10;        count -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Ll 09 Copy List With Random Pointer<br><br></b> <a href="https://leetcode.com/problems/copy-list-with-random-pointer/" target="_blank">LeetCode 138</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Return a deep copy.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> 3 Steps O(1) space. 1) Insert copy nodes right after original nodes. 2) Set random pointers for copy nodes: `iter->next->random = iter->random ? iter->random->next : NULL`. 3) Separate the two lists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def copyRandomList(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    iter_node = head&#10;    while iter_node:&#10;        copy = Node(iter_node.val)&#10;        copy.next = iter_node.next&#10;        iter_node.next = copy&#10;        iter_node = copy.next&#10;    iter_node = head&#10;    while iter_node:&#10;        if iter_node.random: iter_node.next.random = iter_node.random.next&#10;        iter_node = iter_node.next.next&#10;    iter_node = head&#10;    pseudoHead = Node(0)&#10;    copyIter = pseudoHead&#10;    while iter_node:&#10;        nextIter = iter_node.next.next&#10;        copyIter.next = iter_node.next&#10;        iter_node.next = nextIter&#10;        copyIter = copyIter.next&#10;        iter_node = nextIter&#10;    return pseudoHead.next</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Ll 10 Rotate List<br><br></b> <a href="https://leetcode.com/problems/rotate-list/" target="_blank">LeetCode 61</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], k = 2<br><b>Output:</b> [4,5,1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compute the length of the list, and make it a circular list by connecting the last node to head. Then find the new break point `(length - k % length)`. Break the circle and return the new head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateRight(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or not head.next or k == 0: return head&#10;    length = 1&#10;    cur = head&#10;    while cur.next:&#10;        length += 1&#10;        cur = cur.next&#10;    cur.next = head&#10;    k = k % length&#10;    k = length - k&#10;    for _ in range(k): cur = cur.next&#10;    head = cur.next&#10;    cur.next = None&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Ll 11 Flattening A Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Recursively merge.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursively flatten the `next` list, then merge the current list (`bottom` pointers) with the flattened `next` list, similar to merging two sorted linked lists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root):&#10;    def mergeTwoLists(a, b):&#10;        temp = Node(0)&#10;        res = temp&#10;        while a and b:&#10;            if a.data &lt; b.data:&#10;                temp.bottom = a; temp = temp.bottom; a = a.bottom&#10;            else:&#10;                temp.bottom = b; temp = temp.bottom; b = b.bottom&#10;        if a: temp.bottom = a&#10;        else: temp.bottom = b&#10;        return res.bottom&#10;    if not root or not root.next: return root&#10;    root.next = flatten(root.next)&#10;    root = mergeTwoLists(root, root.next)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ll 12 Sort A Linked List<br><br></b> <a href="https://leetcode.com/problems/sort-list/" target="_blank">LeetCode 148</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [4,2,1,3]<br><b>Output:</b> [1,2,3,4]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(log N)</td>
      <td><b>Explanation:</b> Merge Sort. Use fast/slow pointers to find the middle of the linked list. Split into two halves, recursively sort both halves, then merge the two sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    def mergeTwoLists(list1, list2):&#10;        dummy = ListNode(0)&#10;        tail = dummy&#10;        while list1 and list2:&#10;            if list1.val &lt; list2.val:&#10;                tail.next = list1; list1 = list1.next&#10;            else:&#10;                tail.next = list2; list2 = list2.next&#10;            tail = tail.next&#10;        tail.next = list1 if list1 else list2&#10;        return dummy.next&#10;    if not head or not head.next: return head&#10;    slow, fast = head, head.next&#10;    while fast and fast.next:&#10;        slow = slow.next; fast = fast.next.next&#10;    mid = slow.next&#10;    slow.next = None&#10;    return mergeTwoLists(sortList(head), sortList(mid))</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Ll 13 Find Pairs With Given Sum In Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Two pointer approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since it is a sorted DLL, set one pointer at the head and one at the tail. If sum == x, add to result and move both. If sum < x, move left pointer next. Else, move right pointer prev.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPairsWithGivenSum(head, target):&#10;    ans = []&#10;    if not head: return ans&#10;    left = head&#10;    right = head&#10;    while right.next: right = right.next&#10;    while left and right and left.data &lt; right.data:&#10;        if left.data + right.data == target:&#10;            ans.append((left.data, right.data))&#10;            left = left.next&#10;            right = right.prev&#10;        elif left.data + right.data &lt; target:&#10;            left = left.next&#10;        else:&#10;            right = right.prev&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Ll 14 Remove Duplicates From Sorted Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Skip duplicates.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the DLL. While `next` node has the same value, bypass it by updating `curr->next` and `curr->next->prev`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(head):&#10;    curr = head&#10;    while curr:&#10;        nextNode = curr.next&#10;        while nextNode and nextNode.data == curr.data:&#10;            nextNode = nextNode.next&#10;        curr.next = nextNode&#10;        if nextNode:&#10;            nextNode.prev = curr&#10;        curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Ll 15 Reverse A Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Swap prev and next.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the DLL. For each node, swap its `prev` and `next` pointers. The new head will be the last node processed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseDLL(head):&#10;    if not head or not head.next: return head&#10;    curr = head&#10;    temp = None&#10;    while curr:&#10;        temp = curr.prev&#10;        curr.prev = curr.next&#10;        curr.next = temp&#10;        curr = curr.prev&#10;    return temp.prev</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Ll 16 Delete All Occurrences Of A Key In Dll<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Update links.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the list. If `node->data == x`, update the `next` pointer of `node->prev` and `prev` pointer of `node->next`. If the node is head, update head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteAllOccurOfX(head, x):&#10;    curr = head&#10;    while curr:&#10;        if curr.data == x:&#10;            if curr == head: head = curr.next&#10;            if curr.prev: curr.prev.next = curr.next&#10;            if curr.next: curr.next.prev = curr.prev&#10;            curr = curr.next&#10;        else:&#10;            curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Ll 17 Swap Nodes In Pairs<br><br></b> <a href="https://leetcode.com/problems/swap-nodes-in-pairs/" target="_blank">LeetCode 24</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4]<br><b>Output:</b> [2,1,4,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a dummy node. Iteratively swap `curr` and `curr->next`. Keep track of `prev` to link the swapped pairs to the rest of the list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapPairs(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    prev = dummy&#10;    while prev.next and prev.next.next:&#10;        first = prev.next&#10;        second = prev.next.next&#10;        first.next = second.next&#10;        second.next = first&#10;        prev.next = second&#10;        prev = first&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Ll 18 Odd Even Linked List<br><br></b> <a href="https://leetcode.com/problems/odd-even-linked-list/" target="_blank">LeetCode 328</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5]<br><b>Output:</b> [1,3,5,2,4]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Maintain two pointers `odd` and `even`. Keep the `evenHead`. Loop to link `odd->next = even->next` and `even->next = odd->next`. Finally, link `odd->next = evenHead`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def oddEvenList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    if not head or not head.next: return head&#10;    odd, even, evenHead = head, head.next, head.next&#10;    while even and even.next:&#10;        odd.next = odd.next.next&#10;        even.next = even.next.next&#10;        odd = odd.next&#10;        even = even.next&#10;    odd.next = evenHead&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Ll 19 Split Linked List In Parts<br><br></b> <a href="https://leetcode.com/problems/split-linked-list-in-parts/" target="_blank">LeetCode 725</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Distribution math.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> First, calculate the length of the list. Then, determine base size `len / k` and extra nodes `len % k`. Iterate through the list, breaking it into parts of appropriate sizes.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitListToParts(head: Optional[ListNode], k: int) -&gt; List[Optional[ListNode]]:&#10;    length = 0&#10;    curr = head&#10;    while curr:&#10;        length += 1&#10;        curr = curr.next&#10;    partSize, extra = length // k, length % k&#10;    ans = []&#10;    curr = head&#10;    for i in range(k):&#10;        ans.append(curr)&#10;        currentPartSize = partSize + (1 if extra &gt; 0 else 0)&#10;        extra -= 1&#10;        for _ in range(currentPartSize - 1):&#10;            if curr: curr = curr.next&#10;        if curr:&#10;            nextPart = curr.next&#10;            curr.next = None&#10;            curr = nextPart&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Ll 20 Add Two Numbers II<br><br></b> <a href="https://leetcode.com/problems/add-two-numbers-ii/" target="_blank">LeetCode 445</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Stack or reverse.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td><b>Explanation:</b> Use two stacks to store the digits of the lists. Pop from stacks, add along with carry, and construct the new list by inserting at the head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    s1, s2 = [], []&#10;    while l1:&#10;        s1.append(l1.val)&#10;        l1 = l1.next&#10;    while l2:&#10;        s2.append(l2.val)&#10;        l2 = l2.next&#10;    carry = 0&#10;    head = None&#10;    while s1 or s2 or carry:&#10;        sum_val = carry&#10;        if s1: sum_val += s1.pop()&#10;        if s2: sum_val += s2.pop()&#10;        node = ListNode(sum_val % 10)&#10;        node.next = head&#10;        head = node&#10;        carry = sum_val // 10&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Ll 21 Insertion Sort List<br><br></b> <a href="https://leetcode.com/problems/insertion-sort-list/" target="_blank">LeetCode 147</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Dummy head.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a dummy head for the sorted part. For each node in the original list, iterate through the sorted part to find its correct position and insert it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertionSortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    curr = head&#10;    while curr:&#10;        prev = dummy&#10;        while prev.next and prev.next.val &lt;= curr.val:&#10;            prev = prev.next&#10;        nxt = curr.next&#10;        curr.next = prev.next&#10;        prev.next = curr&#10;        curr = nxt&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Ll 22 Partition List<br><br></b> <a href="https://leetcode.com/problems/partition-list/" target="_blank">LeetCode 86</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Two lists then join.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Maintain two separate linked lists: `before` and `after` with their own dummy heads. Iterate through original list, appending to `before` or `after` based on value. Then link `before` tail to `after` head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(head: Optional[ListNode], x: int) -&gt; Optional[ListNode]:&#10;    before_head = ListNode(0)&#10;    before = before_head&#10;    after_head = ListNode(0)&#10;    after = after_head&#10;    while head:&#10;        if head.val &lt; x:&#10;            before.next = head&#10;            before = before.next&#10;        else:&#10;            after.next = head&#10;            after = after.next&#10;        head = head.next&#10;    after.next = None&#10;    before.next = after_head.next&#10;    return before_head.next</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Ll 23 Reverse Nodes In Even Length Groups<br><br></b> <a href="https://leetcode.com/problems/reverse-nodes-in-even-length-groups/" target="_blank">LeetCode 2074</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Group tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the list while tracking the expected group length. First, count the actual number of nodes left in the current group. If the count is even, reverse this sublist and connect it to the previous part. If odd, just skip. Update lengths and pointers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseEvenLengthGroups(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    groupLen = 1&#10;    prev, curr = None, head&#10;    while curr:&#10;        temp, count = curr, 0&#10;        while count &lt; groupLen and temp:&#10;            temp = temp.next&#10;            count += 1&#10;        if count % 2 == 0:&#10;            gPrev, gCurr = None, curr&#10;            for _ in range(count):&#10;                nxt = gCurr.next&#10;                gCurr.next = gPrev&#10;                gPrev = gCurr&#10;                gCurr = nxt&#10;            prev.next = gPrev&#10;            curr.next = gCurr&#10;            prev = curr&#10;            curr = gCurr&#10;        else:&#10;            for _ in range(count):&#10;                prev = curr&#10;                curr = curr.next&#10;        groupLen += 1&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Ll 24 Swapping Nodes In A Linked List<br><br></b> <a href="https://leetcode.com/problems/swapping-nodes-in-a-linked-list/" target="_blank">LeetCode 1721</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Two passes or three pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers. Move `fast` pointer `k-1` steps. `first_node` is at `fast`. Initialize `slow = head`. Move both `slow` and `fast` to the end. `slow` will be at `second_node`. Swap values.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapNodes(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    fast = head&#10;    for _ in range(k - 1): fast = fast.next&#10;    first_node = fast&#10;    slow = head&#10;    while fast.next:&#10;        slow = slow.next&#10;        fast = fast.next&#10;    first_node.val, slow.val = slow.val, first_node.val&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Ll 25 Merge Nodes In Between Zeros<br><br></b> <a href="https://leetcode.com/problems/merge-nodes-in-between-zeros/" target="_blank">LeetCode 2181</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Accumulate and connect.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) extra space if we modify in-place</td>
      <td><b>Explanation:</b> Maintain a dummy node. Traverse the list. Maintain a running sum. When we encounter a 0 (and sum > 0), create a new node with `sum`, attach it to dummy list, reset `sum` to 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeNodes(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = currDummy = ListNode(0)&#10;    curr = head.next&#10;    current_sum = 0&#10;    while curr:&#10;        if curr.val == 0:&#10;            currDummy.next = ListNode(current_sum)&#10;            currDummy = currDummy.next&#10;            current_sum = 0&#10;        else:&#10;            current_sum += curr.val&#10;        curr = curr.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Ll 26 Design Hashmap<br><br></b> <a href="https://leetcode.com/problems/design-hashmap/" target="_blank">LeetCode 706</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Array of Linked Lists with Key-Value pairs.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(Number of elements)</td>
      <td><b>Explanation:</b> Similar to HashSet, but each node stores a `(key, value)` pair. On Put, if key exists, update value. Else insert new node. On Get, return value if key found, else -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class ListNode:&#10;    def __init__(self, key, val):&#10;        self.key, self.val = key, val&#10;        self.next = None&#10;class MyHashMap:&#10;    def __init__(self):&#10;        self.size = 10007&#10;        self.buckets = [None] * self.size&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        while curr:&#10;            if curr.key == key:&#10;                curr.val = value&#10;                return&#10;            curr = curr.next&#10;        newNode = ListNode(key, value)&#10;        newNode.next = self.buckets[idx]&#10;        self.buckets[idx] = newNode&#10;    def get(self, key: int) -&gt; int:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        while curr:&#10;            if curr.key == key: return curr.val&#10;            curr = curr.next&#10;        return -1&#10;    def remove(self, key: int) -&gt; None:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        prev = None&#10;        while curr:&#10;            if curr.key == key:&#10;                if prev: prev.next = curr.next&#10;                else: self.buckets[idx] = curr.next&#10;                return&#10;            prev = curr&#10;            curr = curr.next</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Ll 27 Design Browser History<br><br></b> <a href="https://leetcode.com/problems/design-browser-history/" target="_blank">LeetCode 1472</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Doubly Linked List.</td>
      <td><b>Time:</b> O(1) visit, O(steps) back/forward<br><b>Space:</b> O(N) for URLs</td>
      <td><b>Explanation:</b> Use a Doubly Linked List. Each visit creates a new node, clearing forward history. Back and forward operations just traverse the pointers up to `steps` times.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, url):&#10;        self.url = url&#10;        self.prev = self.next = None&#10;class BrowserHistory:&#10;    def __init__(self, homepage: str):&#10;        self.curr = Node(homepage)&#10;    def visit(self, url: str) -&gt; None:&#10;        newNode = Node(url)&#10;        self.curr.next = newNode&#10;        newNode.prev = self.curr&#10;        self.curr = newNode&#10;    def back(self, steps: int) -&gt; str:&#10;        while steps &gt; 0 and self.curr.prev:&#10;            self.curr = self.curr.prev&#10;            steps -= 1&#10;        return self.curr.url&#10;    def forward(self, steps: int) -&gt; str:&#10;        while steps &gt; 0 and self.curr.next:&#10;            self.curr = self.curr.next&#10;            steps -= 1&#10;        return self.curr.url</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Ll 28 Lru Cache Ll<br><br></b> <a href="https://leetcode.com/problems/lru-cache/" target="_blank">LeetCode 146</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> Duplicate logic entry to ensure coverage.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Included for chapter coverage completeness. See sq_31_lru_cache.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># See Stacks and Queues module for full implementation.</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Ll 29 Lfu Cache Ll<br><br></b> <a href="https://leetcode.com/problems/lfu-cache/" target="_blank">LeetCode 460</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> Duplicate logic entry to ensure coverage.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Included for chapter coverage completeness. See sq_32_lfu_cache.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># See Stacks and Queues module for full implementation.</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Ll 30 All Oone Data Structure<br><br></b> <a href="https://leetcode.com/problems/all-oone-data-structure/" target="_blank">LeetCode 432</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Doubly linked list of frequency buckets.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Maintain a DLL where each node represents a specific frequency and contains a set of strings. Use a hash map mapping strings to their current bucket. On inc/dec, move the string to the adjacent bucket (create if necessary). Max is tail->prev, Min is head->next.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Bucket:&#10;    def __init__(self, count):&#10;        self.count = count&#10;        self.keys = set()&#10;        self.prev = self.next = None&#10;class AllOne:&#10;    def __init__(self):&#10;        self.head, self.tail = Bucket(0), Bucket(0)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;        self.m = {}&#10;    def _add_bucket(self, prev_b, new_b):&#10;        new_b.prev, new_b.next = prev_b, prev_b.next&#10;        prev_b.next.prev = prev_b.next = new_b&#10;    def _remove_bucket(self, b):&#10;        b.prev.next, b.next.prev = b.next, b.prev&#10;    def inc(self, key: str) -&gt; None:&#10;        if key in self.m:&#10;            curr = self.m[key]&#10;            nxt = curr.next&#10;            if nxt == self.tail or nxt.count != curr.count + 1:&#10;                self._add_bucket(curr, Bucket(curr.count + 1))&#10;                nxt = curr.next&#10;            nxt.keys.add(key)&#10;            self.m[key] = nxt&#10;            curr.keys.remove(key)&#10;            if not curr.keys: self._remove_bucket(curr)&#10;        else:&#10;            nxt = self.head.next&#10;            if nxt == self.tail or nxt.count != 1:&#10;                self._add_bucket(self.head, Bucket(1))&#10;                nxt = self.head.next&#10;            nxt.keys.add(key)&#10;            self.m[key] = nxt&#10;    def dec(self, key: str) -&gt; None:&#10;        curr = self.m[key]&#10;        if curr.count == 1:&#10;            del self.m[key]&#10;        else:&#10;            prv = curr.prev&#10;            if prv == self.head or prv.count != curr.count - 1:&#10;                self._add_bucket(curr.prev, Bucket(curr.count - 1))&#10;                prv = curr.prev&#10;            prv.keys.add(key)&#10;            self.m[key] = prv&#10;        curr.keys.remove(key)&#10;        if not curr.keys: self._remove_bucket(curr)&#10;    def getMaxKey(self) -&gt; str:&#10;        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else &quot;&quot;&#10;    def getMinKey(self) -&gt; str:&#10;        return next(iter(self.head.next.keys)) if self.head.next != self.tail else &quot;&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Ll 31 Flatten A Multilevel Doubly Linked List<br><br></b> <a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/" target="_blank">LeetCode 430</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> DFS / Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the list. When a node has a child, find the tail of the child list. Connect the tail to `node->next`, and `node->next` to the child. Update `prev` pointers. Set `node->child` to `nullptr`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    curr = head&#10;    while curr:&#10;        if curr.child:&#10;            tail = curr.child&#10;            while tail.next: tail = tail.next&#10;            tail.next = curr.next&#10;            if curr.next: curr.next.prev = tail&#10;            curr.next = curr.child&#10;            curr.child.prev = curr&#10;            curr.child = None&#10;        curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Ll 32 Multiply Two Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Traverse and compute numbers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the first linked list and compute the number it represents modulo 10^9+7. Do the same for the second linked list. Multiply the two numbers and return the result modulo 10^9+7.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def multiplyTwoLists(head1: Node, head2: Node) -&gt; int:&#10;    num1 = num2 = 0&#10;    mod = 10**9 + 7&#10;    while head1:&#10;        num1 = (num1 * 10 + head1.data) % mod&#10;        head1 = head1.next&#10;    while head2:&#10;        num2 = (num2 * 10 + head2.data) % mod&#10;        head2 = head2.next&#10;    return (num1 * num2) % mod</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Ll 33 Delete Nodes Having Greater Value On Right<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Reverse, filter, reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Reverse the linked list. Traverse the reversed list and keep track of the maximum value seen so far. If a node's value is less than the maximum, delete it. Otherwise, update the maximum. Finally, reverse the list again.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def compute(head: Node) -&gt; Node:&#10;    def reverseList(node):&#10;        prev, curr = None, node&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    head = reverseList(head)&#10;    curr = head&#10;    max_val = head.data&#10;    while curr and curr.next:&#10;        if curr.next.data &lt; max_val:&#10;            curr.next = curr.next.next&#10;        else:&#10;            curr = curr.next&#10;            max_val = curr.data&#10;    return reverseList(head)</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Ll 34 Segregate Even And Odd Nodes In A Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two pointers for even and odd.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Create two dummy nodes, one for the even list and one for the odd list. Traverse the original list and append even nodes to the even list and odd nodes to the odd list. Finally, connect the end of the even list to the head of the odd list and terminate the odd list with NULL.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def divide(N: int, head: Node) -&gt; Node:&#10;    evenStart = evenEnd = None&#10;    oddStart = oddEnd = None&#10;    curr = head&#10;    while curr:&#10;        val = curr.data&#10;        if val % 2 == 0:&#10;            if not evenStart:&#10;                evenStart = evenEnd = curr&#10;            else:&#10;                evenEnd.next = curr&#10;                evenEnd = evenEnd.next&#10;        else:&#10;            if not oddStart:&#10;                oddStart = oddEnd = curr&#10;            else:&#10;                oddEnd.next = curr&#10;                oddEnd = oddEnd.next&#10;        curr = curr.next&#10;    if not oddStart or not evenStart: return head&#10;    evenEnd.next = oddStart&#10;    oddEnd.next = None&#10;    return evenStart</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Ll 35 Nth Node From End Of Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers, `fast` and `slow`. Move `fast` `N` steps ahead. If `fast` becomes NULL before `N` steps, return -1 (N > length). Then move both `fast` and `slow` one step at a time until `fast` reaches the end. `slow` will be pointing to the Nth node from the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getNthFromLast(head: Node, n: int) -&gt; int:&#10;    fast, slow = head, head&#10;    for _ in range(n):&#10;        if not fast: return -1&#10;        fast = fast.next&#10;    while fast:&#10;        slow = slow.next&#10;        fast = fast.next&#10;    return slow.data</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Ll 36 First Non Repeating Character In A Stream<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Queue and frequency array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a queue to maintain the order of characters and an array to keep track of their frequencies. For each character, increment its frequency and push it to the queue. Then, while the queue is not empty and the frequency of the front character is greater than 1, pop it. If the queue is empty, append '#', else append the front character.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def FirstNonRepeating(A: str) -&gt; str:&#10;    freq = [0] * 26&#10;    q = collections.deque()&#10;    res = []&#10;    for c in A:&#10;        freq[ord(c) - ord(&#x27;a&#x27;)] += 1&#10;        q.append(c)&#10;        while q and freq[ord(q[0]) - ord(&#x27;a&#x27;)] &gt; 1:&#10;            q.popleft()&#10;        if not q: res.append(&#x27;#&#x27;)&#10;        else: res.append(q[0])&#10;    return &quot;&quot;.join(res)</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Ll 37 Clone A Linked List With Next And Random Pointer<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Interleaving lists.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Create a copy of each node and insert it immediately after the original node. Then, set the random pointers for the copied nodes (`curr->next->arb = curr->arb ? curr->arb->next : NULL`). Finally, separate the original and copied lists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def copyList(head: Node) -&gt; Node:&#10;    if not head: return None&#10;    curr = head&#10;    while curr:&#10;        temp = Node(curr.data)&#10;        temp.next = curr.next&#10;        curr.next = temp&#10;        curr = temp.next&#10;    curr = head&#10;    while curr:&#10;        if curr.arb:&#10;            curr.next.arb = curr.arb.next&#10;        curr = curr.next.next&#10;    curr = head&#10;    copyHead = head.next&#10;    copyCurr = copyHead&#10;    while curr:&#10;        curr.next = curr.next.next&#10;        if copyCurr.next:&#10;            copyCurr.next = copyCurr.next.next&#10;        curr = curr.next&#10;        copyCurr = copyCurr.next&#10;    return copyHead</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Ll 38 Merge K Sorted Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N * K * log K)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Create a min-heap and push the head of each linked list into it. Pop the minimum element, append it to the result list, and if the popped node has a next node, push the next node into the heap. Continue until the heap is empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKLists(arr: List[Node], K: int) -&gt; Node:&#10;    pq = []&#10;    for i in range(K):&#10;        if arr[i]:&#10;            heapq.heappush(pq, (arr[i].data, i, arr[i]))&#10;    dummy = Node(0)&#10;    tail = dummy&#10;    while pq:&#10;        val, idx, curr = heapq.heappop(pq)&#10;        tail.next = curr&#10;        tail = tail.next&#10;        if curr.next:&#10;            heapq.heappush(pq, (curr.next.data, idx, curr.next))&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Ll 39 Reverse A Linked List In Groups Of Given Size<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> Recursive grouping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N/K)</td>
      <td><b>Explanation:</b> Reverse the first `k` nodes of the linked list iteratively. After reversing, the `head` pointer will be the end of the reversed group, and `curr` will point to the next node. Recursively call the function for `curr` and set `head->next` to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(head: Node, k: int) -&gt; Node:&#10;    if not head: return None&#10;    curr, prev, nxt = head, None, None&#10;    count = 0&#10;    while curr and count &lt; k:&#10;        nxt = curr.next&#10;        curr.next = prev&#10;        prev = curr&#10;        curr = nxt&#10;        count += 1&#10;    if nxt:&#10;        head.next = reverse(nxt, k)&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Ll 40 Split A Circular Linked List Into Two Halves<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Slow and Fast Pointer.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use slow and fast pointers to find the mid of the circular linked list. The slow pointer will point to the mid. Then break the list into two and make both circular.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitList(head, head1, head2):&#10;    if head is None: return&#10;    slow, fast = head, head&#10;    while fast.next != head and fast.next.next != head:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    if fast.next.next == head:&#10;        fast = fast.next&#10;    head1.head = head&#10;    if head.next != head:&#10;        head2.head = slow.next&#10;    fast.next = slow.next&#10;    slow.next = head</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Ll 41 Check If Circular Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/circular-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Traverse to head.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the linked list starting from head. If we reach NULL, it's not circular. If we reach head again, it is circular.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isCircular(head):&#10;    if head is None: return True&#10;    temp = head.next&#10;    while temp is not None and temp != head:&#10;        temp = temp.next&#10;    return temp == head</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Ll 42 Count Triplets In A Sorted Doubly Linked List Whose Sum Is Equal To Given Value X<br><br></b> <a href="https://www.geeksforgeeks.org/count-triplets-sorted-doubly-linked-list-whose-sum-equal-given-value-x/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the list. For each node, use two pointers (left and right) on the remaining list to find pairs that sum to `x - node.data`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countTriplets(head, x):&#10;    if head is None: return 0&#10;    last = head&#10;    while last.next: last = last.next&#10;    count = 0&#10;    curr = head&#10;    while curr:&#10;        first = curr.next&#10;        right = last&#10;        while first and right and first != right and right.next != first:&#10;            total = curr.data + first.data + right.data&#10;            if total == x:&#10;                count += 1&#10;                first = first.next&#10;                right = right.prev&#10;            elif total &lt; x:&#10;                first = first.next&#10;            else:&#10;                right = right.prev&#10;        curr = curr.next&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Ll 43 Sort A K Sorted Doubly Linked List<br><br></b> <a href="https://www.geeksforgeeks.org/sort-k-sorted-doubly-linked-list/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Create a Min Heap of size k+1. Insert the first k+1 elements into the heap. Then, pop the minimum element, place it in the sorted list, and push the next element from the original list into the heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def sortAKSortedDLL(head, k):&#10;    if not head: return head&#10;    pq = []&#10;    newHead, last = None, None&#10;    i = 0&#10;    while head and i &lt;= k:&#10;        heapq.heappush(pq, (head.data, id(head), head))&#10;        head = head.next&#10;        i += 1&#10;    while pq:&#10;        _, _, minNode = heapq.heappop(pq)&#10;        if not newHead:&#10;            newHead = minNode&#10;            newHead.prev = None&#10;            last = newHead&#10;        else:&#10;            last.next = minNode&#10;            minNode.prev = last&#10;            last = minNode&#10;        if head:&#10;            heapq.heappush(pq, (head.data, id(head), head))&#10;            head = head.next&#10;    last.next = None&#10;    return newHead</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Ll 44 Rotate Doubly Linked List By N Nodes<br><br></b> <a href="https://www.geeksforgeeks.org/rotate-doubly-linked-list-n-nodes/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Traverse and link.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse to the Nth node. This will be the new tail. Its next will be the new head. Traverse to the end of the list and link it to the original head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateDLL(start, N):&#10;    if N == 0: return start&#10;    current = start&#10;    count = 1&#10;    while count &lt; N and current:&#10;        current = current.next&#10;        count += 1&#10;    if not current: return start&#10;    nthNode = current&#10;    while current.next:&#10;        current = current.next&#10;    current.next = start&#10;    start.prev = current&#10;    start = nthNode.next&#10;    start.prev = None&#10;    nthNode.next = None&#10;    return start</code></pre></details></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Ll 45 Reverse A Doubly Linked List In Groups Of Given Size<br><br></b> <a href="https://www.geeksforgeeks.org/reverse-doubly-linked-list-groups-given-size/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N/K) recursion stack</td>
      <td><b>Explanation:</b> Similar to reversing singly linked list in groups of k. Keep track of prev, next, and current. Reverse k nodes, then recursively call for the rest of the list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def revListInGroupOfGivenSize(head, k):&#10;    if not head: return None&#10;    current = head&#10;    next_node = None&#10;    new_head = None&#10;    count = 0&#10;    while current and count &lt; k:&#10;        next_node = current.next&#10;        current.prev = next_node&#10;        current.next = new_head&#10;        if new_head:&#10;            new_head.prev = current&#10;        new_head = current&#10;        current = next_node&#10;        count += 1&#10;    if next_node:&#10;        head.next = revListInGroupOfGivenSize(next_node, k)&#10;        head.next.prev = head&#10;    return new_head</code></pre></details></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Ll 46 Can We Reverse A Linked List In Less Than On<br><br></b> N/A<br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Theoretical Question.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> No, it is not possible. To reverse a linked list, we must visit every single node at least once to change its pointer. Therefore, the minimum time complexity required is strictly O(N), where N is the number of nodes in the linked list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># It is not possible to reverse in less than O(n).</code></pre></details></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Ll 47 Find The First Node Of Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Floyd's Cycle Detection.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Floyd's Cycle Detection to find if a cycle exists (slow and fast pointers meet). Then, move slow back to head, and advance both slow and fast by one step until they meet. The meeting point is the start of the loop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findFirstNode(head):&#10;    slow = head&#10;    fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast:&#10;            slow = head&#10;            while slow != fast:&#10;                slow = slow.next&#10;                fast = fast.next&#10;            return slow.data&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Ll 48 Detect Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Floyd's Cycle Detection.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Floyd's Cycle Detection algorithm (Tortoise and Hare). Move `slow` by 1 and `fast` by 2. If they meet, a loop exists. If `fast` reaches NULL, there is no loop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def detectLoop(head):&#10;    slow = fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>49</td>
      <td>Ll 49 Remove Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Floyd's Cycle Detection + Loop removal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Floyd's Cycle Detection. If a loop is found, reset `slow` to head. Move both `slow` and `fast` by 1. The node where they meet is the start of the loop. Keep track of `fast`'s previous node to set its `next` to NULL.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeLoop(head):&#10;    if not head or not head.next: return&#10;    slow = fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: break&#10;    if slow == fast:&#10;        slow = head&#10;        if slow == fast:&#10;            while fast.next != slow: fast = fast.next&#10;        else:&#10;            while slow.next != fast.next:&#10;                slow = slow.next&#10;                fast = fast.next&#10;        fast.next = None</code></pre></details></td>
    </tr>
    <tr>
      <td>50</td>
      <td>Ll 50 Remove Duplicates From An Unsorted Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Hash set.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a hash set to store the seen values. Iterate the list. If a node's value is in the set, skip it by updating the `next` pointer of the `prev` node. Else, add it to the set and update `prev`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(head):&#10;    if not head: return None&#10;    seen = set()&#10;    curr, prev = head, None&#10;    while curr:&#10;        if curr.data in seen:&#10;            prev.next = curr.next&#10;            curr = prev.next&#10;        else:&#10;            seen.add(curr.data)&#10;            prev = curr&#10;            curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td>51</td>
      <td>Ll 51 Move Last Element To Front Of A Given Linked List<br><br></b> <a href="https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse the list to find the last node (`tail`) and the second last node (`sec_last`). Make `sec_last->next = NULL`, `tail->next = head`, and update `head = tail`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveToFront(head):&#10;    if not head or not head.next: return head&#10;    sec_last = None&#10;    tail = head&#10;    while tail.next:&#10;        sec_last = tail&#10;        tail = tail.next&#10;    sec_last.next = None&#10;    tail.next = head&#10;    return tail</code></pre></details></td>
    </tr>
    <tr>
      <td>52</td>
      <td>Ll 52 Add 1 To A Number Represented As Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Reverse, Add, Reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Reverse the linked list. Add 1 to the first node, and propagate the carry if the value becomes 10. Once done, reverse the list back. If carry still remains at the end, add a new node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOne(head):&#10;    def reverse(node):&#10;        curr, prev, nxt = node, None, None&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    head = reverse(head)&#10;    curr, prev = head, None&#10;    carry = 1&#10;    while curr:&#10;        total = curr.data + carry&#10;        carry = total // 10&#10;        curr.data = total % 10&#10;        prev = curr&#10;        curr = curr.next&#10;    if carry &gt; 0:&#10;        prev.next = Node(carry)&#10;    return reverse(head)</code></pre></details></td>
    </tr>
    <tr>
      <td>53</td>
      <td>Ll 53 Add Two Numbers Represented By Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Reverse, Add, Reverse.</td>
      <td><b>Time:</b> O(max(N, M))<br><b>Space:</b> O(max(N, M))</td>
      <td><b>Explanation:</b> Reverse both linked lists. Traverse both lists simultaneously, adding the data values of corresponding nodes along with the carry. Create new nodes for the sum and append them to the result list. Finally, reverse the result list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoLists(first, second):&#10;    def reverse(node):&#10;        curr, prev, nxt = node, None, None&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    first = reverse(first)&#10;    second = reverse(second)&#10;    dummy = Node(0)&#10;    temp = dummy&#10;    carry = 0&#10;    while first or second or carry:&#10;        total = carry&#10;        if first: total += first.data; first = first.next&#10;        if second: total += second.data; second = second.next&#10;        carry = total // 10&#10;        temp.next = Node(total % 10)&#10;        temp = temp.next&#10;    return reverse(dummy.next)</code></pre></details></td>
    </tr>
    <tr>
      <td>54</td>
      <td>Ll 54 Intersection Of Two Sorted Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td><b>Explanation:</b> Use two pointers, `ptr1` for the first list and `ptr2` for the second. If `ptr1->data < ptr2->data`, `ptr1++`. If `ptr2->data < ptr1->data`, `ptr2++`. If they are equal, add to the result list and advance both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findIntersection(head1, head2):&#10;    dummy = Node(0)&#10;    temp = dummy&#10;    p1, p2 = head1, head2&#10;    while p1 and p2:&#10;        if p1.data &lt; p2.data: p1 = p1.next&#10;        elif p2.data &lt; p1.data: p2 = p2.next&#10;        else:&#10;            temp.next = Node(p1.data)&#10;            temp = temp.next&#10;            p1 = p1.next&#10;            p2 = p2.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td>55</td>
      <td>Ll 55 Intersection Point In Y Shaped Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers `a` and `b`. Traverse both lists. When `a` reaches the end, redirect it to `head2`. When `b` reaches the end, redirect it to `head1`. They will meet at the intersection point or both become NULL.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersectPoint(head1, head2):&#10;    a, b = head1, head2&#10;    while a != b:&#10;        a = a.next if a else head2&#10;        b = b.next if b else head1&#10;    if a: return a.data&#10;    return -1</code></pre></details></td>
    </tr>
  </tbody>
</table>
