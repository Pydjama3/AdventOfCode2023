def get_input():
    with open("input") as raw:
        return [line for line in raw.read().split("\n")]


def func_part_i(_input):
    tot = 0
    for line in _input:
        fl = [None, None]
        i = 0
        while not (fl[0] and fl[1]) and i < len(line):
            current = line[i], line[len(line) - 1 - i]
            if current[0].isnumeric():
                fl[0] = current[0] if fl[0] is None else fl[0]
            if current[1].isnumeric():
                fl[1] = current[1] if fl[1] is None else fl[1]
            i += 1

        if all(fl):
            tot += int("".join(fl))

    return tot


def func_part_ii(_input):
    tot = 0
    num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in _input:
        fl = [None, None]
        reverse = line[::-1]
        i = 0

        while not (fl[0] and fl[1]) and i < len(line):
            if line[i].isnumeric():
                fl[0] = line[i] if fl[0] is None else fl[0]

            if reverse[i].isnumeric():
                fl[1] = reverse[i] if fl[1] is None else fl[1]

            for size in range(3, 6):  # max and min length of a number
                fl[0] = num.get(line[i: i + size]) if fl[0] is None else fl[0]
                fl[1] = num.get(reverse[i: i + size][::-1]) if fl[1] is None else fl[1]
            i += 1

        tot += int("".join(fl))

    return tot


if __name__ == "__main__":
    data = get_input()
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(data))
    print("Part II - Result: ", func_part_ii(data))
