#!/usr/bin/env python3

from ..modules.utils import read_file
from ..modules.wire import WireNode, parse_wires, walk_wires, closest_intersections, fastest_intersections


def run(input: str) -> None:
    wires: [[str]] = parse_wires(read_file(input))
    nodes: [WireNode] = walk_wires(wires)
    closest: [WireNode] = closest_intersections(nodes)

    if len(closest) > 0:
        print("Day 03: distance to closest intersection is {}".format(
            closest[0].dist_manhattan()))
    else:
        print("Day 03: no intersections were found")

    fastest: [WireNode] = fastest_intersections(nodes)

    if len(fastest) > 0:
        print("Day 03: step count to fastest intersection is {}".format(
            fastest[0].sum_steps()))
    else:
        print("Day 03: no intersections were found")
