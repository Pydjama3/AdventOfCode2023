import math

import numpy as np

from utils import LogManager


def get_input():
    with open('input') as file:
        raw = file.read().splitlines()
        sequence = raw[0]

        _summits = {}
        for line in raw[2::]:
            from_a, to_b_and_c = line.split(" = ")

            b_w_p, c_w_p = to_b_and_c.split(", ")

            b = b_w_p[1::]
            c = c_w_p[:3:]

            _summits[from_a] = (b, c)

        return sequence, _summits


def func_part_i(sequence, _summits, start="AAA"):
    steps = 0
    current = "AAA"
    while not current.endswith("Z"):
        instruction = sequence[steps % len(sequence)]
        current = _summits.get(current)[0 if instruction == "L" else 1]
        steps += 1
    return steps


def func_part_ii(sequence, _summits):
    cursor = 0
    times = -1
    divider = len(sequence)
    current = [key for key in _summits if key.endswith("A")]
    starts = [None for _ in current]
    running = True
    while running:
        instruction = sequence[cursor % divider]
        for i in range(len(current)):
            current[i] = _summits.get(current[i])[0 if instruction == "L" else 1]
            if current[i].endswith("Z"):
                if starts[i] is None:
                    starts[i] = cursor + 1
        cursor += 1

        end = True
        for start in starts:
            if not start:
                end = False
                break
        if end:
            running = False
    return np.lcm.reduce(np.array(starts))


if __name__ == "__main__":
    log_manager = LogManager(f"{__file__.split('/')[-2]:-^22s}")
    data, summits = get_input()
    log_manager.heading()
    log_manager.answer("Part I - Result: ", func_part_i(data, summits))
    log_manager.answer("Part II - Result: ", func_part_ii(data, summits))
