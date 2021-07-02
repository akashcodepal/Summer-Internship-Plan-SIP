# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # we need 2 pointers to delete 1 node , but for this case we don't have prev
        # so we will delete next node inplce of this node and copy its value and pass it in this node
        
        nodeValue = node.next.val   # 1
        node.val = nodeValue      # replace 5 with 1
        node.next = node.next.next   # delete node with origianl value 1
        
        
        
