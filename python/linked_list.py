# Initiate the class of linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# ---------------------------------------------------------------------------------------------------

# find the middle of a linked list

def find_middle(node):

    slow = fast = node
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow

# ---------------------------------------------------------------------------------------------------

# head = node = ListNode(0)
# for i in range(10)[1:]:
#     node.next = ListNode(i)
#     node = node.next
#
# a = []
# node = head
# while node:
#     a.append(node.val)
#     node = node.next
# print(a)
#
# a = []
# node = find_middle(head)
# while node:
#     a.append(node.val)
#     node = node.next
# print(a)

# ---------------------------------------------------------------------------------------------------

# reverse a linked list

def reverseList(node):

    if not node:
        return node

    prev, cur = None, node
    while cur:
        next_one = cur.next
        cur.next = prev
        prev, cur = cur, next_one
    return prev

# ---------------------------------------------------------------------------------------------------

# head = node = ListNode(0)
# for i in range(10)[1:]:
#     node.next = ListNode(i)
#     node = node.next
#
# a = []
# node = head
# while node:
#     a.append(node.val)
#     node = node.next
# print(a)
#
# a = []
# node = reverseList(head)
# while node:
#     a.append(node.val)
#     node = node.next
# print(a)

# ---------------------------------------------------------------------------------------------------
