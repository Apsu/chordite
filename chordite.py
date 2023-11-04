#!/usr/bin/env python

import click

@click.command()
@click.argument("layout")
def main(layout):
    print(f"Layout specified: {layout}")

if __name__ == "__main__":
    main()
