"""
This module compares two CSV files (previous.csv and current.csv) and prints the differences.
"""

from typing import Dict, Any
from csv_diff import load_csv, compare

# Load and compare the CSV files


def compare_csv(previous_file: str, current_file: str) -> Dict[str, Any]:
    """
    Compare two CSV files and return the differences.

    Args:
        previous_file (str): The path to the previous CSV file.
        current_file (str): The path to the current CSV file.

    Returns:
        Dict[str, Any]: A dictionary containing the differences between the two CSV files.
    """
    return compare(
        load_csv(open(previous_file, encoding="utf-8"), key="name"),
        load_csv(open(current_file, encoding="utf-8"), key="name")
    )


def get_added_products(previous_file: str = "previous.csv",
                       current_file: str = "current.csv") -> str:
    """
    Print the products that were added in the current CSV file compared to the previous CSV file.

    Args:
        previous_file (str): The path to the previous CSV file. Defaults to "previous.csv".
        current_file (str): The path to the current CSV file. Defaults to "current.csv".

    Returns:
        str: A string containing the names of the added products
    """
    diff = compare_csv(previous_file, current_file)
    result = ""
    for difference in diff["added"]:
        name = difference["name"]
        result += f"+ {name}\n"
    return result


def get_removed_products(previous_file: str = "previous.csv",
                         current_file: str = "current.csv") -> str:
    """
    Print the products that were removed in the current CSV file compared to the previous CSV file.

    Args:
        previous_file (str): The path to the previous CSV file. Defaults to "previous.csv".
        current_file (str): The path to the current CSV file. Defaults to "current.csv".

    Returns:
        str: A string containing the names of the removed products
    """
    diff = compare_csv(previous_file, current_file)
    result = ""
    for difference in diff["removed"]:
        name = difference["name"]
        result += f"- {name}\n"
    return result


def get_changed_products(previous_file: str = "previous.csv",
                         current_file: str = "current.csv") -> str:
    """
    Print the products that had their prices changed in the 
    current CSV file compared to the previous CSV file.

    Args:
        previous_file (str): The path to the previous CSV file. Defaults to "previous.csv".
        current_file (str): The path to the current CSV file. Defaults to "current.csv".

    Returns:
        str: A string containing the names of the products with changed prices
    """
    diff = compare_csv(previous_file, current_file)
    result = ""
    for changed in diff["changed"]:
        name = changed["key"]
        prices = changed["changes"]["price"]
        result += f"* {name} Previous Price {prices[0]} - New Price {prices[1]}"
    return result
