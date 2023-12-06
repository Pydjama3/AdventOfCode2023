def get_input():
    with open('input') as file:
        content = file.read().splitlines()
        data = []
        for line in content:
            _, lists = line.split(':')
            parts = []
            for p in lists.split(' |'):
                part = []
                for i in range(0, len(p), 3):
                    part.append(int(p[i + 1] + p[i + 2]))
                parts.append(part)
            data.append(parts)
    return data


def func_part_i(_input):
    tot = 0
    for my, given in _input:
        power = None
        for num in my:
            if num in given:
                power = 1 if power == None else power + 1
        if power:
            tot += 2 ** (power - 1)
    return tot


def func_part_ii(_input):
    d = {i: 1 for i in range(len(_input))}
    for i in range(len(_input)):
        in_both = 0
        for num in _input[i][0]:
            if num in _input[i][1]:
                in_both += 1
                d[i + in_both] += d[i]
    return sum(d.values())


if __name__ == '__main__':
    data = get_input()
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(data))
    print("Part II - Result: ", func_part_ii(data))
