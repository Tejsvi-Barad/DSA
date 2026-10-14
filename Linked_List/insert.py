class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insert_position(self, data, pos):
        new_node = Node(data)

        # Insert at the first position
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        # Move to the node before the required position
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" => ")
            temp = temp.next
        print("None")


s1 = SLL()

# Add initial nodes
n = int(input("How many nodes initially? "))

for i in range(n):
    data = int(input(f"Enter data for node {i + 1}: "))
    s1.insert_last(data)

# Menu
while True:
    print("\n---- Linked List Menu ----")
    print("1. Insert first")
    print("2. Insert last")
    print("3. Insert at specific position")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        s1.insert_first(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        s1.insert_last(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        s1.insert_position(data, pos)

    elif choice == 4:
        s1.display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice")