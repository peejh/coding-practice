import re

def fun(s):
    # return True if s is a valid email, else return False
    regex_valid_email = r"^[\w-]+@[a-zA-Z0-9]+\.[A-Za-z]{1,3}$"
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)