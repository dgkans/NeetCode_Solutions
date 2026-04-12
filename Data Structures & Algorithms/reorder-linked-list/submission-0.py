# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #splitting
        mid = end = head
        while end.next and end.next.next != None:
            mid = mid.next
            end = end.next.next
        p2 = mid.next
        mid.next = None

        #reversing
        prev = None
        while p2:
            temp=p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        p2 =prev
        #merge
        p1 = head
        
        while p1 and p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next
        