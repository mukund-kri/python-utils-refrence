from PyInquirer import prompt, print_json


databases = ['db1', 'db2', 'db3']


questions = [
    {
        'type': 'checkbox',
        'name': 'databases',
        'message': 'Select the Databases you want to delete',
        'choices': [{'name': db} for db in databases]
    }
]

answers = prompt(questions)
print(answers)
