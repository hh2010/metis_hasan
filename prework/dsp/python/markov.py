#!/usr/bin/env python

# This Markov text generator was heavily influenced
#   by the example found here: https://pythonadventures.wordpress.com/

# Import 'sys' to grab command line arguments
# Import 'random' which will be used to create our model
import sys
from random import choice

# Specify characters that represent end of line
EOS = ['.', '?', '!']

# Create a dictionary from the text input to be used for modeling
# We will be using two words at a time to model the expected third word
def build_dict(words):
    d = {}
    for i, word in enumerate(words):
        try: first, second, third = words[i], words[i+1], words[i+2]
        except IndexError: break
        key = (first, second)
        if key not in d: d[key] = []
        d[key].append(third)
    return d

# Generate text based on our Markov model and punctuate it
def generate(d):
    count = int(sys.argv[2])
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while len(li) < count:
        try: third = choice(d[key])
        except KeyError: break
        li.append(third)
        key = (second, third)
        first, second = key
        if (len(li) == count and li[-1][-1] not in EOS): li[-1] += choice(EOS)
    return ' '.join(li)

def main():
    fname = sys.argv[1]
    with open(fname, "rt") as f: text = f.read()
    words = text.split()
    d = build_dict(words)
    print(generate(d))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: missing arguments (./markov.py [file.txt] [words])")
        sys.exit(1)
    main()
