# ================================================================================================= #
""" Description: Contains the implementation of a LRU Cache """
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
from Linked_List.doubly_linked_list import doubly_linked_list
from Helper.helper_functions import helper_functions
from Logger.logger import logger_wrapper

# Total Pages
TOTAL_PAGES = 10


# LRU Cache class implements the functionality of a LRU cache
class lru_cache:
    def __init__(self, size, logger):
        self.cache_size = size
        self.ll = doubly_linked_list()
        self.hashmap = [None] * TOTAL_PAGES
        self.faults = 0
        self.logger = logger

        self.logger.info("LRU Cache Instance created and initialized")
        self.logger.debug("LRU Cache Instance parameters are: Size - {}, Total Pages = {}".format(self.cache_size, TOTAL_PAGES))

    def refer(self, page):
        self.logger.info("Cache refer call was made")

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

        self.logger.debug("The page requested was {} and the refer call result was - {}".format(page, status))
        return status

    def display_cache(self):
        self.logger.info("Display Cache call was made")

        print("The total number of cache misses as far is: ", self.faults)
        print("The present cache state is")
        self.ll.display_list()

        self.logger.debug("The total cache misses are - {}".format(self.faults))


# Code execution begins here
def main():
    lw = logger_wrapper()
    logger = lw.new_logger()

    logger.debug("Program Execution Initiated")
    print("------------------------------ Welcome ------------------------------")
    print("Please specify the cache size...")
    lru_cache_test = lru_cache(helper_functions.accept_int(), logger)

    while True:
        print("\n1. Refer Cache\n2. Display Cache\nPress any other key to exit...")
        choice = input("Make a choice: ")

        if choice == '1':
            print("Specify the page to be referred...")
            page = helper_functions.accept_int_range(0, TOTAL_PAGES - 1)
            print("The cache reference status is:", lru_cache_test.refer(page))
        elif choice == '2':
            lru_cache_test.display_cache()
        else:
            print("\n------------------------------ Thank You ------------------------------")
            break

    logger.debug("Program Execution Completed")


if __name__ == '__main__':
    main()
