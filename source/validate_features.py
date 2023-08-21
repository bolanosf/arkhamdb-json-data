import argparse
import json
import os
from jmespath import search
from common.optimization import runtime_function
from common.utils import load_json_file
from common.consts import (
    ENCOUNTER_SUBSET_PATH, 
    FEATURE_ENCOUNTER_DICT,
    PLAYER_SUBSET_PATH,
    FEATURE_PLAYER_DICT,
)

def verify_type(feature_dict, data):
    for key in feature_dict.keys():
        key_universe = search(f'[*].{key}',data)
        for element in key_universe:
            if type(element) != feature_dict[key]:
                print(f'{key}: {element}')

def main():
    enc_data = load_json_file(ENCOUNTER_SUBSET_PATH)
    player_data = load_json_file(PLAYER_SUBSET_PATH) 

    # Verify types
    verify_type(FEATURE_PLAYER_DICT, player_data)
    verify_type(FEATURE_ENCOUNTER_DICT, enc_data)

    print("Done")


if __name__ == "__main__":
    main()
