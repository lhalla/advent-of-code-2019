#!/usr/bin/env python3

from .utils import read_file, parse_int_list
from .computer import Computer
from .icpp import exec_intcode


class Diagnostics(Computer):
    def run_diagnostics(self, input: [[int]] = [[]]) -> None:
        for i, code in enumerate(self.codes):
            for args in input:
                res: int
                outputs: [int]
                res, outputs = exec_intcode(code, args)

                if outputs:
                    if any(outputs[:-1]):
                        raise Exception("Execution failed")

                    print(":: CODE {} | INPUT {} | DIAGNOSTIC CODE: {}".format(
                        i + 1, args, outputs[-1]))
