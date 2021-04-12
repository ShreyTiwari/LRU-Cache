# ================================================================================================= #
""" Description: Contains the implementation of helper functions """
# ================================================================================================= #
__author__ = "Shrey Tiwari"
__copyright__ = "Copyright 2021, LRU Cache"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Shrey Tiwari"
__email__ = "shreymt@gmail.com"
__status__ = 'Prototype'
# ================================================================================================= #


# Helper Functions class implements basic helper functions
class helper_functions:
    @staticmethod
    def accept_int():
        while True:
            try:
                input_data = int(input("Enter a number: "))
                return input_data
            except Exception as exception:
                print("Exception raised: ", exception)
                print("Invalid input. Try again...")

    @staticmethod
    def accept_int_range(lower, upper):
        while True:
            try:
                input_data = int(input("Enter a number: "))

                if lower <= input_data <= upper:
                    return input_data
                else:
                    raise Exception("Input Out of Range.")

            except Exception as exception:
                print("Exception raised: ", exception)
                print("Invalid input. Try again...")


# Function to manually test functionality
def test():
    print("------------------------------ Welcome ------------------------------")

    while True:
        print("\n1. Accept Integer\n2. Accept Integer in Range\nPress any other key to exit...")
        choice = input("Make a choice: ")

        if choice == '1':
            print("The number entered is: ", helper_functions.accept_int())
        elif choice == '2':
            print("Enter the lower limit, the upper limit followed by the actual number...")
            lower = helper_functions.accept_int()
            upper = helper_functions.accept_int()
            print("The number entered is: ", helper_functions.accept_int_range(lower, upper))

        else:
            print("\n------------------------------ Thank You ------------------------------")
            break


if __name__ == '__main__':
    test()
