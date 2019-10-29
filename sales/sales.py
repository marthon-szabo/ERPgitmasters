""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

SALE_ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5
CUSTOMER_ID = 6
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
                    "Get Sale ID of lowest priced item",
                    "Get sold items between dates",
                    "Get title by sale ID",
                    "Get item sale ID sold last",
                    "Get item title sold last from table",
                    "Get the sum of prices",
                    "Get customer ID by sale ID",
                    "Get all customer IDs"]
    exit_message = "Exit to main menu"
    common.clear()

    while True:
        table = data_manager.get_table_from_file(FILE_LOCATION)
        ui.print_menu(title, list_options, exit_message)
        existing_id = common.id_finder(table)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]

        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            ids_we_have = common.id_finder(table)
            remove_record = ui.get_inputs(["Enter SALE_ID of game to be deleted: "], "")
            remove_id = remove_record[SALE_ID]
            if remove_id in ids_we_have:
                table = remove(table, remove_id)
            else:
                ui.print_error_message("Invalid SALE_ID!")
        elif option == "4":
            ids_we_have = common.id_finder(table)
            update_record = ui.get_inputs(["Enter SALE_ID of game to be updated: "], "")
            update_id = update_record[SALE_ID]
            if update_id in ids_we_have:
                table = update(table, update_id)
            else:
                ui.print_error_message("Invalid SALE_ID!")
        elif option == "5":
            result = get_lowest_price_item_id(table)
            ui.print_result(result, "The SALE_ID of game with the lowest price: ")
        elif option == "6":
            get_dates = ui.get_inputs([
                                        "from month: ",
                                        "from day from: ",
                                        "from year: ",
                                        "until month: ",
                                        "until day: ",
                                        "until year: "
                                     ], "Get items sold between dates as"
                                     )
            month_from, day_from, year_from, month_to, day_to, year_to = get_dates
            result = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
            ui.print_result(
                "",
                'Items sold between ' +
                str(month_from) +
                '/' +
                str(day_from) +
                '/' +
                str(year_from) +
                '-' +
                str(month_to) +
                '/' +
                str(day_to) +
                '/' +
                str(year_to))
            for line in result:
                line[PRICE] = str(line[PRICE])
                line[YEAR] = str(line[YEAR])
                line[MONTH] = str(line[MONTH])
                line[DAY] = str(line[DAY])
            ui.print_table(result, ["SALE_ID", "Title", "Price", "Month", "Day", "Year"])
        elif option == "7":
            title_id = ui.get_inputs(["Enter a sale ID: "], "")
            id_ = title_id[0]
            if id_ in existing_id:
                get_title_by_id_from_table(id_, table)
            else:
                return None
        elif option == "8":
            get_item_id_sold_last_from_table(table)
        elif option == "9":
            get_item_title_sold_last_from_table(table)
        elif option == "10":
            item_ids = [data[0] for data in table]
            get_the_sum_of_prices_from_table(table, item_ids)
        elif option == "11":
            get_sale_id = ui.get_inputs(["Enter a sale ID: "], "")
            sale_id = get_sale_id[0]
            if sale_id in existing_id:
                get_customer_id_by_sale_id_from_table(table, sale_id)
            else:
                return None
        elif option == "12":
            get_all_customer_ids_from_table(table)
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
    title_list = ["SALE_ID", "Title", "Price", "Month", "Day", "Year", "Customer_ID"]
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
        new_item.insert(SALE_ID, id_)
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
                common.clear()
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
            common.clear()
            ui.print_result(f"SALE_ID {id_} no longer in database", "Game sale deletion succeeded.")
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
        item.insert(SALE_ID, id_)
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
                        ui.print_result(f"SALE_ID {id_} with updated data in database", "Game sale update succeeded.")
                        return table
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message("Invalid input: price, year, month and day must all be numbers and have valid values.")
            return table

    # your code

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
    # your code


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

    """
    items_sold_between = []
    for data in table:
        if int(data[YEAR]) >= year_from and int(data[YEAR]) <= year_to:
            if int(data[MONTH]) >= month_from and int(data[MONTH]) <= month_to:
                if int(data[DAY]) <= day_from and int(data[DAY]) >= day_to:
                    items_sold_between.append(data)
    return items_sold_between
    """
    while True:
        try:
            int(month_from)
            int(month_to)
            int(day_from)
            int(day_to)
            int(year_from)
            int(year_to)

            while True:
                valid_month_from = int(month_from) in range(1, 13)
                valid_month_to = int(month_to) in range(1, 13)
                valid_day_from = int(day_from) in range(1, 32)
                valid_day_to = int(day_to) in range(1, 32)
                valid_year_from = int(year_from) in range(1900, 3001)
                valid_year_to = int(year_to) in range(1900, 3001)

                valid = [valid_day_from, valid_day_to, valid_month_from, valid_month_to, valid_year_from, valid_year_to]
                if all(valid):
                    break
                else:
                    raise ValueError

            filtered_table = []

            from_date = (int(year_from), int(month_from), int(day_from))
            to_date = (int(year_to), int(month_to), int(day_to))

            for line in table:
                if from_date < (int(line[YEAR]), int(line[MONTH]), int(line[DAY])) < to_date:
                    filtered_table.append(line[:6])

            for line in filtered_table:
                line[YEAR], line[DAY], line[MONTH], line[PRICE] = int(
                    line[YEAR]), int(line[DAY]), int(line[MONTH]), int(line[PRICE])
            return filtered_table

        except ValueError:
            ui.print_error_message("Invalid input: year, month and day must all be numbers and have valid values.")
            error_table = [["invalid input", "invalid input", "invalid input",
                            "invalid input", "invalid input", "invalid input"]]
            return error_table
    # your code


# functions supports data analyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    for data in table:
        if id == data[SALE_ID]:
            return data[TITLE]


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    for data in table:
        if id == data[SALE_ID]:
            return data[TITLE]


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    all_id = []
    for data in table:
        all_id.append(data[SALE_ID])
    _id_ = all_id[0]
    return _id_


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """
    all_id = []
    for data in table:
        all_id.append(data[SALE_ID])
    _id_ = all_id[0]
    return _id_
    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """
    all_titles = []
    for data in table:
        all_titles.append(data[TITLE])
    _title_ = all_titles[-1]
    return _title_
    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    item_prices = []
    for data in table:
        item_prices.append(int(data[2]))

    ids_and_prices = dict(zip(item_ids, item_prices))
    return sum(ids_and_prices.values())


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    item_prices = []
    for data in table:
        item_prices.append(int(data[2]))

    ids_and_prices = dict(zip(item_ids, item_prices))
    return sum(ids_and_prices.values())
    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    for data in table:
        if sale_id == data[SALE_ID]:
            return data[CUSTOMER_ID]
    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """
    for data in table:
        if sale_id == data[SALE_ID]:
            return data[CUSTOMER_ID]

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """
    table = data_manager.get_table_from_file(FILE_LOCATION)
    all_customer_ids = set()
    for data in table:
        all_customer_ids.add(data[CUSTOMER_ID])
    return all_customer_ids
    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """
    all_customer_ids = set()
    for data in table:
        all_customer_ids.add(data[CUSTOMER_ID])
    return all_customer_ids
    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    num_of_sales = {}
    table = data_manager.get_table_from_file(FILE_LOCATION)
    for item in table:
        if item[CUSTOMER_ID] in num_of_sales:
            num_of_sales[item[CUSTOMER_ID]] += 1
        else:
            num_of_sales[item[CUSTOMER_ID]] = 1
    return num_of_sales


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
