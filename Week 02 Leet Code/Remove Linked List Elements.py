# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head :
            return 
        
        prev = head
        current = head.next
        
        while current :
            if current.val == val :
                prev.next = current.next
            else :
                prev = current
            current = current.next
            
        if head.val == val :
            return head.next
        
        return head    
