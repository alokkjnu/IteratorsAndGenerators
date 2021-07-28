#Iterating in Reverse

a = [1,2,3,4]
for x in reversed(a):
    print(x)

f = open('msg.txt')
for line in reversed(list(f)):
    print(line, end='')