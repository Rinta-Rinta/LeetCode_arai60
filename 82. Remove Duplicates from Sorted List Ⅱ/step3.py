step3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy = ListNode()
        dummy.next = head
        ptr = dummy

        while ptr.next is not None and ptr.next.next is not None:
            if ptr.next.val != ptr.next.next.val:
                ptr = ptr.next
            else:
                duplicated_val = ptr.next.val
                runner = ptr.next
                while runner.next is not None and runner.next.val == duplicated_val:
                    runner.next = runner.next.next
                
                ptr.next = runner.next
        
        return dummy.next
```
