import re

words = []

with open('./thoppe/starter_passwords.txt') as f:
    head = [next(f).strip() for x in xrange(10)]
for i in head: print i
    for i in f.readlines():
        if re.search(r'\s\([+-]\d+\.?\d*\)', i):
            words.append([i]i.strip()