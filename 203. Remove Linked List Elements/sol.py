class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        res.next = head
        head = res
        while head != None and head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return res.next