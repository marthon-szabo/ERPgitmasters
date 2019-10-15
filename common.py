""" Common module
implement commonly used functions here
"""

import random


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
