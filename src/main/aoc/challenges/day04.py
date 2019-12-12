#!/usr/bin/env python3

from ..modules.utils import read_file, parse_int_list
from ..modules.password import viable_passwords, has_double_strict


def run(input: str) -> None:
    limits: [int] = parse_int_list(read_file(input))
    passwords: [int] = viable_passwords(limits)

    print("Day 04: there are {} viable passwords".format(len(passwords)))

    passwords_strict: [int] = [
        pw for pw in passwords if has_double_strict(str(pw))]

    print("Day 04: there are {} strictly viable passwords".format(
        len(passwords_strict)))
