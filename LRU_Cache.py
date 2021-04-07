# Contains essential functions for implementation of a LRU Cache

# Importing the required modules
from LRU_DLL import LinkedList
from LRU_DLL import accept_int

# Defining total number of pages (zero based indexing)
TOTAL_PAGES = 10


# LRU Cache class implements the functionality of a LRU cache
class LRUCache:
    def __init__(self, size):
        self.cache_size = size
        self.ll = LinkedList()
        self.hashmap = [None] * TOTAL_PAGES
        self.faults = 0

    def refer(self, page):
        status = ""

        if self.hashmap[page] is not None:
            status = "Cache Hit!"
            self.ll.move_node_back(self.hashmap[page])

        else:
            status = "Cache Miss"
            self.faults += 1

            if self.ll.count == self.cache_size:
                page_removed = self.ll.remove_node_front()
                self.hashmap[page_removed] = None

            node = self.ll.add_node_back(page)
            self.hashmap[page] = node

        return status

    def total_faults(self):
        print("The total number of cache misses as far is: ", self.faults)

    def display_cache(self):
        print("The present cache state is")
        self.ll.display_list()


# Function to manually test functionality
def main():
    print("------------------------------ Welcome ------------------------------")
    print("Please specify the cache size...")
    size = accept_int()
    lru_cache = LRUCache(size)

    while True:
        print("\n1. Refer Cache\n2. Total Faults\n3. Display Cache\nPress any other key to exit...")
        choice = input("Make a choice: ")

        if choice == '1':
            print("Specify the page to be referred...")
            page = accept_int()
            print("The cache reference status is:", lru_cache.refer(page))
        elif choice == '2':
            lru_cache.total_faults()
        elif choice == '3':
            lru_cache.display_cache()
        else:
            print("\n------------------------------ Thank You ------------------------------")
            break


if __name__ == '__main__':
    main()
