step3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        fixed_tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            node1_val = 0
            if l1 is not None:
                node1_val = l1.val
                l1 = l1.next
            
            node2_val = 0
            if l2 is not None:
                node2_val = l2.val
                l2 = l2.next
            
            total = node1_val + node2_val + carry
            
            digit = total % 10
            fixed_tail.next = ListNode(digit)
            fixed_tail = fixed_tail.next

            carry = total // 10
        
        return dummy.next
```
