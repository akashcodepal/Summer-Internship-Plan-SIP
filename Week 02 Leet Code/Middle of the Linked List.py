# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def len_list(self,head) :
        count , current = 0 , head
        while current :
            count+=1
            current=current.next
        return count
    
    def middleNode(self, head: ListNode) -> ListNode:
        len , current = self.len_list(head) , head
        i = 0
        while i != len//2 :
            current=current.next
            i+=1
        
        head = current
        
        return head
