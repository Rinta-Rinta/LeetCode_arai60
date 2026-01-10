```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number = 0
        l2_number = 0

        #l1の数字を求める
        node = l1
        digit = 1
        while node is not None:
            l1_number += node.val * digit
            digit = digit * 10
            node = node.next
        
        #l2の数字を求める
        node = l2
        digit = 1
        while node is not None:
            l2_number += node.val * digit
            digit = digit * 10
            node = node.next
        
        sum = l1_number + l2_number
         
        if sum == 0:
            node = ListNode(0)
            return  node

        dummy = ListNode()
        last_added_node = dummy
        #sumの１の位から順にリストを作成する
        while sum != 0:
            node_val = sum % 10
            sum = (sum - node_val) // 10

            node = ListNode(node_val)
            last_added_node.next = node
            last_added_node = node
         
        return dummy.next
```
