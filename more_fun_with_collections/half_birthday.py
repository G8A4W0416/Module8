"""
Program half_birthday.py

Author: Greg Wilhelm

Last date modified: 3/19/2020

The purpose of this program is to get the date of the birthday and return the date six months later.

"""

from datetime import timedelta


def half_birthday(date_of_birthday):
    six_months_later = date_of_birthday + timedelta(days=182)
    return str(six_months_later)
