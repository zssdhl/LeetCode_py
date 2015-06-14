##Reverse Linked List
##Reverse a singly linked list.
##
##2015年6月10日 AC
##zss

##Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m == n:
            return head
        hh = ListNode(0)
        hh.next = head
        cur = hh
        for i in range(1,n+1):
            pre = cur
            cur = cur.next
            if i == m:
               plm = pre
               clm = cur
            if i == n:
                nln = cur.next
                cur.next = None
        shead,stail = self.reverseList(clm)
        plm.next = shead
        stail.next = nln
        return hh.next
        
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head,head
        pre = head
        cur = pre.next
        pre.next = None
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre,head
            
