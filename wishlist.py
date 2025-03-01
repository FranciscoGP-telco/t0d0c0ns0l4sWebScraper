"""
This module provides functions to manage a wishlist stored in a CSV file.
It includes functionality to create the wishlist file, add products to the wishlist,
remove products from the wishlist, and delete the wishlist file.
"""

import csv
import os

WISHLIST_FILE = "wishlist.csv"


def create_wishlist_file() -> None:
    """
    Create the wishlist file if it does not exist.

    This function creates a new CSV file named 'wishlist.csv' with a header row
    containing the column name 'name' if the file does not already exist.
    """
    if not os.path.isfile(WISHLIST_FILE):
        with open(WISHLIST_FILE, 'w', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["name"])


def add_product_to_wishlist(name: str) -> None:
    """
    Add a product to the wishlist.

    Args:
        name (str): The name of the product to add to the wishlist.

    This function appends a new row with the product name to the 'wishlist.csv' file.
    If the file does not exist, it creates the file first.
    """
    create_wishlist_file()
    with open(WISHLIST_FILE, 'a', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";", lineterminator="\n")
        writer.writerow([name])


def remove_product_from_wishlist(name: str) -> None:
    """
    Remove a product from the wishlist.

    Args:
        name (str): The name of the product to remove from the wishlist.

    This function reads the 'wishlist.csv' file, removes the row with the specified
    product name, and writes the remaining rows back to the file.
    """
    if not os.path.isfile(WISHLIST_FILE):
        return
    with open(WISHLIST_FILE, 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        lines = list(reader)
    with open(WISHLIST_FILE, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";", lineterminator="\n")
        for line in lines:
            if line[0] != name:
                writer.writerow(line)


def reset_wishlist() -> None:
    """
    Remove the wishlist file.

    This function deletes the 'wishlist.csv' file if it exists.
    """
    if os.path.isfile(WISHLIST_FILE):
        os.remove(WISHLIST_FILE)
