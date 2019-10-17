""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
MANUFACTURER = 2
PRICE = 3
IN_STOCK = 4
FILE_LOCATION = "store/games.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title = "Store"
    list_options = ["Show all game and data",
                    "Add a new game",
                    "Remove a game",
                    "Update a game's data",
                    "How many different kinds of game are available of each manufacturer",
                    "Get average amount of games by a manufacturer"]
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
            counts = get_counts_by_manufacturers(table)
            ui.print_result("Manufacturers have the following amount of games", "")
            ui.print_result(counts, ["Manufacturers", "Number of games"])
        elif option == "6":
            manufacturers_we_have = common.manufacturer_finder(table)
            get_manufacturer = ui.get_inputs(["Enter name of Manufacturer to be checked: "], "")
            manufacturer_name = get_manufacturer[0]
            if manufacturer_name in manufacturers_we_have:
                result = get_average_by_manufacturer(table, manufacturer_name)
                ui.print_result(result, f"Average amount of stock by {manufacturer_name}:")
            else:
                ui.print_error_message("Invalid ID!")
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

    title_list = ["ID", "Title", "Manufacturer", "Price", "Number in stock"]
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
    list_labels = ["Game title: ", "Manufacturer: ", "Price: ", "Number in stock: "]
    title = "Please enter new customer data to CRM database: "

    while True:
        new_item = ui.get_inputs(list_labels, title)
        new_item.insert(ID, id_)
        try:
            int(new_item[PRICE])
            int(new_item[IN_STOCK])
            table.append(new_item)
            data_manager.write_table_to_file(FILE_LOCATION, table)
            ui.print_result("Game added to database.", "Operation succeeded.")
            return table
        except ValueError:
            ui.print_error_message("Invalid input: price and stock must be a number.")
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
    for line in table:
        if id_ in line:
            table.remove(line)
            data_manager.write_table_to_file(FILE_LOCATION, table)
            ui.print_result(f"ID {id_} no longer in database", "Game deletion succeeded.")
            return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    list_labels = ["Game title: ", "Manufacturer: ", "Price: ", "Number in stock: "]
    title = "Please give updated data of the game: "

    while True:
        item = ui.get_inputs(list_labels, title)
        item.insert(ID, id_)
        try:
            int(item[PRICE])
            int(item[IN_STOCK])
            for line in table:
                if id_ in line:
                    line[0:] = item
                    data_manager.write_table_to_file(FILE_LOCATION, table)
                    ui.print_result(f"ID {id_} with updated data in database", "Game update succeeded.")
                    return table
        except ValueError:
            ui.print_error_message("Invalid input: price and stock must be a number.")
            return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    counts_by_man = {}
    for line in table:
        if line[MANUFACTURER] in counts_by_man.keys():
            counts_by_man[line[MANUFACTURER]] += 1
        else:
            counts_by_man[line[MANUFACTURER]] = 1

    return counts_by_man
    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    total_stock_amount = 0
    number_of_titles = 0
    for line in table:
        if line[MANUFACTURER] == manufacturer:
            total_stock_amount += int(line[IN_STOCK])
            number_of_titles += 1

    return total_stock_amount / number_of_titles
    # your code
