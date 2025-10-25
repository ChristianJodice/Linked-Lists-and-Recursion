
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        TODO:
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        TODO:
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def recursive_sum(self):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        return self._sum_helper(self.head)
    
    def _sum_helper(self, node):
        """
        Helper function for recursive sum.
        Base case: if node is None, return 0
        Recursive case: return node.data + sum of rest of list
        """
        if node is None:
            return 0
        return node.data + self._sum_helper(node.next)

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        self.head = self._reverse_helper(None, self.head)
    
    def _reverse_helper(self, prev, current):
        """
        Helper function for recursive reverse.
        Base case: if current is None, return prev (new head)
        Recursive case: reverse the rest and update current's next to prev
        """
        if current is None:
            return prev
        
        next_node = current.next
        current.next = prev
        return self._reverse_helper(current, next_node)

    def recursive_search(self, target):
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        return self._search_helper(self.head, target)
    
    def _search_helper(self, node, target):
        """
        Helper function for recursive search.
        Base case: if node is None, return False
        Base case: if node.data == target, return True
        Recursive case: search in the rest of the list
        """
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search_helper(node.next, target)

    def display(self):
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        if self.head is None:
            print("Empty list")
            return
        
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next
        
        print(" -> ".join(result) + " -> None")
