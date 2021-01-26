'''
Date :: 15 Apr 2010

Basics of using ConfigObj
'''
from configobj import ConfigObj

def main():    
    config = ConfigObj('example.ini')

    # List all the hosts
    hosts = config['Hosts']

    for key in hosts:
        host = hosts[key]
        print host

if __name__ == "__main__":
    main()



