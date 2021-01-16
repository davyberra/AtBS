import pyinputplus as pyip

# response = pyip.inputNum('Enter number: ', min=4, lessThan=6, blank=True)

# response = pyip.inputYesNo('Answer "yes" or "no".', limit=2, default='No')
#
# print(f'The response is {response}.')

def adds_up_to_ten(numbers):
    print("Enter a string of numbers that adds up to ten. IF YOU DARE.")
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception("The digits must add up to 10, not %s." % (sum(numbers_list)))
    return int(numbers)     # Return an int form of numbers.

response = pyip.inputCustom("Enter a string of numbers that adds up to ten. IF YOU DARE.", adds_up_to_ten)




