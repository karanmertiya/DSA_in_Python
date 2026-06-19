# Linked Lists Revision Table

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
      <td rowspan="1">Ll 01 Reverse Linked List<br><br></b> <a href='https://leetcode.com/problems/reverse-linked-list/' target='_blank'>LeetCode 206</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], Output: [5,4,3,2,1]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Null List:</b> Automatically handled because the `while` loop checks `curr != NULL`.</td>
      <td><b>Explanation:</b> Iterative approach: Maintain three pointers (`prev`, `curr`, `next_node`). Re-point `curr->next` to `prev` and slide forward.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_list(head: ListNode) -&gt; ListNode:&#10;    prev = None&#10;    curr = head&#10;    while curr:&#10;        next_node = curr.next&#10;        curr.next = prev&#10;        prev = curr&#10;        curr = next_node&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Ll 02 Middle Of The Linked List<br><br></b> <a href='https://leetcode.com/problems/middle-of-the-linked-list/' target='_blank'>LeetCode 876</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5,6], Output: [4,5,6]</td>
      <td><b>Time:</b> O(N/2) &cong; O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Even/Odd Length:</b> Loop condition `fast != NULL && fast->next != NULL` handles both.</td>
      <td><b>Explanation:</b> Use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). When fast reaches the end, slow is exactly at the middle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def middle_node(head: ListNode) -&gt; ListNode:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Ll 03 Linked List Cycle<br><br></b> <a href='https://leetcode.com/problems/linked-list-cycle/' target='_blank'>LeetCode 141</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [3,2,0,-4], pos = 1, Output: true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>No Cycle:</b> Handled if `fast == NULL` or `fast->next == NULL`.</td>
      <td><b>Explanation:</b> Tortoise and Hare algorithm. If there is a cycle, the fast pointer will eventually "lap" and collide with the slow pointer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_cycle(head: ListNode) -&gt; bool:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Ll 04 Merge Two Sorted Lists<br><br></b> <a href='https://leetcode.com/problems/merge-two-sorted-lists/' target='_blank'>LeetCode 21</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: list1 = [1,2,4], list2 = [1,3,4], Output: [1,1,2,3,4,4]</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Leftover Nodes:</b> When one list exhausts, directly attach the entirety of the other list via `tail->next = list1 ? list1 : list2`.</td>
      <td><b>Explanation:</b> Use a dummy node to easily handle the head of the new list. Compare `list1` and `list2`, attaching the smaller node to `tail`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeTwoLists(list1: ListNode, list2: ListNode) -&gt; ListNode:&#10;    dummy = tail = ListNode()&#10;    while list1 and list2:&#10;        if list1.val &lt; list2.val:&#10;            tail.next = list1&#10;            list1 = list1.next&#10;        else:&#10;            tail.next = list2&#10;            list2 = list2.next&#10;        tail = tail.next&#10;    tail.next = list1 or list2&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Ll 05 Remove Nth Node From End Of List<br><br></b> <a href='https://leetcode.com/problems/remove-nth-node-from-end-of-list/' target='_blank'>LeetCode 19</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], n = 2, Output: [1,2,3,5]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Remove Head:</b> If `fast` becomes NULL after moving `n` steps, it means the head needs to be removed. Return `head->next`.</td>
      <td><b>Explanation:</b> Two-pointer approach. Move `fast` pointer `n` steps ahead. Then move both `slow` and `fast` until `fast` reaches the end. `slow` will be right before the target node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeNthFromEnd(head: ListNode, n: int) -&gt; ListNode:&#10;    fast = slow = head&#10;    for _ in range(n):&#10;        fast = fast.next&#10;    if not fast: return head.next&#10;    while fast.next:&#10;        fast = fast.next&#10;        slow = slow.next&#10;    slow.next = slow.next.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Ll 06 Add Two Numbers<br><br></b> <a href='https://leetcode.com/problems/add-two-numbers/' target='_blank'>LeetCode 2</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: l1 = [2,4,3], l2 = [5,6,4], Output: [7,0,8]</td>
      <td><b>Time:</b> O(max(N, M))<br><b>Space:</b> O(max(N, M))</td>
      <td>-</td>
      <td><b>Leftover Carry:</b> After the loop, if `carry > 0`, we must append one last node.</td>
      <td><b>Explanation:</b> Iterate through both lists, keeping a `carry`. Create new nodes for the `sum % 10`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: ListNode, l2: ListNode) -&gt; ListNode:&#10;    dummy = temp = ListNode()&#10;    carry = 0&#10;    while l1 or l2 or carry:&#10;        s = carry&#10;        if l1: s += l1.val; l1 = l1.next&#10;        if l2: s += l2.val; l2 = l2.next&#10;        carry = s // 10&#10;        temp.next = ListNode(s % 10)&#10;        temp = temp.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Ll 07 Intersection Of Two Linked Lists<br><br></b> <a href='https://leetcode.com/problems/intersection-of-two-linked-lists/' target='_blank'>LeetCode 160</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3, Output: Intersected at '8'</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>No Intersection:</b> If no intersection, both pointers will simultaneously hit `NULL` at the end of their second traversal.</td>
      <td><b>Explanation:</b> Two pointers `a` and `b`. Traverse `A` then `B`, and `B` then `A`. They will meet at the intersection node or `NULL`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getIntersectionNode(headA: ListNode, headB: ListNode) -&gt; ListNode:&#10;    a, b = headA, headB&#10;    while a != b:&#10;        a = a.next if a else headB&#10;        b = b.next if b else headA&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Ll 08 Reverse Nodes In K Group<br><br></b> <a href='https://leetcode.com/problems/reverse-nodes-in-k-group/' target='_blank'>LeetCode 25</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], k = 2, Output: [2,1,4,3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Remaining nodes < K:</b> The loop terminates early, leaving the remaining list intact.</td>
      <td><b>Explanation:</b> Find length of list. Traverse groups of size k. For each group, perform standard linked list reversal. Link the prev group's tail to the current reversed head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    cur, pre, count = head, dummy, 0&#10;    while cur: &#10;        count += 1; cur = cur.next&#10;    while count &gt;= k:&#10;        cur = pre.next&#10;        nex = cur.next&#10;        for _ in range(1, k):&#10;            cur.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = cur.next&#10;        pre = cur&#10;        count -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Ll 09 Intersection Of Two Linked Lists<br><br></b> <a href='https://leetcode.com/problems/intersection-of-two-linked-lists/' target='_blank'>LeetCode 160</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], Output: Intersected at '8'</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>No intersection:</b> Both pointers will reach NULL simultaneously after swapping lists once.</td>
      <td><b>Explanation:</b> Two pointers. Pointer A traverses list A, then jumps to list B. Pointer B traverses list B, then jumps to list A. They traverse the same total distance (A+B) and will meet at the intersection, or at NULL.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getIntersectionNode(headA: ListNode, headB: ListNode) -&gt; Optional[ListNode]:&#10;    if not headA or not headB: return None&#10;    a, b = headA, headB&#10;    while a != b:&#10;        a = a.next if a else headB&#10;        b = b.next if b else headA&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Ll 10 Reverse Nodes In K Group<br><br></b> <a href='https://leetcode.com/problems/reverse-nodes-in-k-group/' target='_blank'>LeetCode 25</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], k = 2, Output: [2,1,4,3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterative approach. Calculate the length. Use a dummy node. Maintain `pre`, `curr`, and `nex` pointers. Reverse `k-1` links in each group. Decrement length by `k` until length < `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    length, temp = 0, head&#10;    while temp:&#10;        length += 1&#10;        temp = temp.next&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    pre, curr, nex = dummy, dummy, dummy&#10;    while length &gt;= k:&#10;        curr = pre.next&#10;        nex = curr.next&#10;        for _ in range(1, k):&#10;            curr.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = curr.next&#10;        pre = curr&#10;        length -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Ll 11 Copy List With Random Pointer<br><br></b> <a href='https://leetcode.com/problems/copy-list-with-random-pointer/' target='_blank'>LeetCode 138</a></td>
      <td rowspan="1"><b>Example 1:</b> Return a deep copy.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 3 Steps O(1) space. 1) Insert copy nodes right after original nodes. 2) Set random pointers for copy nodes: `iter->next->random = iter->random ? iter->random->next : NULL`. 3) Separate the two lists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def copyRandomList(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    iter_node = head&#10;    while iter_node:&#10;        copy = Node(iter_node.val)&#10;        copy.next = iter_node.next&#10;        iter_node.next = copy&#10;        iter_node = copy.next&#10;    iter_node = head&#10;    while iter_node:&#10;        if iter_node.random: iter_node.next.random = iter_node.random.next&#10;        iter_node = iter_node.next.next&#10;    iter_node = head&#10;    pseudoHead = Node(0)&#10;    copyIter = pseudoHead&#10;    while iter_node:&#10;        nextIter = iter_node.next.next&#10;        copyIter.next = iter_node.next&#10;        iter_node.next = nextIter&#10;        copyIter = copyIter.next&#10;        iter_node = nextIter&#10;    return pseudoHead.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Ll 16 Rotate List<br><br></b> <a href='https://leetcode.com/problems/rotate-list/' target='_blank'>LeetCode 61</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>k = 0 or empty list:</b> Return head immediately.</td>
      <td><b>Explanation:</b> Compute the length of the list, and make it a circular list by connecting the last node to head. Then find the new break point `(length - k % length)`. Break the circle and return the new head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateRight(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or not head.next or k == 0: return head&#10;    length = 1&#10;    cur = head&#10;    while cur.next:&#10;        length += 1&#10;        cur = cur.next&#10;    cur.next = head&#10;    k = k % length&#10;    k = length - k&#10;    for _ in range(k): cur = cur.next&#10;    head = cur.next&#10;    cur.next = None&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Ll 17 Flattening A Linked List<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursively merge.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recursively flatten the `next` list, then merge the current list (`bottom` pointers) with the flattened `next` list, similar to merging two sorted linked lists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root):&#10;    def mergeTwoLists(a, b):&#10;        temp = Node(0)&#10;        res = temp&#10;        while a and b:&#10;            if a.data &lt; b.data:&#10;                temp.bottom = a; temp = temp.bottom; a = a.bottom&#10;            else:&#10;                temp.bottom = b; temp = temp.bottom; b = b.bottom&#10;        if a: temp.bottom = a&#10;        else: temp.bottom = b&#10;        return res.bottom&#10;    if not root or not root.next: return root&#10;    root.next = flatten(root.next)&#10;    root = mergeTwoLists(root, root.next)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Ll 18 Sort A Linked List<br><br></b> <a href='https://leetcode.com/problems/sort-list/' target='_blank'>LeetCode 148</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [4,2,1,3], Output: [1,2,3,4]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(log N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Merge Sort. Use fast/slow pointers to find the middle of the linked list. Split into two halves, recursively sort both halves, then merge the two sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    def mergeTwoLists(list1, list2):&#10;        dummy = ListNode(0)&#10;        tail = dummy&#10;        while list1 and list2:&#10;            if list1.val &lt; list2.val:&#10;                tail.next = list1; list1 = list1.next&#10;            else:&#10;                tail.next = list2; list2 = list2.next&#10;            tail = tail.next&#10;        tail.next = list1 if list1 else list2&#10;        return dummy.next&#10;    if not head or not head.next: return head&#10;    slow, fast = head, head.next&#10;    while fast and fast.next:&#10;        slow = slow.next; fast = fast.next.next&#10;    mid = slow.next&#10;    slow.next = None&#10;    return mergeTwoLists(sortList(head), sortList(mid))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Ll 19 Find Pairs With Given Sum In Doubly Linked List<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointer approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Since it is a sorted DLL, set one pointer at the head and one at the tail. If sum == x, add to result and move both. If sum < x, move left pointer next. Else, move right pointer prev.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPairsWithGivenSum(head, target):&#10;    ans = []&#10;    if not head: return ans&#10;    left = head&#10;    right = head&#10;    while right.next: right = right.next&#10;    while left and right and left.data &lt; right.data:&#10;        if left.data + right.data == target:&#10;            ans.append((left.data, right.data))&#10;            left = left.next&#10;            right = right.prev&#10;        elif left.data + right.data &lt; target:&#10;            left = left.next&#10;        else:&#10;            right = right.prev&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Ll 20 Remove Duplicates From Sorted Doubly Linked List<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Skip duplicates.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse the DLL. While `next` node has the same value, bypass it by updating `curr->next` and `curr->next->prev`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(head):&#10;    curr = head&#10;    while curr:&#10;        nextNode = curr.next&#10;        while nextNode and nextNode.data == curr.data:&#10;            nextNode = nextNode.next&#10;        curr.next = nextNode&#10;        if nextNode:&#10;            nextNode.prev = curr&#10;        curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Ll 21 Reverse A Doubly Linked List<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Swap prev and next.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse the DLL. For each node, swap its `prev` and `next` pointers. The new head will be the last node processed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseDLL(head):&#10;    if not head or not head.next: return head&#10;    curr = head&#10;    temp = None&#10;    while curr:&#10;        temp = curr.prev&#10;        curr.prev = curr.next&#10;        curr.next = temp&#10;        curr = curr.prev&#10;    return temp.prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Ll 22 Delete All Occurrences Of A Key In Dll<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Update links.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Head deletion:</b> handled by reassigning head pointer.</td>
      <td><b>Explanation:</b> Traverse the list. If `node->data == x`, update the `next` pointer of `node->prev` and `prev` pointer of `node->next`. If the node is head, update head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteAllOccurOfX(head, x):&#10;    curr = head&#10;    while curr:&#10;        if curr.data == x:&#10;            if curr == head: head = curr.next&#10;            if curr.prev: curr.prev.next = curr.next&#10;            if curr.next: curr.next.prev = curr.prev&#10;            curr = curr.next&#10;        else:&#10;            curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Ll 23 Swap Nodes In Pairs<br><br></b> <a href='https://leetcode.com/problems/swap-nodes-in-pairs/' target='_blank'>LeetCode 24</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4], Output: [2,1,4,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a dummy node. Iteratively swap `curr` and `curr->next`. Keep track of `prev` to link the swapped pairs to the rest of the list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapPairs(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    prev = dummy&#10;    while prev.next and prev.next.next:&#10;        first = prev.next&#10;        second = prev.next.next&#10;        first.next = second.next&#10;        second.next = first&#10;        prev.next = second&#10;        prev = first&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Ll 24 Odd Even Linked List<br><br></b> <a href='https://leetcode.com/problems/odd-even-linked-list/' target='_blank'>LeetCode 328</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: head = [1,2,3,4,5], Output: [1,3,5,2,4]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain two pointers `odd` and `even`. Keep the `evenHead`. Loop to link `odd->next = even->next` and `even->next = odd->next`. Finally, link `odd->next = evenHead`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def oddEvenList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    if not head or not head.next: return head&#10;    odd, even, evenHead = head, head.next, head.next&#10;    while even and even.next:&#10;        odd.next = odd.next.next&#10;        even.next = even.next.next&#10;        odd = odd.next&#10;        even = even.next&#10;    odd.next = evenHead&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Ll 25 Split Linked List In Parts<br><br></b> <a href='https://leetcode.com/problems/split-linked-list-in-parts/' target='_blank'>LeetCode 725</a></td>
      <td rowspan="1"><b>Example 1:</b> Distribution math.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>-</td>
      <td><b>k > length:</b> Fill remaining parts with null.</td>
      <td><b>Explanation:</b> First, calculate the length of the list. Then, determine base size `len / k` and extra nodes `len % k`. Iterate through the list, breaking it into parts of appropriate sizes.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitListToParts(head: Optional[ListNode], k: int) -&gt; List[Optional[ListNode]]:&#10;    length = 0&#10;    curr = head&#10;    while curr:&#10;        length += 1&#10;        curr = curr.next&#10;    partSize, extra = length // k, length % k&#10;    ans = []&#10;    curr = head&#10;    for i in range(k):&#10;        ans.append(curr)&#10;        currentPartSize = partSize + (1 if extra &gt; 0 else 0)&#10;        extra -= 1&#10;        for _ in range(currentPartSize - 1):&#10;            if curr: curr = curr.next&#10;        if curr:&#10;            nextPart = curr.next&#10;            curr.next = None&#10;            curr = nextPart&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Ll 26 Reverse Nodes In K Group<br><br></b> <a href='https://leetcode.com/problems/reverse-nodes-in-k-group/' target='_blank'>LeetCode 25</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive/Iterative k-reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Count nodes. While `count >= k`, reverse `k` nodes. Keep track of previous group's tail to connect to current group's head. If `< k` nodes remain, just connect them.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    curr, nex, pre = dummy, dummy, dummy&#10;    count = 0&#10;    while curr.next:&#10;        curr = curr.next&#10;        count += 1&#10;    while count &gt;= k:&#10;        curr = pre.next&#10;        nex = curr.next&#10;        for _ in range(1, k):&#10;            curr.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = curr.next&#10;        pre = curr&#10;        count -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Ll 27 Rotate List<br><br></b> <a href='https://leetcode.com/problems/rotate-list/' target='_blank'>LeetCode 61</a></td>
      <td rowspan="1"><b>Example 1:</b> Find tail and break.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Compute length `N` of list. Connect tail to head to form a cycle. Find `k = k % N`. Move `N - k` steps from head. The new head is `current->next`. Break the cycle by setting `current->next = NULL`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateRight(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or not head.next or k == 0: return head&#10;    cur = head&#10;    length = 1&#10;    while cur.next:&#10;        length += 1&#10;        cur = cur.next&#10;    cur.next = head&#10;    k = k % length&#10;    k = length - k&#10;    while k &gt; 0:&#10;        cur = cur.next&#10;        k -= 1&#10;    head = cur.next&#10;    cur.next = None&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Ll 28 Flattening A Linked List<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Merge two sorted lists bottom-up.</td>
      <td><b>Time:</b> O(N * M) total nodes<br><b>Space:</b> O(N) aux space for recursion</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recursively go to the end of the `next` pointers. Merge the last two lists using the `bottom` pointers, just like merging two sorted linked lists. Return the merged head upwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, data):&#10;        self.data = data&#10;        self.next = None&#10;        self.bottom = None&#10;def mergeTwoLists(a, b):&#10;    temp = Node(0)&#10;    res = temp&#10;    while a is not None and b is not None:&#10;        if a.data &lt; b.data:&#10;            temp.bottom = a&#10;            temp = temp.bottom&#10;            a = a.bottom&#10;        else:&#10;            temp.bottom = b&#10;            temp = temp.bottom&#10;            b = b.bottom&#10;    if a: temp.bottom = a&#10;    else: temp.bottom = b&#10;    return res.bottom&#10;def flatten(root):&#10;    if root is None or root.next is None: return root&#10;    root.next = flatten(root.next)&#10;    root = mergeTwoLists(root, root.next)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Ll 29 Copy List With Random Pointer<br><br></b> <a href='https://leetcode.com/problems/copy-list-with-random-pointer/' target='_blank'>LeetCode 138</a></td>
      <td rowspan="1"><b>Example 1:</b> Insert copies in-between.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate list. For each node, insert a copy node right after it. Then, iterate again and set `copy->random = original->random->next`. Finally, separate the original list and the copy list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, x: int, next: &#x27;Node&#x27; = None, random: &#x27;Node&#x27; = None):&#10;        self.val = int(x)&#10;        self.next = next&#10;        self.random = random&#10;def copyRandomList(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    iter = head&#10;    while iter:&#10;        nxt = iter.next&#10;        copy = Node(iter.val)&#10;        iter.next = copy&#10;        copy.next = nxt&#10;        iter = nxt&#10;    iter = head&#10;    while iter:&#10;        if iter.random:&#10;            iter.next.random = iter.random.next&#10;        iter = iter.next.next&#10;    iter = head&#10;    pseudoHead = Node(0)&#10;    copy = pseudoHead&#10;    while iter:&#10;        nxt = iter.next.next&#10;        copy.next = iter.next&#10;        iter.next = nxt&#10;        copy = copy.next&#10;        iter = nxt&#10;    return pseudoHead.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Ll 30 Add Two Numbers Ii<br><br></b> <a href='https://leetcode.com/problems/add-two-numbers-ii/' target='_blank'>LeetCode 445</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack or reverse.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use two stacks to store the digits of the lists. Pop from stacks, add along with carry, and construct the new list by inserting at the head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    s1, s2 = [], []&#10;    while l1:&#10;        s1.append(l1.val)&#10;        l1 = l1.next&#10;    while l2:&#10;        s2.append(l2.val)&#10;        l2 = l2.next&#10;    carry = 0&#10;    head = None&#10;    while s1 or s2 or carry:&#10;        sum_val = carry&#10;        if s1: sum_val += s1.pop()&#10;        if s2: sum_val += s2.pop()&#10;        node = ListNode(sum_val % 10)&#10;        node.next = head&#10;        head = node&#10;        carry = sum_val // 10&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Ll 31 Split Linked List In Parts<br><br></b> <a href='https://leetcode.com/problems/split-linked-list-in-parts/' target='_blank'>LeetCode 725</a></td>
      <td rowspan="1"><b>Example 1:</b> Calculate lengths.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(k)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Count total nodes `N`. Each part will have at least `N // k` nodes, and the first `N % k` parts will have one extra node. Iterate and break the links.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitListToParts(head: Optional[ListNode], k: int) -&gt; List[Optional[ListNode]]:&#10;    ans = [None] * k&#10;    n = 0&#10;    node = head&#10;    while node:&#10;        n += 1&#10;        node = node.next&#10;    part, extra = divmod(n, k)&#10;    node = head&#10;    prev = None&#10;    for i in range(k):&#10;        if not node: break&#10;        ans[i] = node&#10;        for j in range(part + (1 if extra &gt; 0 else 0)):&#10;            prev = node&#10;            node = node.next&#10;        if prev: prev.next = None&#10;        extra -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Ll 32 Insertion Sort List<br><br></b> <a href='https://leetcode.com/problems/insertion-sort-list/' target='_blank'>LeetCode 147</a></td>
      <td rowspan="1"><b>Example 1:</b> Dummy head.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a dummy head for the sorted part. For each node in the original list, iterate through the sorted part to find its correct position and insert it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertionSortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    curr = head&#10;    while curr:&#10;        prev = dummy&#10;        while prev.next and prev.next.val &lt;= curr.val:&#10;            prev = prev.next&#10;        nxt = curr.next&#10;        curr.next = prev.next&#10;        prev.next = curr&#10;        curr = nxt&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Ll 33 Sort List<br><br></b> <a href='https://leetcode.com/problems/sort-list/' target='_blank'>LeetCode 148</a></td>
      <td rowspan="1"><b>Example 1:</b> Merge sort.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(log N) due to recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Merge sort for linked lists. Find mid using fast and slow pointers, split list into two, recursively sort, and merge the two sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    if not head or not head.next: return head&#10;    slow, fast = head, head.next&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    mid = slow.next&#10;    slow.next = None&#10;    left = sortList(head)&#10;    right = sortList(mid)&#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    while left and right:&#10;        if left.val &lt; right.val:&#10;            tail.next = left&#10;            left = left.next&#10;        else:&#10;            tail.next = right&#10;            right = right.next&#10;        tail = tail.next&#10;    if left: tail.next = left&#10;    if right: tail.next = right&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Ll 34 Partition List<br><br></b> <a href='https://leetcode.com/problems/partition-list/' target='_blank'>LeetCode 86</a></td>
      <td rowspan="1"><b>Example 1:</b> Two lists then join.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain two separate linked lists: `before` and `after` with their own dummy heads. Iterate through original list, appending to `before` or `after` based on value. Then link `before` tail to `after` head.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(head: Optional[ListNode], x: int) -&gt; Optional[ListNode]:&#10;    before_head = ListNode(0)&#10;    before = before_head&#10;    after_head = ListNode(0)&#10;    after = after_head&#10;    while head:&#10;        if head.val &lt; x:&#10;            before.next = head&#10;            before = before.next&#10;        else:&#10;            after.next = head&#10;            after = after.next&#10;        head = head.next&#10;    after.next = None&#10;    before.next = after_head.next&#10;    return before_head.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Ll 35 Swap Nodes In Pairs<br><br></b> <a href='https://leetcode.com/problems/swap-nodes-in-pairs/' target='_blank'>LeetCode 24</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative with dummy.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a dummy node. Maintain a `prev` pointer. While `prev->next` and `prev->next->next` exist, swap them and move `prev` two steps ahead.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapPairs(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    prev = dummy&#10;    while prev.next and prev.next.next:&#10;        first = prev.next&#10;        second = prev.next.next&#10;        first.next = second.next&#10;        second.next = first&#10;        prev.next = second&#10;        prev = first&#10;    return dummy.next</code></pre></details></td>
    </tr>
  </tbody>
</table>
