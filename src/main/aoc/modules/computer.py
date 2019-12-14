#!/usr/bin/env python3

from .utils import read_file, parse_int_list
from .icpp import exec_intcode


class Computer:
    def __init__(self, path: str) -> None:
        lines: [str] = read_file(path)

        self.codes: [[int]] = [parse_int_list(
            line.split(",")) for line in lines]

    def run(self, overrides: {int, int}={}, input: [[int]] = [[]]) -> None:
        for i, code in enumerate(self.codes):
            for key in overrides:
                code[key] = overrides[key]

            for args in input:
                res: int
                outputs: [int]
                res, outputs = exec_intcode(code, args)

                print(":: CODE {} | INPUT {} | RESULT: {}".format(i + 1, args, res))

    def solve_grammar(self, target: int, noun_ini: (int, int, int) = (1, 0, 100), verb_ini: (int, int, int) = (2, 0, 100)) -> None:
        for i, code in enumerate(self.codes):
            intcode: [int] = code.copy()

            noun_index: int
            noun: int
            noun_max: int

            verb_index: int
            verb: int
            verb_max: int

            noun_index, noun, noun_max = noun_ini
            verb_index, verb, verb_max = verb_ini

            while verb < verb_max:
                intcode[noun_index] = noun
                intcode[verb_index] = verb

                res: int
                res, _ = exec_intcode(intcode)

                if res == target:
                    break

                noun += 1
                if noun >= noun_max:
                    noun = 0
                    verb += 1

            print(":: CODE {} | TARGET {} | NOUN: {}, VERB: {}".format(
                i + 1,  target, noun, verb))
