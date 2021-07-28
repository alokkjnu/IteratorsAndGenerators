# Creating New Iteration Patterns with Generators

def frange(start,stop,step):
    x = start
    while x<stop:
        yield x
        x += step

for n in frange(0,4,.5):
    print(n)

print(list(frange(0,1,0.125)))


def countdown(n):
    print('starting to count from',n)
    while n>0:
        yield n 
        n -=1
    print('done')

c =countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))