# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printList(self):
        x = self
        while x:
            print(x.val, end = '')
            if x.next:
                print('->',end = '')
            x = x.next
        print()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        sums = 0
        while l1 or l2:
            if l1:
                sums += l1.val
                l1 = l1.next
            if l2:
                sums += l2.val
                l2 = l2.next
            curr.next = ListNode(sums%10)
            curr = curr.next
            sums //= 10
        if sums:
            curr.next = ListNode(sums)
        return head.next

# Test case
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
ans = s.addTwoNumbers(l1,l2)
l1.printList()
l2.printList()
ans.printList()