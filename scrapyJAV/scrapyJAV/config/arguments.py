# -*- coding: utf-8 -*-
"""
File: arguments
Description: 
Author: mikeshinoda
Date: 2024/1/19
"""

# TODO: Add your code here
import yaml
import os


def get_config(key):
    """
    Get specified configuration value by passing key

    Args:
        key (str): the key of value

    Returns:
        value (str): the value of the specified key
    """
    with open(os.path.join(os.getcwd(), "config.yaml"), "r") as f:
        data = yaml.safe_load(f)
    return data[key]
