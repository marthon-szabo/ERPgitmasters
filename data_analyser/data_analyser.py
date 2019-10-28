"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    title = "DATA ANALYSER"
    list_options = ["Last buyer's name",
                    "Last buyer's ID"]
    exit_message = "Exit to main menu"
    while True:
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]

        if option == "1":
            common.clear()
            get_the_last_buyer_name()

        elif option == "2":
            common.clear()
            get_the_last_buyer_id()

        elif option == "0":
            common.clear()
            break


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    pass


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    sale_id = sales.get_item_id_sold_last()
    last_buyer_id = sales.get_customer_id_by_sale_id(sale_id)
    return last_buyer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
