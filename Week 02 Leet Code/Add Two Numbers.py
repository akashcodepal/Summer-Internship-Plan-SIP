# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp_head = ListNode(0);
        # 1 extra node is created with val 0.. so remove it later
        current = temp_head
        carry = 0
        
        while l1 or l2 or carry :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            carry ,val3 = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(val3)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        temp_head = temp_head.next
        #extra node removed
        
        return temp_head
