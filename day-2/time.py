import main
import time

def _main():
	times = 1000

	avg = 0

	for _ in range(times):
		start = time.time()

		main.part1()
		avg += (time.time() - start)

	print("Part 1:", (avg / times) * 1000, "ms")


	avg = 0

	for _ in range(times):
		start = time.time()
		main.part2()
		avg += (time.time() - start)

	print("Part 2:", (avg / times) * 1000, "ms")

_main()