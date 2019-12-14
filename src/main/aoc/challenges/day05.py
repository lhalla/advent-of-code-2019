#!/usr/bin/env python3

from ..modules.diagnostics import Diagnostics


def run(input: str) -> None:
    diag: Diagnostics = Diagnostics(input)

    print("Day 05: running diagnostics...")
    diag.run_diagnostics([[1], [5]])
