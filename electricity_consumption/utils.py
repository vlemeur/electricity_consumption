"""This module provides code to perform generic transformation
"""
from pathlib import Path


def get_variables_from_mk_file(path_mk_file: Path) -> dict:
    """Creates a Python dict with variables names as key and variable
    values as values from a Mk config file path


    Parameters
    ----------
    path_mk_file : Path
        Path to 'Mk' file containing variables names and values
    Returns
    -------
    dict
        Python dict with variables names as key and variable
    values as values
    """
    with open(path_mk_file, "r", encoding="utf8") as file:
        lines = file.readlines()
    dict_variables = {}
    for line in lines:
        name, value = line.split(" := ")
        dict_variables[name] = value.replace("\n", "").replace('"', "")
    return dict_variables
