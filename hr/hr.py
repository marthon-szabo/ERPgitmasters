""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""
import datetime
# everything you'll need is imported:
# User interface module
import ui

# data manager module
import data_manager
# common module
import common

items = data_manager.get_table_from_file("hr/persons.csv")
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
                    "Get oldest",
                    "Get average"]
    while True:
            

        ui.print_menu("Human resorces", options, "Main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(items)
        elif option == "2":
            add(items)
        elif option == "3":
            id_ = ui.get_inputs(["Write the id: "], "")
            remove(items, id_)
        elif option == "4":
            id_ = ui.get_inputs(["Write the id: "], "")
            update(items, id_)
        elif option == "5":
            get_oldest_person(items)
        elif option == "6":
            get_persons_closest_to_average(items)
        elif option == "0":
            break
        else:
            #raise KeyError("There is no such option.")
            continue
        
def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    
    print(table)    
    
    
    
        



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    
    new_record = []
    new_record.append(input("Type here the name of the person: "))
    new_record.append(int(input("Type here the person's birth date: ")))
    table.append(new_record)
   

    data_manager.write_table_to_file("hr/persons.csv", table)  
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
    for elem in table:
        for i in elem:
            if id_ in i:
                table.remove(elem)
    data_manager.write_table_to_file("hr/persons.csv", table)  
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
    user_input = input("WHat do you want to change (Name / Date of Birth)? ").lower()
    
    if user_input == "name":
        for elem in table:
            if id_ in elem[0]:
                user_text_new = input(f"Previous name: {elem[1]}.\n\nNew name: ")
                elem[1] = user_text_new
    elif user_input == "date of birth":
        for elem in table:
            if id_ in elem[0]:
                user_text_new = input(f"Previous Date of Birth: {elem[2]}.\n\nNew Date of Birth: ")
                elem[2] = user_text_new 
    data_manager.write_table_to_file("hr/persons.csv", table)  
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    unsorted_list = len(table)
    for i in range(unsorted_list):
        for j in range(0, unsorted_list-i-1):
            if table[j][2] > table[j+1][2]:
                table[j], table[j+1] = table[j+1], table[j]
    names = []
    names.append(table[0][1])
    for elem in table:
        for i in range(0, len(elem)):
            if table[i][2] == table[i + 1][2]:
                names.append(table[i + 1][1])
    names = list(set(names))
   
    return names
    ######

def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    current_date = 2019
    #current_date = [[date] for date in str(datetime.datetime.now())
    people = table
    list_for_key = []
    list_for_value = []    
    for elem in people:
        #for i in range(0, len(elem)):
        ages_key = elem[1]
        ages_value = int(current_date) - int(elem[2])
        list_for_key.append(ages_key)
        list_for_value.append(ages_value)
    names_with_ages = {key: value for (key, value) in zip(list_for_key, list_for_value)}
    
    sum_of_ages = 0
    for value in names_with_ages.values():
        sum_of_ages += value
    average = sum_of_ages // len(names_with_ages.values())
    counter = 0
    closest_to_average = {key: average - value for key, value in zip(list_for_key, list_for_value)}
    for key, value in closest_to_average.items():
        if value < 0:
            closest_to_average[key] = value * (-1)
         
    closest_to_average_list = [[key, value] for key, value in closest_to_average.items()]
    
    unsorted_list = len(closest_to_average_list)
    for i in range(unsorted_list):
        for j in range(0, unsorted_list-i-1):
            if closest_to_average_list[j][1] > closest_to_average_list[j+1][1]:
                closest_to_average_list[j], closest_to_average_list[j+1] = closest_to_average_list[j+1], closest_to_average_list[j]
    
    names = []
    names.append(closest_to_average_list[0][0])
    for i in range(0, len(closest_to_average_list)):
        if closest_to_average_list[i][1] == closest_to_average_list[0][1]:
            names.append(closest_to_average_list[i][0])
        #for i in range(0, len(elem)):
        #    if elem[]
    final = list(set(names))
    
    return final




    
        
  
