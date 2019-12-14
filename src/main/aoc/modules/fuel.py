#!/usr/bin/env python3


def __mass_to_fuel(mass: int, recursive: int = 1) -> int:
    if mass <= 0:
        return 0

    fuel: int = mass // 3 - 2

    return fuel + mass_to_fuel(fuel if recursive else 0)


def total_fuel(module_masses: [int], recursive: int = 1) -> int:
    return sum([mass_to_fuel(mass, recursive) for mass in module_masses])
