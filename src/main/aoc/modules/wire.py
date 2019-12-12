#!/usr/bin/env python3


class WireNode:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.wires: {int} = set({})
        self.wire_steps: {int, int} = {}

    def add_wire(self, wire_no: int, wire_steps: int) -> None:
        self.wires.add(wire_no)
        if wire_no not in self.wire_steps:
            self.wire_steps[wire_no] = wire_steps

    def is_intersection(self) -> bool:
        return len(self.wires) > 1

    def dist_manhattan(self) -> int:
        return abs(self.x) + abs(self.y)

    def sum_steps(self) -> int:
        return sum([self.wire_steps[key] for key in self.wire_steps])


def parse_wires(raw_wires: [str]) -> [[str]]:
    return [wire.split(",") for wire in raw_wires]


def walk_wires(wires: [[str]]) -> [WireNode]:
    nodes: {str, WireNode} = {}

    for i, wire in enumerate(wires):
        x: int = 0
        y: int = 0
        steps: int = 0

        for section in wire:
            dx: int = 0
            dy: int = 0
            if section.startswith("L") or section.startswith("R"):
                dx += int(section.replace("L", "-").replace("R", "+"))
            else:
                dy += int(section.replace("D", "-").replace("U", "+"))

            while dx != 0 or dy != 0:
                if dx > 0:
                    x += 1
                    dx -= 1
                elif dx < 0:
                    x -= 1
                    dx += 1
                elif dy > 0:
                    y += 1
                    dy -= 1
                else:
                    y -= 1
                    dy += 1

                steps += 1

                key: str = "{},{}".format(x, y)

                if key not in nodes:
                    new_node: WireNode = WireNode(x, y)
                    new_node.add_wire(i, steps)
                    nodes[key] = new_node
                else:
                    nodes[key].add_wire(i, steps)

    return [nodes[key] for key in nodes]


def closest_intersections(nodes: [WireNode]) -> [WireNode]:
    intersections: [WireNode] = [
        node for node in nodes if node.is_intersection()]

    min_dist: int = min([node.dist_manhattan() for node in intersections])

    closest: [WireNode] = [
        node for node in intersections if node.dist_manhattan() == min_dist]

    return closest


def fastest_intersections(nodes: [WireNode]) -> [WireNode]:
    intersections: [WireNode] = [
        node for node in nodes if node.is_intersection()]

    min_steps: int = min([node.sum_steps() for node in intersections])

    fastest: [WireNode] = [
        node for node in intersections if node.sum_steps() == min_steps]

    return fastest
