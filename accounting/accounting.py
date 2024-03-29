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

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    options = ["Show accounting table",
                "Add new accounting item",
                "Remove an accounting item",
                "Update one item in the accounting table",
                "Which year has the highest profit?",
                "What is the average (per item) profit in a given year?"]
    while True:
        id_ = ""
        ui.print_menu("Accounting menu", options, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(items)
        elif option == "2":
            add(items)
        elif option == "3":
            id_ = ui.get_inputs(["Please enter an id: "], "")
            identifiers = common.id_finder(items)
            if id_[0] in identifiers:
                remove(items, id_[0])
                break
            else:
                ui.print_error_message("No such id.")
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an id: "], "")
            identifiers = common.id_finder(items)
            if id_[0] in identifiers:
                update(items, id_[0])
                break
            else:
                ui.print_error_message("No such id.")
        elif option == "5":
            which_year_max(items)
        elif option == "6":
            years_in_table = [item[3] for item in items]
            while True:
                year = ui.get_inputs(["Please enter a year: "], "")
                seek_year = year[0]
                if seek_year in years_in_table:
                    avg_amount(items, seek_year)
                    break
        elif option == "0":
            common.clear()
            break
        else:
            ui.print_error_message("There is no such option.")
            #raise KeyError("There is no such option.")
            continue

    # you code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    common.clear()
    list_labels = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(items, list_labels)

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    valid_types = ["in", "out"]
    id_ = common.generate_random(table)
    list_labels = ["month (1-12): ", "day (1-31): ", "year (1900-3000): ", "type (\"in/out\"): ", "amount: "]
    title = "Please give all new data: "
    while True:
        item = ui.get_inputs(list_labels, title)
        valid_month = item[0].isnumeric() and int(item[0]) in range(1, 13)
        valid_day = item[1].isnumeric() and int(item[1]) in range(1, 32)
        valid_year = (item[2].isnumeric() and int(item[2]) in range(1900, 3001))
        valid_type = item[3] in valid_types
        valid_amount = item[4].isnumeric()
        valid = [valid_month, valid_day, valid_year, valid_type, valid_amount]
        if all(valid):
            break
        else:
            ui.print_error_message("Please check your data.")   
    item.insert(0, id_)
    table.append(item)
    data_manager.write_table_to_file("accounting/items.csv", table)
    common.clear()
    label = ("The data have been added to the table under this id:")
    result = id_ 
    ui.print_result(result, label)

    # your code

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
            data_manager.write_table_to_file("accounting/items.csv", table)
            common.clear()
            label = ("The data under the following id have been removed from the table:")
            result = id_ 
            ui.print_result(result, label)
            return table
    ui.print_error_message("There is no such item in the list.")

    # your code

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
    valid_types = ["in", "out"]
    list_labels = ["month (1-12): ", "day (1-31): ", "year (1900-3000): ", "type (\"in/out\"): ", "amount: "]
    title = "Please give all new data: "
    while True:
        item = ui.get_inputs(list_labels, title)
        valid_month = item[0].isnumeric() and int(item[0]) in range(1, 13)
        valid_day = item[1].isnumeric() and int(item[1]) in range(1, 32)
        valid_year = item[2].isnumeric() and int(item[2]) in range(1900, 3001)
        valid_type = item[3] in valid_types
        valid_amount = item[4].isnumeric()
        valid = [valid_month, valid_day, valid_year, valid_type, valid_amount]
        if all(valid):
            break
        else:
            ui.print_error_message("Please check your data.")
    item.insert(0, id_)
    for element in table:
        if element[0] == id_:
            element[0:] = item
            data_manager.write_table_to_file("accounting/items.csv", table)
            label = ("The data under the following id have been updated:")
            result = id_ 
            ui.print_result(result, label)
            return table
    ui.print_error_message("There is no such item in the list.")

    # your code

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
    years = list(set([item[3] for item in table]))
    amounts = []
    for i in range(len(years)):
        amounts.append(0)
    
    year_prof = dict(zip(years, amounts))
    
    for item in table:
        if item[3] in year_prof:    
            if item[4] == "in":
                year_prof[item[3]] = year_prof[item[3]] + int(item[5])
            elif item[4] == "out":
                year_prof[item[3]] = year_prof[item[3]] - int(item[5])
        else:
            year_prof[item[3]] = 1
    result = int(max(year_prof, key=year_prof.get))
    label = "The following year has the highest profit:"
    ui.print_result(result, label)
    return result

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    
    amounts = []
    for item in table:
        if str(item[3]) == str(year):
            if item[4] == "in":
                amounts.append(str("+"+item[5]))
            elif item[4] == "out":
                amounts.append(str("-"+item[5]))
    for i in range(len(amounts)):
        amounts[i] = int(amounts[i])
    result_base = 0
    items_count = len(amounts)
    for amount in amounts:
        result_base += amount
    result = result_base/items_count
    label = (f"The average profit (per item) in the year {year} is:")
    ui.print_result(result, label)
    return result

    # your code
