step1
訪れたノードのアドレスを記録しておき、同じアドレスが出てきたらサイクルがあると判断できると考えた。

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        check = head

        while check != None:
            if id(check) in visited:
                return True

            visited.append(id(check))

            check = check.next

        return False
```

解説の動画を見てみると知らない方法を使っていたのでそれも真似してみた。

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
```

