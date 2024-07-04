# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
import email.utils

def validateEmail(line):
    emailPattern = r'^[A-Za-z][\w\.-]+@[A-Za-z]{1,}\.[A-Za-z]{1,3}$'
    name, email = line.split()
    email = email[1:-1] # remove enclosing brackets
    return bool(re.match(emailPattern, email))

def sol1():
    T = int(input())
    records = [input() for _ in range(T)]
    clean_recs = list(filter(validateEmail, records))
    print(*clean_recs, sep='\n')

def sol2():
    n = int(input())
    regex_pattern = r'^([a-zA-Z])([a-zA-Z0-9-._]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$'
    for _ in range(n):
        name, user_email = email.utils.parseaddr(input())
        if re.match(regex_pattern, user_email):
            print(email.utils.formataddr((name, user_email)))