'''
JSON can also be used as config files. 
Python now comes with a builtin JSON parser.

Note: JSON is not nearly as human readable as YAML or INI
'''

config_file = 'files.json'


import json


def read_config():
    config = json.load(open(config_file))
    for fl in config['files']:
        print(fl)


if __name__ == '__main__':
    read_config()

