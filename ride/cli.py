from cfonts import render
from click import (
    command,
    echo
)

@command()
def cli():
    echo(
        render(
            "Ride.",
            colors=['blue', 'white'],
            align='center'
        )
    )