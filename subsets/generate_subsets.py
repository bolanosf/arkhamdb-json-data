import argparse
import json
import jsonschema
import os
import sys
import re
from utils import check_dir_access, verbose_print, format_json, check_file_access


PACK_DIR="pack"
SCHEMA_DIR="schema"
formatting_errors = 0
validation_errors = 0

#### LOAD JSON ####
def load_json_file(args, path):
    global formatting_errors
    global validation_errors
    try:
        with open(path, "rb") as data_file:
            bin_data = data_file.read()
        raw_data = bin_data.decode("utf-8")
        json_data = json.loads(raw_data)
    except ValueError as e:
        verbose_print(args, "%s: File is not valid JSON.\n" % path, 0)
        validation_errors += 1
        verbose_print(args, "%s\n" % e.message, 0)
        return None

    verbose_print(args, "%s: Checking JSON formatting...\n" % path, 1)
    formatted_raw_data = format_json(json_data)

    if "<sup>" in formatted_raw_data:
        verbose_print(args, "%s: File contains invalid content (<sup>)\n" % path, 0)
        validation_errors += 1
        return None

    if formatted_raw_data != raw_data:
        ##verbose_print(args, "%s: File is not correctly formatted JSON.\n" % path, 0)
        formatting_errors += 0
        if args.fix_formatting and len(formatted_raw_data) > 0:
            verbose_print(args, "%s: Fixing JSON formatting...\n" % path, 0)
            try:
                with open(path, "wb") as json_file:
                    bin_formatted_data = formatted_raw_data.encode("utf-8")
                    json_file.write(bin_formatted_data)
            except IOError as e:
                verbose_print(args, "%s: Cannot open file to write.\n" % path, 0)
                print(e)
    return json_data

#### COMMAND LINE ARGS ####
def parse_commandline():
    argparser = argparse.ArgumentParser(description="Validate JSON in the netrunner cards repository.")
    argparser.add_argument("-f", "--fix_formatting", default=False, action="store_true", help="write suggested formatting changes to files")
    argparser.add_argument("-v", "--verbose", default=0, action="count", help="verbose mode")
    argparser.add_argument("-b", "--base_path", default=os.getcwd(), help="root directory of JSON repo (default: current directory)")
    argparser.add_argument("-p", "--pack_path", default=None, help=("pack directory of JSON repo (default: BASE_PATH/%s/)" % PACK_DIR))
    argparser.add_argument("-c", "--schema_path", default=None, help=("schema directory of JSON repo (default: BASE_PATH/%s/" % SCHEMA_DIR))
    args = argparser.parse_args()

    # Set all the necessary paths and check if they exist
    if getattr(args, "schema_path", None) is None:
        setattr(args, "schema_path", os.path.join(args.base_path,SCHEMA_DIR))
    if getattr(args, "pack_path", None) is None:
        setattr(args, "pack_path", os.path.join(args.base_path,PACK_DIR))
    check_dir_access(args.base_path)
    check_dir_access(args.schema_path)
    check_dir_access(args.pack_path)

    return args

#### LOAD METADATA ####
def load_cycles(args):
    verbose_print(args, "Loading cycle index file...\n", 1)
    cycles_path = os.path.join(args.base_path, "cycles.json")
    cycles_data = load_json_file(args, cycles_path)

    return cycles_data

def load_packs(args, cycles_data):
    verbose_print(args, "Loading pack index file...\n", 1)
    packs_path = os.path.join(args.base_path, "packs.json")
    packs_data = load_json_file(args, packs_path)

    for p in packs_data:
        if p["cycle_code"] == "promotional":
            p["cycle_code"] = "promo"
        pack_filename = "{}.json".format(p["code"])
        pack_path = os.path.join(args.pack_path, p["cycle_code"], pack_filename)
        p['player'] = check_file_access(pack_path)
        pack_filename = "{}_encounter.json".format(p["code"])
        pack_path = os.path.join(args.pack_path, p["cycle_code"], pack_filename)
        p['encounter'] = check_file_access(pack_path)

    return packs_data

def load_factions(args):
    verbose_print(args, "Loading faction index file...\n", 1)
    factions_path = os.path.join(args.base_path, "factions.json")
    factions_data = load_json_file(args, factions_path)

    return factions_data

def load_types(args):
    verbose_print(args, "Loading type index file...\n", 1)
    types_path = os.path.join(args.base_path, "types.json")
    types_data = load_json_file(args, types_path)

    return types_data

def load_sides(args):
    verbose_print(args, "Loading side index file...\n", 1)
    sides_path = os.path.join(args.base_path, "sides.json")
    sides_data = load_json_file(args, sides_path)

    return sides_data


# Parse Subset Paths
def parse_subset_filepaths(args):
    verbose_print(args, "Loading pack index file...\n", 1)
    packs_path = os.path.join(args.base_path, "packs.json")
    packs_data = load_json_file(args, packs_path)

    player_json_paths = []
    encounter_json_paths = []

    for p in packs_data:
        # reformat cycle code to match dir
        if p["cycle_code"] == "side_stories":
            p["cycle_code"] = "side"
        elif p["cycle_code"] == "promotional":
            p["cycle_code"] = "promo"

        # Special Encounter Tags
        if p["code"] in ["eoec","tskc"]:
            pack_filename = "{}.json".format(p["code"])
            pack_path = os.path.join(args.pack_path, p["cycle_code"], pack_filename)
            encounter_json_paths.append(pack_path)
            continue

        # Encounter Cards
        pack_filename = "{}_encounter.json".format(p["code"])
        pack_path = os.path.join(args.pack_path, p["cycle_code"], pack_filename)
        if check_file_access(pack_path):
            encounter_json_paths.append(pack_path)
            if p["cycle_code"] in ["side"]:
                continue

        # Player Cards
        pack_filename = "{}.json".format(p["code"])
        pack_path = os.path.join(args.pack_path, p["cycle_code"], pack_filename)
        player_json_paths.append(pack_path)

    return player_json_paths, encounter_json_paths

def merge_JsonFiles(path_list, filename):
    result = list()
    for f1 in path_list:
        print(f1)
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open(filename, 'w') as output_file:
        json.dump(result, output_file)

def main():
    args = parse_commandline()
    player_paths, encounters_paths = parse_subset_filepaths(args)
    merge_JsonFiles(player_paths, "subsets/player_subset.json")
    merge_JsonFiles(encounters_paths, "subsets/encounter_subset.json")

if __name__ == "__main__":
    main()
