# Manually Consuming an Iterator

with open('msg.txt') as f:
    try:
        while True:
            line = next(f)
            print(line,end='')
    except StopIteration:
        pass

with open('msg.txt') as f:
    while True:
        line = next(f,None)
        if line is None:
            break
        print(line,end='')

items = [1,2,3,4]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
