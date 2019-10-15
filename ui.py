""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code

    columns = []
    column_num = 0
    length = []
    
    for number in range(len(title_list)):
        columns.append([])
        for row in table:
            columns[column_num].append(row[column_num])
        column_num += 1
    
    for item in columns:
        for k, item in enumerate(sorted(item, key=len, reverse=True)):
            if k == 0:
                length.append(len(item))

    start_header = "/"
    end_header = "\\"
    separator = "|"
    divisor_line = "-"
    padding = 2
    sum = 0

    for element in length:
        sum += element

    def print_separator(length):
        print(separator, end="")
        for i, element in enumerate(length):
            print(f"{divisor_line * (length[i] + len(str(padding)) + 1)}", end="")
            print(separator, end="")
        print()

    # HEADER
    print((start_header)
        + (divisor_line * (sum + (padding * len(length)) + (len(separator) * len(length)) - 1))
        + (end_header))

    # TITLES
    print(separator, end="")
    for i, element in enumerate(title_list):
        print(f"{element.center(length[i] + padding)}", end="")
        print(separator, end="")
    print()


    # Separator
    for lines in table:
        print_separator(length)

        print(separator, end="")
        for i, element in enumerate(lines):
            print(f"{element.center(length[i] + padding)}", end="")
            print(separator, end="")
        print()

    # FOOTER
    print((end_header)
        + (divisor_line * (sum + (padding * len(length)) + (len(separator) * len(length)) - 1))
        + (start_header))


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(label)
    if type(result) is list:
        for line in result:
            print(line)
    elif type(result) is dict:
        for k, v in result.items():
            print(f"{k}: {v}")
    else:
        print(result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    print()
    print()
    for i in range(len(list_options)):
        print("{}. {}".format(i+1, list_options[i]))
    print("0. {}".format(exit_message))
    
    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
