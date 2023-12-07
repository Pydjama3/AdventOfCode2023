import copy
import math
from math import sqrt


def get_input():
    # raw = [["7", "9"], ["15", "40"], ["30", "200"]]
    raw = [["51", "377"], ["69", "1171"], ["98", "1224"], ["78", "1505"]]
    distance = int("".join([d for d, _ in raw]))
    time = int("".join([t for _, t in raw]))
    return [(int(t), int(d)) for t, d in raw], (distance, time)


def func_part_i(_input):
    tot = 1
    for time, distance in _input:
        last = False
        ways = 0
        for i in range(time + 1):
            if i * (time - i) > distance:
                ways += 1
                last = True
            else:
                if last:
                    tot *= ways if ways != 0 else 1
                    break
    return tot


def func_part_ii(_input):
    time, distance = _input

    # -(x**2) + x*time - distance > 0
    discriminant = time**2 - 4*distance
    x1 = (-time - sqrt(discriminant))/(-2)
    x2 = (-time + sqrt(discriminant))/(-2)

    if x1 > x2:
        x1, x2 = x2, x1

    # x1 = math.floor(x1)
    # x2 = math.ceil(x2)

    return round(x2 - x1)


if __name__ == "__main__":
    part1, part2 = get_input()
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(part1))
    print("Part II - Result: ", func_part_ii(part2))
    print("Part II - Result: ", func_part_i([part2]))
