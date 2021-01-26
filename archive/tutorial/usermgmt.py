'''
Script to automate user management.

Code for the "Writing python utilites series of posts"
'''

import argparse


parser = argparse.ArgumentParser(prog='USER_MGMT')
sub_parsers = parser.add_subparsers(help='sub command help')

# Create and configure "addcsv" sub parser
addcsv_subparser = sub_parsers.add_parser(
    "addcsv",
    help="Add all the users in a csv file"
)

# Create and configure "add"  sub parser
add_subparser = sub_parsers.add_parser(
    "add",
    help="Add a single user"
)

# Create and configure "rm" sub parser
rm_subparser = sub_parsers.add_parser(
    "rm",
    help="Remove a single user"
)

# Create and configure "rmcsv" sub parser
rmcsv_subparser = sub_parsers.add_parser(
    "rmcsv",
    help="Remove all the users in the csv file"
)

# Create and configure "stat" sub parser
stat_
