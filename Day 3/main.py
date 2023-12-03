import numpy


def get_input():
    with open("input") as raw:
        lines = [line for line in raw.read().splitlines()]

        positions = {}
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x].isnumeric():
                    positions[(x, y)] = "num"
                elif lines[y][x] != ".":
                    positions[(x, y)] = "char"

    return positions, lines


def func_part_i(_input):
    positions, lines = _input

    valid = []
    for position in positions:
        x, y = position
        if positions[position] == "num":
            is_valid = False
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if positions.get((x+i, y+j)) == "char":
                        is_valid = True
                if is_valid:
                    valid.append(position)
                    break

    tot = 0
    checked = []
    for position in valid:
        if position not in checked:
            x, y = position

            chunk = [lines[y][x]]
            checked.append(position)

            i = 1
            before = True
            after = True
            while before or after:
                before = False if positions.get((x-i, y)) != "num" else before
                after = False if positions.get((x + i, y)) != "num" else after
                if before:
                    chunk.insert(0, lines[y][x-i])
                    checked.append((x-i, y))
                if after:
                    chunk.append(lines[y][x+i])
                    checked.append((x+i, y))
                i += 1
            tot += int("".join(chunk))
    return tot


def func_part_ii(_input):
    global total
    positions, lines = _input

    tot = 0
    valid = {}
    for position in positions:
        x, y = position
        if positions[position] == "char" and lines[y][x] == "*":
            checks = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
            multipliers = []
            checked = []
            for cursor in range(len(checks)):
                i, j = checks[cursor]
                if positions.get((x+i, y+j)) == "num" and (x+i, y+j) not in checked:
                    chunk = [lines[y+j][x+i]]
                    checked.append((x+i, y+j))

                    on_line = 1
                    before = True
                    after = True
                    while before or after:
                        before = False if positions.get((x + i - on_line, y + j)) != "num" else before
                        after = False if positions.get((x + i + on_line, y + j)) != "num" else after
                        if before:
                            chunk.insert(0, lines[y + j][x + i - on_line])
                            checked.append((x + i - on_line, y + j))
                        if after:
                            chunk.append(lines[y + j][x + i + on_line])
                            checked.append((x + i + on_line, y + j))
                        on_line += 1
                    multipliers.append(int("".join(chunk)))
            print(multipliers, position)
            print(numpy.array([[lines[position[1] + j][position[0] + i] for i in range(-1, 2)] for j in range(-1, 2)]))
            if len(multipliers) == 2:
                tot += multipliers[0] * multipliers[1]
    return tot


if __name__ == "__main__":
    data = get_input()
    # print(data)
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(data))
    print("Part II - Result: ", func_part_ii(data))  # 1871340
