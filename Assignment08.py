# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Stupponce,05/27/2021, Added code for Product class
# Stupponce,05/27/2021, Added code for FileProcessor class
# Stupponce,05/27/2021, Added code for IO class
# Stupponce,05/27/2021, Added code for Main Body of script
# ------------------------------------------------------------------------ #


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Stupponce, 05/27/2021, Added sections to class
        Stupponce, 05/27/2021, Added documentation to class
    """

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error assigning values: \n" + str(e))


    # -- Properties --

    # product_name
    @property
    def product_name(self):  # getter
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, name_value: str):  # setter
        if str(name_value).isnumeric():
            self.__product_name = name_value
        else:
            raise Exception("Please enter a string for the name")

    # product_price
    @property
    def product_price(self):  # getter
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, price_value: float):  # setter
        if str(price_value).isnumeric():
            self.__product_price = float(price_value)
        else:
            raise Exception("Please enter a number for the price")

    # -- Methods --
    def to_string(self):  # converts product data to string
        return self.__str__()

    def __str__(self):  # converts product data to string
        return self.product_name + ',' + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name, list_of_product_objects): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Stupponce, 05/27/2021, Added methods to class
        Stupponce, 05/27/2021, Added documentation to class
    """
    # -- Methods --
    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """Writes data to file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) of product objects data to save to file
        :return: (bool) status of save
        """
        save_status = False
        try:
            file = open(file_name, "w")
            # file.write(list_of_product_objects)
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            save_status = True
        except Exception as e:
            print("Error in saving data to file")
            print(e, e.__doc__, type(e), sep="\n")
        return save_status

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of product rows

        :param file_name: (string) with name of file
        :return: (list) of product objects rows
        """
        try:
            list_of_product_rows = []
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("Error in reading the data from file")
            print(e, e.__doc__, type(e), sep="\n")
        return list_of_product_rows
    # Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

    methods:
        print_menu():

        input_menu_choice(): -> (string that captures user's menu choice)

        print_current_data_in_list(list_of_product_objects):

        input_new_name_and_price(): -> (string that captures user's product data)

    changelog: (When, Who, What)
        Stupponce, 05/27/2021, Added methods to class
        Stupponce, 05/27/2021, Added documentation to class
    """

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show Current Product Data
            2) Add Product Data
            3) Save Data to File
            4) Exit Program       
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_data_in_list(list_of_product_rows: list):
        """ Shows the current items in the list of rows

        :param list_of_product_rows: (list) of products you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_product_rows:
            print(row.product_name + " - $" + str(row.product_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_name_and_price():
        """ Gets a new product name and price from the user

        :return: (Product) object with new name and price
        """
        try:
            new_name = str(input("Enter a new product name: ").strip())
            new_price = float(input("Enter new product price: ").strip())
            p = Product(product_name=new_name, product_price=new_price)
        except Exception as e:
            print("Error in getting new data")
            print(e)
        return p
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        IO.print_menu()  # Show user a menu of options
        menu_choice = IO.input_menu_choice()  # Get user's menu option choice

        if menu_choice == "1":  # Show user current data in the list of product objects
            IO.print_current_data_in_list(lstOfProductObjects)

        elif menu_choice == "2":  # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_new_name_and_price())

        elif menu_choice == "3":  # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Saving Data...")

        elif menu_choice == "4":
            print("Exiting Program...")
            break
except Exception as e:
    print("Error in main body of script")
    print(e, e.__doc__, type(e), sep="\n")
# Main Body of Script  ---------------------------------------------------- #

