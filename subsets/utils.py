import json
import jsonschema
import os
import sys
import re

def verbose_print(args, text, minimum_verbosity=0):
    if args.verbose >= minimum_verbosity:
        sys.stdout.write(text)

def check_dir_access(path):
    if not os.path.isdir(path):
        sys.exit("%s is not a valid path" % path)
    elif os.access(path, os.R_OK):
        return
    else:
        sys.exit("%s is not a readable directory")

def check_file_access(path):
    if not os.path.isfile(path):
        return False;
    elif os.access(path, os.R_OK):
        return True
    else:
        return False

def format_json(json_data):
    formatted_data = json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    formatted_data = formatted_data.replace(u"\u2018", "'").replace(u"\u2019", "'")
    formatted_data = formatted_data.replace(u"\u2212", "-").replace(u"\u2013", "-")
    formatted_data = formatted_data.replace("\\r\\n", "\\n").replace(" \\n", "\\n")
    formatted_data = formatted_data.replace("][", "] [")
    for i in range(8, 0, -1):
         formatted_data = re.sub("^" + ("    " * i), "\t" * i, formatted_data, flags=re.MULTILINE)
    formatted_data += "\n"
    return formatted_data