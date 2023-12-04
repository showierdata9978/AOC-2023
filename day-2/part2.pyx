
with open("input.txt", "r") as f:
    lines = f.read().split("\n")

def max_lists(l1, l2):
    # get the shortest list
    shortest = None
    longest = None
    if len(l1) < len(l2):
        shortest = l1
        longest = l2
    else:
        shortest = l2
        longest = l1

    ret = []
    for n, i in enumerate(longest):
        if i >= shortest[n]:
            ret.append(i)
        else:
            ret.append(i if i > shortest[n] else 0)

    return ret

max_posible_r = 12
max_posible_g = 13
max_posible_b = 14

def split(l):
    game_id, l = l.strip().split(":")
    game_id = int(game_id.split()[1]) # remove "Game "

    r = 0
    g = 0
    b = 0

    prev = [0, 0, 0]
    for i in l.split(";"):
        colors = i.split(",")
        r = 0
        g = 0
        b = 0
        for i in colors:
            count, color = i.strip().split(" ")


            if color == "red":
                r = int(count)
            elif color == "green":
                g = int(count)
            elif color == "blue":
                b = int(count)


        prev = [max(r, prev[0]), max(g, prev[1]), max(b, prev[2])]

    print(prev)
    return prev[0] * prev[1] * prev[2]



def check_max():
    sum = 0
    for l in lines:

        sum += split(l)





    return sum

