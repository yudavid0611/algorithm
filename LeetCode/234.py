# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head
        rev = ListNode()

        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
        
        # 노드 개수가 홀수일 경우
        if fast:
            slow, rev, rev.next = slow.next, slow, rev
        
        while slow:
            if slow.val != rev.val:
                break
            slow, rev = slow.next, rev.next
        else:
            print(True)
        print(False)

        