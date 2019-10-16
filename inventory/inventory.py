""" Inventory module
Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""
# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    table = data_manager.get_table_from_file("inventory/inventory.csv")
    existing_id = common.id_finder(table)
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Available",
               "Average durability by manufacturers"]
    while True:
        ui.print_menu("Inventory menu", options, "Go back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove_record = ui.get_inputs(["Enter an ID: "], "")
            id_ = remove_record[0]
            if id_ in existing_id:
                remove(table, id_)
            else:
                common.clear()
                ui.print_error_message("Invalid ID!")
        elif option == "4":
            update_record = ui.get_inputs(["Enter an ID: "], "")
            id_ = update_record[0]
            if id_ in existing_id:
                update(table, id_)
            else:
                ui.print_error_message("Invalid ID!")
        elif option == "5":
            get_available_items(table, year)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            common.clear()
            break
        else:
            common.clear()
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    common.clear()
    title_list = ["ID", "Name", "Manufacturer", "Purchase year", "Durability"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    id_ = common.generate_random(table)
    list_labels = ["Name: ", "Manufacturer: ", "Purchase year: ", "Durability: "]
    title = "Please give all new data: "
    item = ui.get_inputs(list_labels, title)
    item.insert(0, id_)
    table.append(item)
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    common.clear()
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

    for line in table:
        if id_ in line:
            table.remove(line)
            data_manager.write_table_to_file("inventory/inventory.csv", table)
            common.clear()
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

    list_labels = ["Name: ", "Manufacturer: ", "Purchase year: ", "Durability: "]
    title = "Please give all new data: "
    item = ui.get_inputs(list_labels, title)
    for line in table:
        if id_ in line:
            line[1:] = item
            data_manager.write_table_to_file("inventory/inventory.csv", table)
            common.clear()
            return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """



def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
