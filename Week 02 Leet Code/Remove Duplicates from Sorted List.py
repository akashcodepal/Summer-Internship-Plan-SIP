# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None :
            return head
        
        prev = head
        current = head.next
        
        while current != None :
            if prev.val == current.val :
                prev.next = current.next
                current = current.next
            else :
                prev = prev.next
                current = current.next
                
        return head         
