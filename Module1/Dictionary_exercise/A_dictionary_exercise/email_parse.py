# Dzialwa Nemakonde
# 03 February 2026

# Write a function `email_parse` that accepts an email address string. The function should return a dictionary containing:- `username`
# - `domain`

def email_parse(email):

    lst = email.split("@") # to separate the username from the domain
    
    dict1 = {'username': lst[0], 'domain': lst[1]}
    return dict1

# examples
print(email_parse("coolcoder42@goodmail.com"))
# { 'username': 'coolcoder42', 'domain': 'goodmail.com' }

print(email_parse("az@woohoomail.com"))
# { 'username': 'az', 'domain': 'woohoomail.com' }

print(email_parse("1337pr0graMmer@coldmail.edu"))
# { 'username': '1337pr0graMmer', 'domain': 'coldmail.edu' }