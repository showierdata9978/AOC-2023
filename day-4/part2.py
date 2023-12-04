import sys

sys.setrecursionlimit(1500)

with open("input.txt", "r") as f:
   data = f.readlines()


memory = {}

def parse(line):
    
    game_id = int(line.split(":")[0].split()[1])
    if game_id in memory:
        return memory[game_id]

    parts = line.split("|")
    numbers = [p.strip()  for p in parts[1].split(" ") if p.strip() != ""]
    winning = [p.strip()  for p in parts[0].split(" ")]

    s = 1
    for number in numbers:
        if number not in winning:
            continue
        winning.remove(number)
        s += 1

    if s == 1:
        memory[game_id] = 1
        return 1

    total = 0
    for d in range(1, s):
        total += parse(data[game_id + d - 1])

    num = total + 1
    memory[game_id] = num

    return num

def part2():
   sum = 0

   for l in data:
       sum += parse(l)
   return sum

if __name__ == "__main__":
   print(part2())
