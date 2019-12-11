#!/usr/bin/env python3

from ..modules.utils import read_file
from ..modules.intcode import parse_intcodes, exec_intcode


def run(input: str) -> None:
    intcodes: [[int]] = parse_intcodes(read_file(input))

    for intcode in intcodes:
        intcopy: [int] = intcode.copy()
        intcopy[1] = 12
        intcopy[2] = 2
        intcopy = exec_intcode(intcopy)
        print("Day 02: result at index 0 is {}".format(intcopy[0]))

        noun: int = 0
        verb: int = 0
        while verb < 100:
            intcopy = intcode.copy()
            intcopy[1] = noun
            intcopy[2] = verb
            intcopy = exec_intcode(intcopy)

            if intcopy[0] == 19690720:
                break
            else:
                noun += 1

                if noun == 100:
                    noun = 0
                    verb += 1

        print("Day 02: noun is {}, verb is {}, result is {}".format(noun, verb, 100 * noun + verb))
