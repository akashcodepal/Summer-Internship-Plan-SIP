# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_data = set()
        current  = headA
        while current :
            node_data.add(current)
            current = current.next
        
        current = headB
        while current :
            if current in node_data :
                return current
            current = current.next
        
        return None
