# ================================================================================================= #
""" Description: Contains the implementation of Doubly Linked List """
# ================================================================================================= #
__author__ = "Shrey Tiwari"
__copyright__ = "Copyright 2021, LRU Cache"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Shrey Tiwari"
__email__ = "shreymt@gmail.com"
__status__ = 'Prototype'
# ================================================================================================= #

# Importing the required modules
from Helper.helper_functions import helper_functions


# Node class acts as the blueprint for the node objects that will be a part of the doubly linked list
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# Linked List class acts as the blueprint for creating the doubly linked list
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Function to add a node to the front of the list
    def add_node_front(self, value):
        new_node = node(value)

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
        new_node = node(value)

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


# Function to manually test functionality
def main():
    print("------------------------------ Welcome ------------------------------")
    dll = doubly_linked_list()

    while True:
        print(
            "\n1. Display list\n2. Add node (front)\n3. Add node (back)\n4. Remove node (front)\n5. Remove node (back)\nPress any other key to exit...")
        choice = input("Make a choice: ")

        if choice == '1':
            print("\nThe list is:")
            dll.display_list()
        elif choice == '2':
            data = helper_functions.accept_int()
            _ = dll.add_node_front(data)
        elif choice == '3':
            data = helper_functions.accept_int()
            _ = dll.add_node_back(data)
        elif choice == '4':
            _ = dll.remove_node_front()
        elif choice == '5':
            _ = dll.remove_node_back()
        else:
            print("\n------------------------------ Thank You ------------------------------")
            break


# Code execution starts here
if __name__ == '__main__':
    main()
