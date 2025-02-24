"""
This module compares two CSV files (yesterday.csv and today.csv) and prints the differences.
"""

from csv_diff import load_csv, compare

# Load and compare the CSV files
def compare_csv(previous_file, current_file):
    return compare(
        load_csv(open(previous_file, encoding="utf-8"), key="Name"),
        load_csv(open(current_file, encoding="utf-8"), key="Name")
    )

def get_added_products():
    diff = compare_csv("yesterday.csv", "today.csv")
    for difference in diff['added']:
        name = difference['Name']
        print(f'+ {name}')
        
def get_removed_products(diff):
    diff = compare_csv("yesterday.csv", "today.csv")
    for difference in diff['removed']:
        name = difference['Name']
        print(f'- {name}')

def get_changed_products(diff):
    diff = compare_csv("yesterday.csv", "today.csv")
    for changed in diff['changed']:
        name = changed['key']
        prices = changed['changes']['price']
        print(f'* {name} Previous Price {prices[0]}- New Price {prices[1]}')
