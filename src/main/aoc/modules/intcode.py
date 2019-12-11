#!/usr/bin/env python3

from .utils import parse_int_list


def parse_intcode(code_str: str) -> [int]:
    return parse_int_list(code_str.split(","))


def parse_intcodes(code_strs: [str]) -> [[int]]:
    return [parse_intcode(code) for code in code_strs]


def exec_opcode(instr_ptr: int, intcode: [int]) -> int:
    opcode: int = intcode[instr_ptr]

    if opcode not in [1, 2, 99]:
        return -1
    elif opcode == 99:
        return 1

    arg0: int = intcode[intcode[instr_ptr + 1]]
    arg1: int = intcode[intcode[instr_ptr + 2]]
    dest: int = intcode[instr_ptr + 3]

    res: int = arg0 + arg1 if opcode == 1 else arg0 * arg1

    intcode[dest] = res

    return 0


def exec_intcode(intcode: [int]) -> [int]:
    res: [int] = intcode.copy()

    instr_ptr: int = 0
    while instr_ptr < len(res):
        err_code: int = exec_opcode(instr_ptr, res)

        if err_code < 0:
            raise Exception("Invalid opcode at {}!".format(instr_ptr))
        elif err_code > 0:
            break
        else:
            instr_ptr += 4

    return res
