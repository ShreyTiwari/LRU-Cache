# Contains the Implementation of Doubly Linked List that will be used by the LRU cache.

# Node class acts as the blueprint for the node objects that will be a part of the doubly linked list
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# Linked List class acts as the blueprint for creating the doubly linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Function to add a node to the front of the list
    def add_node_front(self, value):
        new_node = Node(value)

        if self.count == 0:
            self.head = self.tail = new_node

        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node

        self.count += 1
        return new_node

    # Function to add a node to the back of the list
    def add_node_back(self, value):
        new_node = Node(value)

        if self.count == 0:
            self.head = self.tail = new_node

        else:
            new_node.left = self.tail
            self.tail.right = new_node
            self.tail = new_node

        self.count += 1
        return new_node

    # Function to remove a node from the front of the list
    def remove_node_front(self):
        data = None
        if self.count == 0:
            return data

        elif self.count == 1:
            self.head = self.tail = None

        else:
            data = self.head.data
            self.head = self.head.right
            self.head.left = None

        self.count -= 1
        return data

    # Function to remove a node from the back of the list
    def remove_node_back(self):
        data = None
        if self.count == 0:
            return data

        elif self.count == 1:
            self.head = self.tail = None

        else:
            data = self.tail.data
            self.tail = self.tail.left
            self.tail.right = None

        self.count -= 1
        return data

    # Function to move a node in the linked list to the back
    def move_node_back(self, node):
        if self.tail == node:
            return

        if self.head == node:
            self.head = self.head.right
            self.head.left = None

        else:
            node.left.right = node.right
            node.right.left = node.left

        node.right = None
        node.left = self.tail
        self.tail.right = node
        self.tail = node

    # Function to display the list
    def display_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="  ")
            temp = temp.right
        print()


def accept_int():
    while True:
        try:
            input_data = int(input("Enter a number: "))
            return input_data
        except:
            print("Invalid input. Try again...")


# Function to manually test functionality
def main():
    print("------------------------------ Welcome ------------------------------")
    ll = LinkedList()

    while True:
        print(
            "\n1. Display list\n2. Add node (front)\n3. Add node (back)\n4. Remove node (front)\n5. Remove node (back)\nPress any other key to exit...")
        choice = input("Make a choice: ")

        if choice == '1':
            print("\nThe list is:")
            ll.display_list()
        elif choice == '2':
            data = accept_int()
            _ = ll.add_node_front(data)
        elif choice == '3':
            data = accept_int()
            _ = ll.add_node_back(data)
        elif choice == '4':
            _ = ll.remove_node_front()
        elif choice == '5':
            _ = ll.remove_node_back()
        else:
            print("\n------------------------------ Thank You ------------------------------")
            break


# Code execution starts here
if __name__ == '__main__':
    main()
