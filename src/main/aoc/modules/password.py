#!/usr/bin/env python3


def has_double(password: str) -> bool:
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True

    return False


def has_double_strict(password: str) -> bool:
    digit_counts: [int] = []
    ptr: int = 0
    while ptr < len(password):
        ctr: int = 0

        while ptr + ctr < len(password) and password[ptr] == password[ptr + ctr]:
            ctr += 1

        digit_counts.append(ctr)

        ptr += ctr

    return 2 in digit_counts


def viable_passwords(limits: [int]) -> [int]:
    pw_min: str = "{0:06d}".format(min(limits))
    # len_min: int = len(pw_min)

    pw_max: str = "{0:06d}".format(max(limits))
    len_max: int = len(pw_max)

    digits: [str] = [str(i) for i in range(10)]

    viables: [str] = [s for s in digits if s >= pw_min[0] and s <= pw_max[0]]

    length: int = 1
    while length < len_max:
        new_viables: [str] = []

        while viables:
            root: str = viables.pop(0)

            new_viables.extend([root + s for s in digits if (root + s) >= pw_min[:length+1]
                                and (root + s) <= pw_max[:length+1] and s >= root[-1]])

        viables = new_viables
        length += 1

    viables = [pw for pw in viables if has_double(pw)]

    return [int(pw) for pw in viables]
