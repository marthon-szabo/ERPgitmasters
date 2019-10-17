""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5
FILE_LOCATION = "sales/sales.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title = "SALES"
    list_options = ["Show all game sales data",
                    "Add a new game sale",
                    "Remove a game sale",
                    "Update a game sale's data",
                    "Get ID of lowest priced item",
                    "Get sold items between dates"]
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
            remove_record = ui.get_inputs(["Enter ID of game to be deleted: "], "")
            remove_id = remove_record[ID]
            if remove_id in ids_we_have:
                table = remove(table, remove_id)
            else:
                ui.print_error_message("Invalid ID!")
        elif option == "4":
            ids_we_have = common.id_finder(table)
            update_record = ui.get_inputs(["Enter ID of game to be updated: "], "")
            update_id = update_record[ID]
            if update_id in ids_we_have:
                table = update(table, update_id)
            else:
                ui.print_error_message("Invalid ID!")
        elif option == "5":
            result = get_lowest_price_item_id(table)
            ui.print_result(result, "The ID of game with the lowest price: ")
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
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

    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
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
    list_labels = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    title = "Please enter new game sale data to database: "

    while True:
        new_item = ui.get_inputs(list_labels, title)
        new_item.insert(ID, id_)
        try:
            int(new_item[PRICE])
            int(new_item[MONTH])
            int(new_item[DAY])
            int(new_item[YEAR])
            if (
                int(new_item[PRICE]) >= 0
                and int(new_item[MONTH]) >= 1 and int(new_item[MONTH]) <= 12
                and int(new_item[DAY]) >= 1 and int(new_item[MONTH]) <= 31
                and int(new_item[YEAR]) >= 1000 and int(new_item[YEAR]) <= 3000
                ):
                table.append(new_item)
                data_manager.write_table_to_file(FILE_LOCATION, table)
                ui.print_result("Game sale added to database.", "Operation succeeded.")
                return table
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message("Invalid input: price, year, month and day must all be numbers and have valid values.")
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
            ui.print_result(f"ID {id_} no longer in database", "Game sale deletion succeeded.")
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
    list_labels = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    title = "Please give updated data of the game sale: "

    while True:
        item = ui.get_inputs(list_labels, title)
        item.insert(ID, id_)
        try:
            int(item[PRICE])
            int(item[MONTH])
            int(item[DAY])
            int(item[YEAR])
            if (
                int(item[PRICE]) >= 0
                and int(item[MONTH]) >= 1 and int(item[MONTH]) <= 12
                and int(item[DAY]) >= 1 and int(item[MONTH]) <= 31
                and int(item[YEAR]) >= 1000 and int(item[YEAR]) <= 3000
                ):
                for line in table:
                    if id_ in line:
                        line[0:] = item
                        data_manager.write_table_to_file(FILE_LOCATION, table)
                        ui.print_result(f"ID {id_} with updated data in database", "Game sale update succeeded.")
                        return table
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message("Invalid input: price, year, month and day must all be numbers and have valid values.")
            return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    price_index = 2
    id_index = 0
    title_index = 1
    id_name_and_price = {}
    prices = []
    titles_with_lowest_price = []
    for data in table:
        id_name_and_price[data[id_index]] = [data[title_index], int(data[price_index])]
        prices.append(int(data[price_index]))
    for key, val in id_name_and_price.items():
        if val[1] == min(prices):
            id_name_and_price[key] = val[0]
            titles_with_lowest_price.append(val[0])
    for key, val in id_name_and_price.items():
        if min(titles_with_lowest_price) == val:
            return key


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    items_sold_between = []
    item_year = 5
    item_month = 3
    item_day = 4

    for data in table:
        if int(data[item_month]) <= month_from and int(data[item_month]) >= month_to:
            if int(data[item_day]) >= day_from and int(data[item_day]) <= day_to:
                if int(data[item_year]) >= year_from and int(data[item_year]) <= year_to:
                    items_sold_between.append(data)
    return items_sold_between
