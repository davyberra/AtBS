import pyinputplus as pyip
import random, time

question_count = 10
correct_answers = 0

starting_time = time.time()

for question_number in range(question_count):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    prompt = f'Question #{question_number + 1}: What is {num1} x {num2}? '
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8,
                              limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correct_answers += 1

elapsed_time = round(time.time() - starting_time)

print(f'Great Job! Your score:\n{correct_answers}/{question_count}\n'
      f'You completed this quiz in {elapsed_time} seconds.')
