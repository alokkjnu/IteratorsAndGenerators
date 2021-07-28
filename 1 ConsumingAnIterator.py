# Manually Consuming an Iterator

with open('msg.txt') as f:
    try:
        while True:
            line = next(f)
            print(line,end='')
    except StopIteration:
        pass
