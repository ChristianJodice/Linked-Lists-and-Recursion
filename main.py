from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    print("Creating linked list with sample data...")
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)
    ll.insert_at_end(15)

    # TODO: 3) Display the list to verify insertion
    print("Initial list:")
    ll.display()

    # TODO: 4) Call recursive_sum and print the result
    total_sum = ll.recursive_sum()
    print(f"Sum of all elements: {total_sum}")

    # TODO: 5) Call recursive_search with a target and print result
    search_target = 10
    found = ll.recursive_search(search_target)
    print(f"Search for {search_target}: {'Found' if found else 'Not found'}")
    
    search_target = 999
    found = ll.recursive_search(search_target)
    print(f"Search for {search_target}: {'Found' if found else 'Not found'}")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("\nReversing the list...")
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()
    
    print(f"Sum after reversal: {ll.recursive_sum()}")