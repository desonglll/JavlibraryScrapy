# -*- coding: utf-8 -*-
"""
File: guide_info
Description: 
Author: mikeshinoda
Date: 2024/2/18
"""

# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here
from rich import print


def print_all():
    print('''
    [bold blue]Run `python run.py -d init` for init database.[/bold blue]
    [bold blue]Run `python run.py -d delete` for [bold red]deleting[/bold red] database.[/bold blue]
    
    [bold green]Run `python run.py -c start` for crawling.[/bold green]
''')
