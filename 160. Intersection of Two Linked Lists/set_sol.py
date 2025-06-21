class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        seen = set()
        while a:
            if a not in seen:
                seen.add(a)
                a = a.next
            else:
                return a
        while b:
            if b not in seen:
                seen.add(b)
                b = b.next
            else:
                return b