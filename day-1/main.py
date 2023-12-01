
with open("input.txt", "r") as f:
    lines = f.readlines()



def parse_from_str(n):
	if n.endswith("one"): return 1
	elif n.endswith("two"): return 2
	elif n.endswith("three"): return 3	
	elif n.endswith("four"): return 4
	elif n.endswith("five"): return 5
	elif n.endswith("six"): return 6
	elif n.endswith("seven"): return 7
	elif n.endswith("eight"): return 8
	elif n.endswith("nine"): return 9
	return 0

def get_numbers(l, part):
	first = None
	parsed = ""
	i = ''
	n = None
	for i in l:
	  if i.isdigit():
	    n = i
	    parsed = ""
	  elif part == 2:
	    if i not in 'fgenohivwtursx': continue 
	    parsed += i
	    if (m := parse_from_str(parsed)) != 0:
	      n = m
	      parsed = parsed[-1]
	    else:
	      continue
	  else:
	     continue

	  if first == None:
	     first = n
	  
	return (int(first) * 10) + int(n)

def part1():
	
	sum = 0

	for l in lines:
	
		sum += get_numbers(l.strip(), 1)

	return sum

def part2():
	sum = 0 
	for l in lines:

	        sum  += get_numbers(l.strip(), 2)

	return sum

def main():
	print("Part 1:", part1())
	print("Part 2:", part2())

	
if __name__ == "__main__":
	main()
