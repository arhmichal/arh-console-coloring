# arh-console-coloring

python-based extendable tool for coloring terminal oputput on the fly in the pipeline

TODOs:
- add and use a good logger
- consider naming convention and .gitignore entry for user schemas
- load schemas by path so that they can be outside of the repo, like in user's home

HELP section

usage: colorme [-h] -s SCHEMA [SCHEMA ...] [-v] [-t] [-f [FILENAME]]

Offers an extensive stdin/file-content replace mechanism using a python file with replace rules for the
main purpose of colloring console output.

options:
  -h, --help            show this help message and exit
  -s SCHEMA [SCHEMA ...], --schema SCHEMA [SCHEMA ...]
                        name of a *.py file but without '.py' extension that contains schema
                        definition. can use multiple schemas.
  -v, --verbose
  -t, --timeit
  -f [FILENAME], --filename [FILENAME]
                        file name/path to read as input
