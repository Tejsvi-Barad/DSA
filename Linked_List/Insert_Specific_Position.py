class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Add First
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Add Last
    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Add Middle
    def add_middle(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        # Find middle
        slow = self.head
        fast = self.head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node.next = slow.next
        slow.next = new_node

    # Display
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l1 = SLL()

while True:
    print("\n--- Singly Linked List ---")
    print("1. Add First")
    print("2. Add Middle")
    print("3. Add Last")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        l1.add_first(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        l1.add_middle(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        l1.add_last(data)

    elif choice == 4:
        l1.display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
