#!/usr/bin/env python3
"""
A module to handle pulling stock symbol data and writing it to a file

"""
# TODO: Figure out how the hell python OOP works
# how the f*ck do I package all of this data?

__author__ = "HyPerNT"
__version__ = "0.1.0"
__license__ = "GNU GPLv3"

def getSecret():
    try:
        with open("secret.txt") as f: # I'll figure out how to securely handle API keys later
            return f.read().split('\n', 1)[0]
    except:
        print("Odds are the secret file doesn't exist. That's either my bad, "\
        "or you don't have the file, and with good reason.")


if __name__ == "__main__":
    """ You really shouldn't be executing this from the command line
    but I do, do as I say not as I do """
    exit()
