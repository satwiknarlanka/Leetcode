import heapq
# Definition for singly-linked list.
class ListNode:
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

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        lists = [x for x in lists if x and x != []]
        if not lists:
            return []
        heap = [(x.val,i) for i,x in enumerate(lists)]
        heapq.heapify(heap)
        headc = heapq.heappop(heap)
        head = lists[headc[1]]
        if head.next:
            heapq.heappush(heap,(lists[headc[1]].next.val,headc[1] ))
            lists[headc[1]] = lists[headc[1]].next
        curr = head
        while len(heap):
            node = heapq.heappop(heap)
            curr.next = lists[node[1]]
            if lists[node[1]].next:
                heapq.heappush(heap,(lists[node[1]].next.val,node[1]))
                lists[node[1]] = lists[node[1]].next
            curr = curr.next
        return(head)


# Test case
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1,l2,l3]
s = Solution()
ans = s.mergeKLists(lists)
ans.printList()
t = [None,ListNode(1)]
x = s.mergeKLists(t)
x.printList()


# although if you could manipulate the definition of Listnode this is much cleaner
# import heapq
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def __lt__(self,other):
#         return self.val < other.val
#     def printList(self):
#         x = self
#         while x:
#             print(x.val, end = '')
#             if x.next:
#                 print('->',end = '')
#             x = x.next
#         print()

# class Solution:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if not lists:
#             return []
#         lists = [x for x in lists if x and x != []]
#         if not lists:
#             return []
#         heapq.heapify(lists)
#         head = heapq.heappop(lists)
#         if head.next:
#             heapq.heappush(lists, head.next)
#         curr = head
#         while len(lists):
#             node = heapq.heappop(lists)
#             curr.next = node
#             if node.next:
#                 heapq.heappush(lists,node.next)
#             curr = curr.next
#         return(head)
