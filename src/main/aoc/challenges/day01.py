#!/usr/bin/env python3

from ..modules.utils import read_file, parse_int_list
from ..modules.fuel import total_fuel_single_pass, total_fuel


def run(input: str) -> None:
    masses: [int] = parse_int_list(read_file(input))

    fuel_req: int = total_fuel_single_pass(masses)

    print("Day 01: fuel requirement is {}".format(fuel_req))

    total_req: int = total_fuel(masses)

    print("Day 01: total requirement is {}".format(total_req))
