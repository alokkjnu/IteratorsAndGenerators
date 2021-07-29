# Skipping the First Part of an Iterable

with open('msg.txt') as f:
    for line in f:
        print(line, end='')

from itertools import dropwhile, islice
with open('msg.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'),f):
        print(line, end='')

