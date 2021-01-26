'''
A more complex example.

Supports two operations ...

1. add
$> python sub_parser.py add -f/--file <filename> -n/--number 10
adds 10 messages read from the file on to the queue.

2. rm
$> python sub_parser.py rm -n 15
removes 15 messages from the top of the queue.

Note add and remove have different arguments. This is supported in 
argparse with the sub-commands.
'''


import argparse


parser = argparse.ArgumentParser(prog='Q_LOADER')
sub_parsers = parser.add_subparsers(help='sub command help')

# create and configure the "add" sub parser
add_parser = sub_parsers.add_parser(
    'add',
    help='Add messages to the queue from file')
add_parser.add_argument(
    '-f',
    '--file',
    type=str,
    help='Name of file containing messages',
    required=True
    )
add_parser.add_argument(
    '-n',
    '--number',
    type=int,
    help='Number of messages to add to the queue',
    default=10
    )
add_parser.set_defaults(action='add')       # add the action type into the args

# crate and configure the "rm" sub parser
rm_parser = sub_parsers.add_parser(
    'rm',
    help='Remove messages from the queue'
)
rm_parser.add_argument(
    '-n',
    '--number',
    type=int,
    help='Number of messages to remove (REQUIRED)',
    required=True
)
rm_parser.set_defaults(action='rm')        # add the action type into the args


args = parser.parse_args()

if (args.action == 'add'):
    print('Adding {} messages from file {} to the queue'.format(args.number, args.file))
else:
    print('Removing {} messages from the queue'.format(args.number))

    
