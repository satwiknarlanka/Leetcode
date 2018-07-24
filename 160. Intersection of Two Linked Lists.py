# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
offset the loop but running through it twice for different lengths and switching heads when none is reached
this is very tricky and needs to be traced manually to understand
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa,pb = headA,headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
        
        '''
        Old solution find difference of lengths and offset it
        
        x,y = headA,headB
        lenA,lenB = 0,0
        while x:
            lenA +=1
            x = x.next
        while y:
            lenB +=1
            y = y.next
        
        big,small = headA,headB
        diff = 0
        if lenA<lenB:
            big,small = headB,headA
            diff = lenB - lenA
        else:
            diff = lenA - lenB
        
        for i in range(diff):
            big = big.next
        
        while big and small:
            if big is small:
                return big
            big = big.next
            small = small.next
        
        return None
        '''