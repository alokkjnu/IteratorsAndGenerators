# Taking a slice of an Iterator

def count(n):
    while True:
        yield n
        n+=1

c = count(0)
#print(c[10:20])

