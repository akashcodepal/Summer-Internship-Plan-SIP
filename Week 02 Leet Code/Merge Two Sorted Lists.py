# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # created result_head with un necessary node
        result_head = ListNode(0)
        result_current = result_head
        
        while l1 and l2 :
            if l1.val <= l2.val :
                
                result_current.next = l1 
                result_current = result_current.next 
                l1 = l1.next 
                
            elif l1.val > l2.val :
                result_current.next = l2
                result_current = result_current.next
                l2 = l2.next
        
        while l1 :
            result_current.next = l1
            result_current = result_current.next 
            l1 = l1.next
        
        while l2 :
            result_current.next = l2
            result_current = result_current.next 
            l2 = l2.next
        
        
        # remove that unnecessary node by sending result_head.next
        return result_head.next        
            
