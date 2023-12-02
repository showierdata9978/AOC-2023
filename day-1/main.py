"""
_main.pyx is the real main.py, but this is here to ignore an error without seeming odd
"""

def parse_from_str(n: str): ...
def get_numbers(l, part): ...
def part1() -> int: ...
def part2() -> int: ...
def main(): ...

import pyximport; pyximport.install()
from _main import * # type: ignore

if __name__ == "__main__":
    main()

__all__ = ["main", "part2", "part1", "get_numbers", "parse_from_str"]