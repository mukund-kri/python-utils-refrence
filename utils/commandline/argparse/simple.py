'''
Python's standard lib includes the argparse lib which makes it easy to write
scripts that intreacts with the user. This example is ripped out of one of my
backup script.
'''

from argparse import ArgumentParser


def backup():
    ''' run backup here '''
    print('backing up your files')


def restore():
    ''' restore from backup '''
    print('restoring files from backup')



if __name__ == '__main__':
    
    parser = ArgumentParser('File backup script')
    parser.add_argument('action', type=str, default='backup', 
                        help='Command: backup/resotre')

    args = parser.parse_args()
    
    if args.action == 'backup':
        backup()
    elif args.action == 'restore':
        restore()
    else:
        print('Command %s not supported' % args.action)

