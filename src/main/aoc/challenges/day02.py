#!/usr/bin/env python3

from ..modules.computer import Computer


def run(input: str) -> None:
    pc: Computer = Computer(input)

    print("Day 02: running the computer...")
    pc.run({1: 12, 2: 2})
    pc.solve_grammar(19690720)
