import re

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# Character class
vowel_regex = re.compile(r'[aeiouAEIOU]')

# Negative Character Class
consonant_regex = re.compile(r'[^aeiouAEIOU]')

# '^' means the pattern must appear at the beginning of the string
# '$' means the pattern must appear at the end.
# Consequently, preceding and finishing the string with '^' and '$' marks that the string must match the regex
# in its entirety - it's not enough for the regex to match just a certain subset of the string.

persons = """Berra, Davy. Phone: (360) 200-9963
Clark, Taylor. Phone #: 253-209-4771
Williams Berra, Brittany - Phone: (360)-270-6458.
"""

# persons_regex = re.compile(r"""
#     ^(?P<last_name>[\w\s]+),\s
#     (?P<first_name>[\w\s]+).?\sPhone\s?#?:\s
#     (?P<phone_number>\(?\d{3}\)?[-|\s]\d{3}-\d{4}).?$
#     """, re.X | re.M)

persons_regex = re.compile(r"""
    ^(?P<last_name>[\w\s]+),\s
    (?P<first_name>[\w\s]+).?\sPhone\s?\#?:\s
    (?P<phone_number>\(?\d{3}\)?[-|\s]\d{3}-\d{4}).?$
    """, re.X | re.M)

me = persons_regex.search(persons).groupdict()
# print(me)
#
# print(persons_regex.findall(persons))


# Substituting with regex

names_regex = re.compile(r'Agent \w+')
subbed_regex = names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

print(subbed_regex)

# Using part of the original string in subbed regexes
# Use '\1', '\2', '\3', etc. to match corresponding group numbers.
agent_names_regex = re.compile(r'(Agent \w\w)\w*')
subbed_agent_names_regex = agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

print(subbed_agent_names_regex)