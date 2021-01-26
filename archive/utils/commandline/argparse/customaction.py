'''
One of the more advanced argparse usage is the custom action. With custom
actions we can excute arbitary code aganst the parsed arguments.

Here I'm just printing the lifecycle.
'''

import argparse


class CustomAction(argparse.Action):
    
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(CustomAction, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
        print("Init :: %r %r" % (option_strings, dest))

    def __call__(self, parser, namespace, values, option_string=None):
        print("CALL: %r %r %r" % (namespace, values, option_string))
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()

parser.add_argument('--foo', dest='bar', action=CustomAction)
parser.add_argument('files', action=CustomAction)

parser.add_argument('--boo', action="store")


args = parser.parse_args('--foo test test1'.split())
print(args)
