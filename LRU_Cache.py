# Contains essential functions for implementation of a LRU Cache

# Importing the required modules
from LRU_DLL import LinkedList


# LRU Cache class implements the functionality of a LRU cache
class LRUCache:
    def __init__(self, size):
        self.cache_size = size
        self.ll = LinkedList()
        self.hashmap = dict()
        self.faults = 0

    def refer(self):
        pass

    def get_fault_count(self):
        return self.faults

    def display_cache(self):
        pass


# Function to manually test functionality
def main():
    lru_cache = LRUCache(5)
    print("The total faults so far are: ", lru_cache.get_fault_count())


if __name__ == '__main__':
    main()
