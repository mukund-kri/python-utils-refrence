'''
Trying out voluptuous for dictonary validation.
'''

from voluptuous import Schema, Required


schema = Schema({
        Required('mongo'): {Required('db'): str},
        })

# schema({})

schema({'mongo': {'db': 'test'}})

