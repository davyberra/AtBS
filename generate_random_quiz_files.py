"""
Random Quiz Generator.py-
Creates quizzes with questions and answers in random order,
along with the answer key.
"""

import random
import os
from pathlib import Path


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



# Generate 35 quiz files.
for quiz_num in range(35):
    # TODO: Create the quiz and answer key files.
    home = Path.home() / 'Quizzes'
    quiz = open(home / f'quiz{quiz_num}.txt', 'w')
    answer_key = open(home / f'quiz{quiz_num}_answers.txt', 'w')
    # TODO: Write out the header for the quiz.
    quiz.write('The Fifty States and Their Capitals.\n')
    answer_key.write(f'Answers for Quiz #{quiz_num}.\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for index, state in enumerate(states):
        quiz.write(f'The capital of {state} is:\n')
        answer_list = []
        # Create list of capitals
        capital_list = []
        for i in capitals:
            capital_list.append(capitals[i])
        # Add correct answer to answer_list and remove it from capital_list
        answer_list.append(capitals[state])
        capital_list.remove(capitals[state])
        # Create random incorrect answers and remove them from capital_list
        for _ in range(3):
            incorrect_answer = random.choice(capital_list)
            answer_list.append(incorrect_answer)
            capital_list.remove(incorrect_answer)
        random.shuffle(answer_list)
        for answer in answer_list:
            quiz.write(f'    {answer}\n')

        # Create answer key

        answer_key.write(f'Question #{index + 1}: {capitals[state]}\n')

