'''
Optional arguments with argparser. 

Follows the unix convention. '--' spcifies the name of the optional argument in 
long form and, '-' spcifies the short form.

In this example ...

--queue :: spacifies the queue name (long form)
-q      :: specifies the queue name (short form)
'''

import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    '-q',                   # short form
    '--queue',              # long form
    type=str,               # extract the queue name from command line as a string
    help='Name of queue to add messages',
    required=True
    )
args = parser.parse_args()

if args.queue:
    print('SUCCESS! added messages to queue {}'.format(args.queue))
