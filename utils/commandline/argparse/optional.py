'''
Optional argument with argparser. 

Follow the unix convention. '--' scifiews the name of the optional argument in 
long form and '-' spcifies the short form.

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
    help='Name of queue to add messages'
    )
args = parser.parse_args()

if not args.queue:
    print('You have to give me a queue name')
else:
    print('SUCCESS! added messages to queue {}'.format(args.queue))
