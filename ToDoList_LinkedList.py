# CS211 Final Project – Linked List To-Do List Manager
# Author: <Mehmet Mert Asma>
# Demonstrates linked list operations: insert, delete, update, search, traverse.

class Node: # I made the node here 
    def __init__(self, data, next): # constructor
        self.data = data # setting data
        self.next = next # setting next node
    
    def getData(self): # getting data
        return self.data # return data
    
    def getNext(self): # getting next node
        return self.next # return next node
    
    def setData(self, Data): # setting data
        self.data = Data # set data to Data
    
    def setNext(self, Next): # setting next node
        self.next = Next # set next node to Next
    
    def __str__(self): # string representation
        return str(self.data) # return data as string
    
class LinkedList: # linked list class

    def __init__(self): # constructor

        self.head = None # head node initialized to None
    
    def insert_at_beginning(self, data): # insert at beginning

        new_node = Node(data, self.head) # create new node
        self.head = new_node # set head to new node
    
    def insert_at_end(self, data): # insert at end
        
        new_node = Node(data, None) # create new node
        if self.head is None: # if list is empty
            self.head = new_node # set head to new node
            return 
        current = self.head # start from head
        while current.getNext() is not None: # traverse to end
            current = current.getNext() # move to next node
        current.setNext(new_node) # set next of last node to new node

    def delete_node(self, key): # delete node by key

        current = self.head # start from head
        previous = None # previous node initialized to None

        if current is None: # if list is empty
            print("List is empty.") # print message
            return

        if current.getData() == key: # if head node is to be deleted
            self.head = current.getNext() # set head to next node
            return

        while current is not None and current.getData() != key: # traverse to find key
            previous = current # set previous to current
            current = current.getNext() # move to next node

        if current is None: # if key not found
            print("Node not found.") # print message
            return

        previous.setNext(current.getNext()) # unlink the node

    def delete_at_position(self, pos): # delete node at position
    
        if self.head is None or pos < 0: # if list is empty or position is invalid
            print("Invalid position or empty list.")
            return

        if pos == 0: # if head node is to be deleted
            self.head = self.head.getNext()
            return

        current = self.head 
        index = 0 
        while current is not None and index < pos - 1: 
            current = current.getNext() 
            index += 1

        if current is None or current.getNext() is None: 
            print("Position out of range.")
            return

        current.setNext(current.getNext().getNext())

    def update_at_position(self, pos, new_data):
    
        if pos < 0:
            print("Invalid position.")
            return

        current = self.head
        index = 0

        while current is not None and index < pos:
            current = current.getNext()
            index += 1

        if current is None:
            print("Position out of range.")
            return

        current.setData(new_data)
        print(f" Task at position {pos} updated to '{new_data}'.")


    def search(self, key):
        
        current = self.head
        while current is not None:
            if current.getData() == key:
                return True
            current = current.getNext()
        return False
    
    def display(self):
        
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current is not None:
            print(current.getData(), end=" -> ")
            current = current.getNext()
        print("None")
    
    def get_length(self):
        
        n, cur = 0, self.head
        while cur is not None:
            n += 1
            cur = cur.getNext()
        return n
    
    def insert_at_position(self, data, pos):
   
        if self.head is None or pos <= 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        index = 0
        while current.getNext() is not None and index < pos - 1:
            current = current.getNext()
            index += 1

        new_node = Node(data, current.getNext())
        current.setNext(new_node)

def main():
    todo = LinkedList()  # your linked list object
    while True:
        print_menu("TO-DO LIST MANAGER", [
        "Add task at beginning",
        "Add task at end",
        "Insert task at position",
        "Delete task by title",
        "Delete task by position",
        "Update task at position",
        "Search for task",
        "View all tasks",
        "Show number of tasks",
        "Exit program"
])

        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            todo.insert_at_beginning(title)
            print(f" Task '{title}' added at beginning.\n")

        elif choice == "2":
            title = input("Enter task title: ")
            todo.insert_at_end(title)
            print(f" Task '{title}' added at end.\n")

        elif choice == "3":
            title = input("Enter task title: ")
            pos = int(input("Enter position (0-based index): "))
            todo.insert_at_position(title, pos)
            print(f" Task '{title}' inserted at position {pos}.\n")

        elif choice == "4":
            title = input("Enter task title to delete: ")
            todo.delete_node(title)
            print(f" Task '{title}' deleted (if it existed).\n")

        elif choice == "5":
            pos = int(input("Enter position (0-based index) to delete: "))
            todo.delete_at_position(pos)
            print(f" Task at position {pos} deleted (if it existed).\n")

        elif choice == "6":
            pos = int(input("Enter position (0-based index) to update: "))
            new_title = input("Enter new task title: ")
            todo.update_at_position(pos, new_title)

        elif choice == "7":
            title = input("Enter task title to search: ")
            found = todo.search(title)
            print(f" Task '{title}' found.\n" if found else f" Task '{title}' not found.\n")

        elif choice == "8":
            todo.display()

        elif choice == "9":
            print(f" Total tasks: {todo.get_length()}\n")

        elif choice == "10":
            print("\n Exiting program... Goodbye!\n")
            break

        else:
            print(" Invalid option. Please choose between 1-10.\n")


def print_menu(title="MAIN MENU", options=None):
    if options is None:
        options = []
    border = "=========================================="
    print("\n" + border)
    print(f"       {title.upper()}")
    print(border)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print(border)


if __name__ == "__main__":
    main()


