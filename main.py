#!/usr/bin/env python3

##
# IMPORTS
# For more information, see https://www.python.org/dev/peps/pep-0008/#imports
##
import click

from lib.pantone import Pantone
from lib.ral import RAL
from lib.dulux import Dulux
from lib.copic import Copic
from lib.prismacolor import Prismacolor


CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
)



class_map = {
    'dulux': Dulux,
    'copic': Copic,
    'prismacolor': Prismacolor,
}

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option('1.0.0-beta.1', '-v', '--version')
def cli():
    pass

@cli.command()
@click.argument('sets', nargs=-1)
@click.option('--all', 'fetch_all', flag_value=True, help='Fetch all available color sets & save as JSON.')
def fetch(sets, fetch_all):
    """
    ARGS:
    pantone | ral | dulux | copic | prismacolor
    """
    valid_sets = list(class_map.keys())

    if fetch_all == True:
        sets = valid_sets

    for set in sets:
        if set in valid_sets:
            object = class_map[set]()

            try:
                object.fetch_all()
            except AttributeError:
                object.fetch()

            object.save()
            object.create_json()
        else:
            print('"' + set + '" isn\'t available. Please provide a valid color space,\nsuch as "pantone", "ral", "dulux", "copic" & "prismacolor".')
            continue


@cli.command()
@click.argument('sets', nargs=-1)
@click.option('--all', 'process_all', flag_value=True, help='Process all available color sets & generate color palettes.')
def process(sets, process_all):
    """
    ARGS:
    pantone | ral | dulux | copic | prismacolor
    """
    valid_sets = list(class_map.keys())

    if process_all == True:
        sets = valid_sets

    for set in sets:
        if set in valid_sets:
            object = class_map[set]()
            object.make_palettes()
        else:
            print('"' + set + '" isn\'t available. Please provide a valid color space,\nsuch as "pantone", "ral", "dulux", "copic" & "prismacolor".')
            continue


if __name__ == '__main__':
    cli()
