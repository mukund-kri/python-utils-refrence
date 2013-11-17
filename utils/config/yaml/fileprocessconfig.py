'''
Example of how to read and process YAML config files. This one is ripped
out of my dotfile backup script.
'''

config_file = 'filelist.yml'


import yaml



def read_config_and_print_files():
    ''' print all the files and dirs listed in my config file '''

    fl = open(config_file)
    config = yaml.load(fl)
    
    print("Files to be processed")
    for fl in config['files']:
        print(fl)


if __name__ == '__main__':
    read_config_and_print_files()

