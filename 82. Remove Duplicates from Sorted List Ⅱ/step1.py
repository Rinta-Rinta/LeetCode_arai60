書きかけのコード
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
        
        root_node = head
        prev_node = head
        check_node = head

        if 
        while check_node.next is not None and check_node.val == check_node.next.val:
            check_node.next = check_node.next.next
```
解答を見てから書いたコード
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        ptr = dummy

        while ptr.next is not None and ptr.next.next is not None:
            if ptr.next.val == ptr.next.next.val:
                copy = ptr.next
                while copy.next is not None and copy.val == copy.next.val:
                    copy = copy.next
                
                ptr.next = copy.next
            else:
                ptr = ptr.next
        
        return dummy.next
```
