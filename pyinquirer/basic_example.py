from PyInquirer import prompt, print_json


questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': "What is your first name?",
    }
]


answers = prompt(questions)
print(answers)
