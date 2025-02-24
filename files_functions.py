"""
This module provides functions to compare two CSV files and print the differences.
"""

from csv_diff import load_csv, compare


def compare_csv(previous_file, current_file):
    """
    Compares two CSV files and returns the differences.

    Args:
        previous_file (str): The path to the previous CSV file.
        current_file (str): The path to the current CSV file.

    Returns:
        dict: A dictionary containing the differences between the two CSV files.
    """
    return compare(
        load_csv(open(previous_file, encoding="utf-8"), key="Name"),
        load_csv(open(current_file, encoding="utf-8"), key="Name")
    )


def get_added_products():
    """
    Prints the products added in the current CSV file compared to the previous CSV file.
    """
    diff = compare_csv("yesterday.csv", "today.csv")
    for difference in diff['added']:
        name = difference['Name']
        print(f'+ {name}')


def get_removed_products():
    """
    Prints the products removed in the current CSV file compared to the previous CSV file.
    """
    diff = compare_csv("yesterday.csv", "today.csv")
    for difference in diff['removed']:
        name = difference['Name']
        print(f'- {name}')


def get_changed_products():
    """
    Prints the products that have changed in the current CSV file compared to the previous CSV file,
    along with their price differences.
    """
    diff = compare_csv("yesterday.csv", "today.csv")
    for changed in diff['changed']:
        name = changed['key']
        prices = changed['changes']['price']
        print(f'* {name} Previous Price {prices[0]}- New Price {prices[1]}')
