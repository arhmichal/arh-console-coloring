#!/usr/bin/env python3

import re

def load_scheme(scheme_name):
    schema = []

    import os
    this_file_dir_path = os.path.dirname(os.path.realpath(__file__))
    schema_path = f"{this_file_dir_path}/schemas/{scheme_name}.py"
    if (not os.path.isfile(schema_path)):
        raise Exception(f"Sorry, no file {schema_path}")
        # TODO log error and exit

    schema_import = f"schemas.{scheme_name}"
    import importlib
    module = importlib.import_module(schema_import)

    schema = module.scheme
    return schema

def apply_schema(line, schema):
    new_line = line
    num_of_replaces = 0
    for rule in schema:
        (_, pattern), (_, replace), (_, final) = rule.items()
        new_line, num_of_replaces = re.subn(pattern, replace, new_line)
        if (final and num_of_replaces > 0):
            break
    return new_line

def process(content, schema):
    line = ""
    while True:
        line = content.readline()
        if not line:
            break
        output_line = apply_schema(line, schema)
        print(output_line)

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        prog="colorme",
        description="Offers an extensive stdin/file-content replace mechanism"'\n'
                    "using a python file with replace rules"'\n'
                    "for the main purpose of colloring console output.",
    )
    parser.add_argument("-s", "--schema", required=True,
                        help="name of a *.py file but without '.py' extension that contains schema definition")
    parser.add_argument("-v", "--verbose", default=False, action="store_true")
    parser.add_argument("filename", nargs="?", help="file name/path to read as input")

    return parser.parse_args()

def main():
    import sys
    args = parse_args()
    schema = load_scheme(args.schema)
    if args.filename:
        with open(args.filename) as content:
            process(content, schema)
    elif not sys.stdin.isatty():
        process(sys.stdin, schema)

if __name__ == "__main__":
    main()
