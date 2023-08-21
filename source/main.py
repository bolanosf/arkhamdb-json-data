import argparse
import json
import os
from common.optimization import runtime_function
from common.utils import load_json_file
from common.consts import (
    BASE_PATH, 
    ENCOUNTER_SUBSET_PATH, 
    PLAYER_SUBSET_PATH 
)

def main():
    runtime_function("load encounter subset", load_json_file, {"path": PLAYER_SUBSET_PATH})
    load_json_file(ENCOUNTER_SUBSET_PATH)

if __name__ == "__main__":
    main()

