import numpy as np

with open("input.txt", 'r') as f:
    data = f.read()

data = [[i for i in d] + ["\n"] for d in data.split("\n")]

def debug(locals):
    locals = locals.copy()
    del locals["data"]

    print(locals)

def issymbol(char):
    return char != '.' and not char.isdigit()

current_number = 0

part_indexes = []
sum = 0

def get_indexes(x, y, indice):

    if x == 0 and y == 0:
        return False
    
    cut = (indice[0] + x, indice[1] + y)
    c = data[cut[0]][cut[1]]
    print(y, x, cut, c.replace("\n", ""))

    if issymbol(c):
        return True

    return False

for y, row in enumerate(data):
    for x, i in enumerate(row):

        if i.isdigit() and i != "." and i != "0":
            part_indexes.append((y, x))
            print((y, x), i)
            current_number = current_number * 10 + int(i)
        else:
            if current_number == 0: continue
            print("----", current_number, "----")
            found = False
            for indice in part_indexes:

                for x2 in [-1, 0, 1]:
                    for y2 in [-1, 0, 1]:
                        try:
                                pass # noop
                                if get_indexes(x2, y2, indice):
                                    print('found')
                                    found = True
                                    break
                        except IndexError:
                            pass

                        if found:
                            break
                    if found:
                        break
                if found:
                    break


            if found:
                sum += current_number


            part_indexes = []
            current_number = 0

print(sum)
