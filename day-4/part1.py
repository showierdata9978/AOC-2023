

with open("input.txt", "r") as f: 
   data = f.readlines()

def parse(line):
    parts = line.split("|")
    numbers = [p.strip()  for p in parts[1].split(" ") if p.strip() != ""]
    winning = [p.strip()  for p in parts[0].split(" ")]

    sum = 0
    for number in numbers:
        if number not in winning:
           continue
        winning.remove(number)
        if sum == 0:
            sum = 1
        else:
            sum = sum * 2
    return sum

def part1():
   sum = 0

   for l in data:
       sum += parse(l)
   return sum

if __name__ == "__main__":
   print(part1())
