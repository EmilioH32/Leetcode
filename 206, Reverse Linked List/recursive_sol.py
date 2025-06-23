class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursiveReverse(node, prev):
            nextNode = node.next
            node.next = prev
            if not nextNode:
                return node
            return recursiveReverse(nextNode, node)
        return recursiveReverse(head, None) if head else None  