"""
Created on Thu Jan 16 05:59:17 2025

@author: Jas-20

"""

"""
CMSC 14200, Winter 2025
Homework #1, Task #1

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def merge_dictionaries(dicts: list[dict[str, int]]) -> dict[str, int]:
    """
    Merge a list of dictionaries into a single dictionary,
    where each key maps to the sum of the values of that
    key in the provided dictionaries.

    Args:
        dicts: A list of dictionaries to merge.

    Returns: Merged dictionary
    """
    merged_dict: dict[str, int] = {} #blank dictionary to store
    # loop through each dictionary in the list
    for sub_dict in dicts:
        for key, value in sub_dict.items():  
            # Add the value to merged_dict if it doesn't exist
            if key in merged_dict:                
                merged_dict[key] += value
            else:
                merged_dict[key] =0

    return merged_dict
