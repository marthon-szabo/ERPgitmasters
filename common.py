""" Common module
implement commonly used functions here
"""

import random
import os


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

    generated = ''
    pswd = []

    char = r"qwertzuiopasdfghjklyxcvbnm"
    sym = r"[!@#$%^&*()?]"

    for i in range(2, 4):
        pswd.append(random.choice(char))
        pswd.append(random.choice(char.upper()))
        pswd.append(str(random.randint(0, 99)))
        pswd.append(random.choice(sym))

    random.shuffle(pswd)

    generated = ("".join(pswd))[:8]
    
    return generated


def bubble_sort(your_list):
    n = len(your_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if your_list[j] > your_list[j+1]:
                your_list[j], your_list[j+1] = your_list[j+1], your_list[j]
    return your_list


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
