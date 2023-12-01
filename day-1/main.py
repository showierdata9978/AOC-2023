
with open("input.txt", "r") as f:
    lines = f.readlines()



def parse_from_str(n):
	if n.endswith("one"): return "1"
	elif n.endswith("two"): return "2"
	elif n.endswith("three"): return "3"	
	elif n.endswith("four"): return "4"
	elif n.endswith("five"): return "5"
	elif n.endswith("six"): return "6"
	elif n.endswith("seven"): return "7"
	elif n.endswith("eight"): return "8"
	elif n.endswith("nine"): return "9"
	return 0

def get_numbers(l, part):
	first = None
	parsed = ""
	i = ''
	c = 0
	n = None
	while c <= len(l) - 1:
	  i = l[c]
	  c += 1
	  if i.isdigit():
	    n = i
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
	  
	return str(first), str(n)

sum = 0

for l in lines:
	
	sum += int("".join(get_numbers(l.strip(), 1)))

print(sum)

sum = 0 
for l in lines:

        sum += int("".join(get_numbers(l.strip(), 2)))

print(sum)
