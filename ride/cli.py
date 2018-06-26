"""
    Ride
    - - - - - - - - - -

    This module implements the Ride CLI interface.

    :copyright: (c) 2018 by David Heimann.
    :license: MIT
    :author: David Heimann
"""
from cfonts import render
from click import (
    command,
    echo
)

@command()
def cli():
    """
    Uber for the command line.
    """
    echo(
        render(
            "Ride.",
            colors=['blue', 'white'],
            align='center'
        )
    )
