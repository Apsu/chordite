#!/usr/bin/env python

import click
import analyzer

import os
import pathlib

@click.command()
@click.argument("layout")
def main(layout):
    layout_path = pathlib.Path(f"layouts/{layout}")
    if not layout_path.exists():
        print(f"layouts/{layout} not found")
        return -1

    analyzer.analyze(layout_path)

if __name__ == "__main__":
    main()
