# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head :
            return 
        
        if not head.next :
            return head
        
        current = head
        
        while current:
            # swap
            temp = current.val
            if current.next is None :
                return head
            current.val = current.next.val
            current.next.val = temp
            
            # increament the current 
            current = current.next.next
            
        return head    
