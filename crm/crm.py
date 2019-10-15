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



def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    title = "Customer Relationship Management (CRM)"
    list_options = ["Show table",
                    "Add new item",
                    "Remove a record",
                    "Update record",
                    "Get longest name ID",
                    "Get e-mail subscribers"]
    exit_message = "Exit to main menu"
    table = data_manager.get_table_from_file("crm/customers.csv")

    while True:
        ui.print_menu(title, list_options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            table = remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            get_longest_name_id(table)
        elif option == "6":
            get_subscribed_emails(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "name", "e-mail", "subscribed"]
    ui.print_table(table, title_list)

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    id_ = common.generate_random(table)
    list_labels = ["name", "e-mail", "subscribed"]
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

    # your code
    for index in range(len(table)):
        if table[index][0] == id_:
            table.pop(index)
        data_manager.write_table_to_file('crm/customers.csv', table)

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

    # your code

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
            ui.print_result(lines[ID], "The ID of the customer with the longest name.")
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
    subscribers_to_print = {line[NAME]: line[EMAIL] for line in table if line[SUBSCRIBED] == "1"}

    # subscribers_to_print = [item for item in subscribers]

    # reconsider list format based on output by ui.py => revise f"" format
    ui.print_result(subscribers_to_print,
                    "The following people subsribed to the newsletter with the following e-mail addresses")

    return subscribers
