#!/usr/bin/env python3


def mass_to_fuel(mass: int) -> int:
    res: int = mass//3 - 2
    return res if res >= 0 else 0


def ship_fuel(module_masses: [int]) -> int:
    return sum([mass_to_fuel(mass) for mass in module_masses])


def total_fuel(module_masses: [int]) -> int:
    res: int = 0

    for mass in module_masses:
        fuel_mass: int = mass_to_fuel(mass)

        while fuel_mass > 0:
            res += fuel_mass
            fuel_mass = mass_to_fuel(fuel_mass)

    return res
