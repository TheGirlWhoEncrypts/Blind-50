# Qns: Given the head of a singly linked list, reverse the list, and return the reversed list.
# Link: https://leetcode.com/problems/reverse-linked-list/

# Iterative Method
# Time complexity = O(N)


class ListNode:
    # Initalise node object
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    # Intialise head
    def __init__(self):
        self.head = None

    # Insert a new node
    def push(self, val):
        newNode = ListNode(val)

        if self.head:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
        else:
            self.head = newNode

    # Print Linked List
    def print(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val)
            currentNode = currentNode.next

    # Solution
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        else:
            previousNode, currentNode = None, head

            # Go till the last node of the list
            while currentNode:
                nextNode = currentNode.next

                currentNode.next = previousNode  # Reverse the link
                previousNode = currentNode  # Move previousNode one node ahead
                currentNode = nextNode  # Move currentNode one node ahead

            return previousNode


# Testing
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.print()

l.reverseList(l.head)
l.print()
