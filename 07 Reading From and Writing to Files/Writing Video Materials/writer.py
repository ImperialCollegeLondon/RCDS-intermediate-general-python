import os

path = os.path.join("Squares", "numbers.dat")

try:
    os.mkdir("Squares")
except FileExistsError:
    pass

with open(path, "w") as f:
    for i in range(1, 11):
        f.write("{}, {}\n".format(i, i ** 2))