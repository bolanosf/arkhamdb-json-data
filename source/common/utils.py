import argparse
import json
import os
from subsets.utils import verbose_print, format_json


#### LOAD JSON ####
def load_json_file(path):
    global formatting_errors
    global validation_errors
    try:
        with open(path, "rb") as data_file:
            bin_data = data_file.read()
        raw_data = bin_data.decode("utf-8")
        json_data = json.loads(raw_data)
    except ValueError as e:
        validation_errors += 1
        return None

    formatted_raw_data = format_json(json_data)

    if "<sup>" in formatted_raw_data:
        validation_errors += 1
        return None

    return json_data


#### GET UNIQUE KEYS FROM DICT ###
def get_keys(list_of_dict):
    unique_keys = set()
    print(len(list_of_dict))
    for dicts in list_of_dict:
        unique_keys.update(set(dicts.keys()))
    return unique_keys
