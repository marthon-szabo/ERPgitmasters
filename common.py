""" Common module
implement commonly used functions here
"""

import random
import string
import os


def id_finder(table):
    id = []
    for item in table:
        id.append(item[0])
    return id


def manufacturer_finder(table):
    manufacturers = []
    for item in table:
        manufacturers.append(item[2])
    return manufacturers


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

    while True:
        pswd = []
        for i in range(2):
            pswd.extend(
                        [
                            random.choice(char),
                            random.choice(char.upper()),
                            str(random.randint(0, 9)),
                            random.choice(sym)
                        ]
                        )
        random.shuffle(pswd)
        generated = ("".join(pswd))

        if generated in id_finder(table):
            continue
        else:
            return generated


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_avrg(your_list):
    n = len(your_list)
    x = 0
    for i in your_list:
        x += i
    return x/n

    generated = ''

    # your code

    return generated
