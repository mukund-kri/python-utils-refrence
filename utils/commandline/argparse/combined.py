'''
Example: using both positional and optional arguments.

The first argument 'action' is a postional argument. 'action' can be either 
'add' or 'rm'.

optional argument.
--queue :: spacifies the queue name (long form)
-q      :: specifies the queue name (short form)
'''

import argparse


parser = argparse.ArgumentParser()

# The first argument. 
parser.add_argument(
    'action',               # argument name
    type=str,
    choices=['add', 'rm'],  # only add and rm will be allowed
    help='Add or remove messages from the queue'
)

# Second argument (optional argument)
parser.add_argument(
    '-q',                   # short form
    '--queue',              # long form
    type=str,               # extract the queue name from command line as a string
    help='Name of queue to add messages',
    required=True,
    )
args = parser.parse_args()

if args.queue:
    print('SUCCESS! added messages to queue {}'.format(args.queue))
