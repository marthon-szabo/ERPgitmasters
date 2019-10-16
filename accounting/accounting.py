""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

items = data_manager.get_table_from_file("accounting/items.csv")
id_for_test = "vH34Jz#&"
year_to_test = 2015

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    
    options = ["Show table",
                "Add",
                "Remove",
                "Update",
                "Which year has the highest profit?",
                "What is the average (per item) profit in a given year?"]
    while True:
        ui.print_menu("Accounting", options, "Back to main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(items)
        elif option == "2":
            add(items)
        elif option == "3":
            remove(items, id_for_test)
        elif option == "4":
            update(items, id_for_test)
        elif option == "5":
            which_year_max(items)
        elif option == "6":
            avg_amount(items, year_to_test)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    list_labels = ["id", "month", "day", "year", "type", "amount"]
    items = data_manager.get_table_from_file("accounting/items.csv")
    
    ui.print_table(items, list_labels)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    id_ = common.generate_random(table)
    list_labels = ["month ", "day ", "year ", "type ", "amount "]
    title = "Please give all new data: "
    item = ui.get_inputs(list_labels, title)
    item.insert(0, id_)
    table.append(item)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for item in table:
        if item[0] == id_:
            table.remove(item)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    list_labels = ["month ", "day ", "year ", "type ", "amount "]
    title = "Please give all new data: "
    item = ui.get_inputs(list_labels, title)
    item.insert(0, id_)
    for element in table:
        if element[0] == id_:
            element[0] = item
    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    year_prof = {}
    
    for item in table:
        if item[3] in year_prof:    
            if item[4] == "in":
                year_prof[item[3]] = year_prof[item[3]] + int(item[5])
            elif item[4] == "out":
                year_prof[item[3]] = year_prof[item[3]] - int(item[5])
        else:
            year_prof[item[3]] = 1
    print(year_prof.items())
    
    
    
    

    


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
