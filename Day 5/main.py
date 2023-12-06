import copy

def get_input():
  with open("input") as file:
    raw = file.read().splitlines()
    seeds = [int(num) for num in raw[0].split(" ")[1::]]

    conversions = {}
    from_to = {}
    i = 1
    current = ""
    while i < len(raw):
      if raw[i] == "":
        i += 1
        continue
      elif not raw[i][0].isnumeric():
        a, _, b = raw[i].split(" ")[0].split("-")
        from_to[a] = b
        conversions[b] = []
        current = b
      else:
        conversions[current].append([int(num) for num in raw[i].split(" ")])

      i += 1
  return seeds, conversions, from_to


def func_part_i(s, c, f_t):
  current = f_t.get("seed")
  while current:
    for i in range(len(s)):
      for destination, source, _range in c[current]:
        if s[i] in range(source, source + _range):
          s[i] = destination + (s[i] - source)
          break
    current = f_t.get(current)
  return min(s)


def func_part_ii(s, c, f_t):
  seed_ranges = []
  for i in range(0, len(s), 2):
    seed_ranges.append([s[i], s[i] + s[i + 1]])
    
  current = f_t.get("seed")
  
  while current:
    # print("seed ranges", seed_ranges)  
    s2 = []
    for start, end in seed_ranges:
      filtered = False
      for destination, source, _range in c[current]:
        lower = max(min(start, source + _range), source)
        higher = min(max(end, source), source+_range)
        # print(f"start: {start}, end: {end}")
        # print(f"source: {source}, up to: {source + _range}")
        # print(f"lower: {lower}, higher: {higher}")
        if lower != higher:
          # print("lower != higher")
          s2.append([
              destination + (lower - source), destination + (higher - source)
          ])
          if lower > start:
            # print("lower > start")
            s2.append([start, lower])
          if higher < end:
            # print("higher < end")
            s2.append([higher, end])

          filtered = True
          # print("-"*20)
          break
          
        # print("-"*20)
      if not filtered:
        s2.append([start, end])
    seed_ranges = s2
    print("seed ranges", seed_ranges)
    print("current", current)
    print("c", c[current])
    print(sorted([seed[0] for seed in seed_ranges]))
    print("-"*30)
    input()
    current = f_t.get(current)
  return min([_seed[0] for _seed in seed_ranges])


if __name__ == "__main__":
  seeds, conversions, from_to = get_input()
  print(func_part_i(copy.deepcopy(seeds), conversions, from_to))
  print(func_part_ii(copy.deepcopy(seeds), conversions, from_to))
