#!/usr/bin/env python3


def mass_to_fuel_single_pass(mass: int) -> int:
    res: int = mass // 3 - 2

    return res if res >= 0 else 0


def mass_to_fuel(mass: int) -> int:
    if mass <= 0:
        return 0

    res: int = mass // 3 - 2

    return res + mass_to_fuel(res)


def total_fuel_single_pass(module_masses: [int]) -> int:
    return sum([mass_to_fuel_single_pass(mass) for mass in module_masses])


def total_fuel(module_masses: [int]) -> int:
    return sum([mass_to_fuel(mass) for mass in module_masses])
