f = open("films.dat")
lines = [line.rstrip() for line in f.readlines()]
f.close()

media = {}

for line in lines:
    x = line.split(": ")
    media[x[0]] = x[1]
    
print(media)