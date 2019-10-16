""" Common module
implement commonly used functions here
"""

import random
import os
import string

def id_finder(table):
    id = []
    for item in table:
        id.append(item[0])
    return id


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    char = string.ascii_lowercase
    sym = "[!@#$%^&*()?]"
    id_ = id_finder(table)

    while True:
        pswd = []
        for i in range(2):
            pswd.extend([random.choice(char), random.choice(char.upper()), str(random.randint(0, 9)), random.choice(sym)])
        generated = ("".join(pswd))

        if generated in id_finder(table):
            continue
        else:
            return generated


def bubble_sorting(your_list):
    n = len(your_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if your_list[j] > your_list[j+1]:
                your_list[j], your_list[j+1] = your_list[j+1], your_list[j]
    return your_list


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
