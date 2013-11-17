'''
A very simple example that reads an ini file and print the value
for the section 'Main' and subsection 'SubMain' and element key.

do 'pip install configobject' before running this file.
'''

from ConfigObject import ConfigObject

config_file = 'config.ini'


def readconfig():
    try:
        # The actual reading and using the config file is quite easy
        config = ConfigObject(filename=config_file)
        assert config['Main']['key'] == 'value'
    except Exception as e:
        print("Error in config file")
        print(e)
    else:
        print("Config file OK")


if __name__ == '__main__':    
    readconfig()


