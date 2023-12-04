
"""
_main.pyx is the real main.py, but this is here to ignore an error without seeming odd
"""

def part1() -> int: ...
def part2() -> int: ...
def main(): ...

import pyximport; pyximport.install()
from part1 import check_max as part1 #type: ignore
from part2 import check_max as part2 #type: ignore

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()

__all__ = ["main", "part2", "part1", "get_numbers", "parse_from_str"]