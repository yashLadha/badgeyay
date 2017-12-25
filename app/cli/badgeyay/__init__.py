"""
Main Source Code for the library : badgeyay
Organisation : FOSSASIA
Author : @yashLadha
"""

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.version_option(version='1.0.0')
@click.command()
@click.option('--img', '-i', default='', help='Path to the svg for background')
@click.option('--font', '-f', default='Ubuntu', help='Font name to be used')
@click.option('--config', '-c', default='', help='Configuration to be used')
@click.option('--names', '-n', default='', help='Path to the file containing'
              'names (must be csv).')
@click.option('--custom_color', '-cust', default='', help='Choose custom colour'
              'for the background')
def main(img, font, config, names, custom_color):
    """
    CLI application for badge generation.
    An open source alternative for generating awesome badges
    for your awesome Organisation created by FOSSASIA.
    """
    pass
