#Iterating in Reverse

a = [1,2,3,4]
for x in reversed(a):
    print(x)

f = open('msg.txt')
for line in reversed(list(f)):
    print(line, end='')

class countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n -= 1

    