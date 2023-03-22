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


def main():
    schema = load_scheme("tmp1")

    import argparse, sys

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        with open(args.filename) as content:
            process(content, schema)
    elif not sys.stdin.isatty():
        process(sys.stdin, schema)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
