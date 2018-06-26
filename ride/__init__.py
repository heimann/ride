#     ____  _     __
#    / __ \(_)___/ /__
#   / /_/ / / __  / _ \
#  / _, _/ / /_/ /  __/
# /_/ |_/_/\__,_/\___/
#
"""
    Ride
    - - - - - - - - - -

    Ride is an application to interface with the Uber API from the command line.

    :copyright: (c) 2018 by David Heimann.
    :license: MIT
    :author: David Heimann
"""
from .cli import cli

if __name__ == '__main__':
    cli()
