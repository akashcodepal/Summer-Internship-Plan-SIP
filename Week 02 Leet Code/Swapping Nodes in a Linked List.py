# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len_list(self,head):
        current = head 
        count = 0
        while current :
            count += 1
            current = current.next
        return count
    
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        if not head :
            return 
        
        crnt_start = head
        count = 1
        while crnt_start.next :
            if count == k :
                break
            count += 1    
            crnt_start = crnt_start.next
            
        crnt_end = head
        len = self.len_list(head)
        count = 1
        while crnt_end.next :
            if count == len - k + 1 :
                break
            count += 1    
            crnt_end = crnt_end.next    
        
        # swap
        crnt_start.val , crnt_end.val = crnt_end.val , crnt_start.val
        
        return head
