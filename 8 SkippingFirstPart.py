# Skipping the First Part of an Iterable

with open('msg.txt') as f:
    for line in f:
        print(line, end='')

from itertools import dropwhile, islice
with open('msg.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'),f):
        print(line, end='')

items = ['a','b','c',1,4,10,15]
for x in islice(items,3,None):
    print(x)