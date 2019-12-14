#!/usr/bin/env python3


def read_file(path: str) -> [str]:
    lines: [str] = []
    with open(path, 'r') as reader:
        lines.extend(reader.readlines())

    return [line.strip() for line in lines]


def parse_int_list(strs: [str]) -> [int]:
    return [int(s) for s in strs if s.isdigit() or s.startswith("-")]
