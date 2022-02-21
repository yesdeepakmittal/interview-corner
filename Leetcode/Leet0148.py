# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr:
            l.append(ptr.val)
            ptr = ptr.next
        l.sort()
        if len(l) < 1: return head
        
        head = ListNode(l[0])
        ptr = head
        for i in range(1,len(l)):
            ptr.next = ListNode(l[i])
            ptr = ptr.next
        return head
        