def get_input():
    with open("input") as raw:
        lines = [line.split(": ") for line in raw.read().splitlines()]
        games = []
        for _, line in lines:
            sets = []
            for shown in line.split("; "):
                sets.append({package.split(" ")[1]: int(package.split(" ")[0]) for package in shown.split(", ")})
            games.append(sets)
    return games


def func_part_i(_input):
    tot = 0
    i = 1
    for line in _input:
        possible = False
        for shown in line:
            possible = False

            red = shown.get("red")
            green = shown.get("green")
            blue = shown.get("blue")
            if red is not None and red > 12:
                break
            if green is not None and green > 13:
                break
            if blue is not None and blue > 14:
                break
            possible = True

        if possible:
            tot += i
        i += 1
    return tot


def func_part_ii(_input):
    tot = 0
    for line in _input:
        red = 0
        green = 0
        blue = 0

        for shown in line:

            r = shown.get("red") if shown.get("red") is not None else 0
            g = shown.get("green") if shown.get("green") is not None else 0
            b = shown.get("blue") if shown.get("blue") is not None else 0

            red = r if r > red else red
            green = g if g > green else green
            blue = b if b > blue else blue

        tot += red * green * blue
    return tot


if __name__ == "__main__":
    data = get_input()
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(data))
    print("Part II - Result: ", func_part_ii(data))
