#!/usr/bin/env python3

# IntCode Plus Plus (ICPP), an improvement over day 2's intcode

op_jump: {int, int} = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1}


def __fetch_arg(intcode: [int], ptr: int, mode: int = 1) -> int:
    if mode:
        return intcode[ptr]

    return __fetch_arg(intcode, intcode[ptr], mode + 1)


def __parse_op(intcode: [int], ptr: int) -> (int, int):
    raw_op: str = str(intcode[ptr])

    return (int(raw_op[-2:]), int("0" + raw_op[:-2], 2))


def __exec_op(code: [int], ptr: int, in_args: [int] = [], out: [int] = []) -> ([int], int, [int], [int]):
    op: int
    mode: int
    op, mode = __parse_op(code, ptr)
    args: [int] = in_args.copy()

    if op not in op_jump:
        raise Exception("Invalid op ({})!".format(op))
    elif op == 3 and not args:
        raise Exception("Input argument required for op ({})!".format(op))

    if op == 1 or op == 2:  # ARITHMETICS
        src1: int = __fetch_arg(code, ptr + 1, mode & 1)
        src2: int = __fetch_arg(code, ptr + 2, mode & 2)
        dest: int = __fetch_arg(code, ptr + 3)
        code[dest] = src1 + src2 if op == 1 else src1 * src2
        return (code, ptr + op_jump[op], args, out)
    elif op == 3:  # INPUT
        dest: int = __fetch_arg(code, ptr + 1)
        code[dest] = args[0]
        args.pop(0)
        return (code, ptr + op_jump[op], args, out)
    elif op == 4:  # OUTPUT
        src1: int = __fetch_arg(code, ptr + 1, mode & 1)
        out.append(src1)
        return (code, ptr + op_jump[op], args, out)
    elif op == 5 or op == 6:  # JUMP
        src1: int = __fetch_arg(code, ptr + 1, mode & 1)
        dest: int = __fetch_arg(code, ptr + 2, mode & 2)
        if op == 5 and src1 or op == 6 and not src1:
            ptr = dest
        else:
            ptr += op_jump[op]
        return (code, ptr, args, out)
    elif op == 7 or op == 8:  # COMPARISON
        src1: int = __fetch_arg(code, ptr + 1, mode & 1)
        src2: int = __fetch_arg(code, ptr + 2, mode & 2)
        dest: int = __fetch_arg(code, ptr + 3)
        if op == 7 and src1 < src2 or op == 8 and src1 == src2:
            code[dest] = 1
        else:
            code[dest] = 0
        return (code, ptr + op_jump[op], args, out)
    elif op == 99:  # END
        return (code, -1, args, out)

    return ([], len(code), [])


def exec_intcode(intcode: [int], args: [int] = []) -> (int, [int]):
    code: [int] = intcode.copy()
    ptr: int = 0
    out: [int] = []
    while ptr >= 0:
        code, ptr, args, out = __exec_op(code, ptr, args, out)

    return (code[0], out)
