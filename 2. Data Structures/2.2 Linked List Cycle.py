# Qns: Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Link: https://leetcode.com/problems/linked-list-cycle/


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

    # Solution 1: Hashing Approach.
    # Time complexity = O(N)
    def hasCycle1(self, head):
        hashTable = set()
        currentNode = head

        while(currentNode):
            if(currentNode in hashTable):
                return True
            else:
                hashTable.add(currentNode)
                currentNode = currentNode.next

        return False

    # Solution 2: Floyd’s Cycle-Finding Algorithm
    # Time complexity = O(N)
    def hasCycle2(self, head):
        fast, slow = head, head

        while slow and fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if fast == slow:
                return True

        return False


# Testing
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)

# Create a loop for testing
l.head.next.next.next.next = l.head.next

print("hasCycle1(): ", "Loop detected" if l.hasCycle1(l.head) else "No Loop")
print("hasCycle2(): ", "Loop detected" if l.hasCycle2(l.head) else "No Loop")
