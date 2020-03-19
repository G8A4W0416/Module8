"""
Program assign_average.py

Author: Greg Wilhelm

Last date modified: 3/18/2020

The purpose of this program is to lookup the least average score for a grade using a switch/case implemented by a
function and the dictionary collection.

"""


def switch_average(grade):
    switcher = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
    }
    # Second parameter acts as our default
    average = switcher.get(grade, "Invalid Grade")
    return average
