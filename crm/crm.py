""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
NAME = 1
EMAIL = 2
SUBSCRIBED = 3
FILE_LOCATION = "crm/customers.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    title = "Customer Relationship Management (CRM)"
    list_options = ["Show all customers and data",
                    "Add a new customer",
                    "Remove a customer",
                    "Update a customer's data",
                    "Get ID of the customer with the longest name",
                    "Get e-mail subscriber customers",
                    "Get name by ID",
                    "Get name by ID from table"]
    exit_message = "Exit to main menu"

    while True:
        table = data_manager.get_table_from_file(FILE_LOCATION)
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]

        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            ids_we_have = common.id_finder(table)
            remove_record = ui.get_inputs(["Enter ID of customer to be deleted: "], "")
            remove_id = remove_record[ID]
            if remove_id in ids_we_have:
                table = remove(table, remove_id)
            else:
                ui.print_error_message("Invalid ID!")
        elif option == "4":
            ids_we_have = common.id_finder(table)
            update_record = ui.get_inputs(["Enter ID of customer to be updated: "], "")
            update_id = update_record[ID]
            if update_id in ids_we_have:
                table = update(table, update_id)
            else:
                ui.print_error_message("Invalid ID!")
        elif option == "5":
            result = get_longest_name_id(table)
            ui.print_result(result, "The ID of the customer with the longest name.")
        elif option == "6":
            subscribers = get_subscribed_emails(table)
            subscribers_to_print = {}
            for item in subscribers:
                name, email = item.split(";")
                subscribers_to_print[email] = name
            ui.print_result("", "The following people subsribed to the newsletter with the following e-mail addresses")
            ui.print_result(subscribers_to_print, ["Name", "E-mail address"])
        # elif options == "7":
        #     id_to_get = ui.get_inputs(["Enter ID to get the name: "], "")
        #     result = get_name_by_id(id_to_get)
        #     ui.print_result(result, "The name of the customer.")
        # elif option == "8":
        #     id_to_get = ui.get_inputs(["Enter ID to get the name: "], "")
        #     result = get_name_by_id_from_table(table, id_to_get)
        #     ui.print_result(str(result), "The name of the customer.")

        elif option == "0":
            common.clear()
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    common.clear()
    title_list = ["ID", "name", "e-mail", "subscribed"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    common.clear()
    id_ = common.generate_random(table)
    list_labels = ["Customer name: ", "E-mail address: ", "Subscribed (enter 1 to if yes, 0 if not): "]
    title = "Please enter new customer data to CRM database: "
    while True:
        new_item = ui.get_inputs(list_labels, title)
        new_item.insert(ID, id_)
        if new_item[SUBSCRIBED] == "1" or new_item[SUBSCRIBED] == "0":
            table.append(new_item)
            data_manager.write_table_to_file(FILE_LOCATION, table)
            common.clear()
            ui.print_result("Customer added to database.", "Operation succeeded.")
            return table
        else:
            ui.print_error_message("Invalid input: 'subsribed' data must be '0' or '1'.")
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
            data_manager.write_table_to_file(FILE_LOCATION, table)
            common.clear()
            ui.print_result("ID no longer in database", "Customer deletion succeeded.")
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

    list_labels = ["Customer name: ", "E-mail address: ", "Subscribed (enter 1 to if yes, 0 if not): "]
    title = "Please give updated data of the customer: "

    while True:
        item = ui.get_inputs(list_labels, title)
        item.insert(ID, id_)
        if item[SUBSCRIBED] == "1" or item[SUBSCRIBED] == "0":
            for line in table:
                if id_ in line:
                    line[0:] = item
                    data_manager.write_table_to_file(FILE_LOCATION, table)
                    ui.print_result("ID with updated data in database", "Customer update succeeded.")
                    return table
        else:
            ui.print_error_message("Invalid input: 'subsribed' data must be '0' or '1'.")
            return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    len_of_names = [len(lines[NAME]) for lines in table]
    longest_names = [lines[NAME] for lines in table if len(lines[NAME]) == max(len_of_names)]

    for lines in table:
        if lines[NAME] == max(longest_names):
            return lines[ID]


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    separator = ";"
    subscribers = [f"{line[EMAIL]}{separator}{line[NAME]}" for line in table if line[SUBSCRIBED] == "1"]

    return subscribers



# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    return get_name_by_id_from_table(table, id)


def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    for line in table:
        if line[ID] == id:
            return line[NAME]
