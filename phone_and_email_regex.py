import pyperclip
import re

phone_regex = re.compile(r'''
    (?P<area_code>\(?\d{3}\)?)?    # area code - optional
    (\s|-|\.)?      # separator - optional
    (?P<first_three>\d{3})         # first 3 digits
    (\s|-|\.)       # separator
    (?P<last_four>\d{4})         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extension - optional
    ''', re.X | re.M)

persons = """Berra, Davy. Phone: (360) 200-9963
Clark, Taylor. Phone #: 253-209-4771
Williams Berra, Brittany - Phone: (360)-270-6458.
"""

matches = []
for groups in phone_regex.findall(persons):
    number = '-'.join([groups[0], groups[2], groups[4]])
    matches.append(number)

print(matches)

me = phone_regex.search(persons).groupdict()
print(me['area_code'], me['first_three'], me['last_four'])