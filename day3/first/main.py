import re
with open("input") as f:
    data = f.readlines()
    data_int = []
    for d in data:
        data_int.append([int(n) for n in list(d.strip("\n"))])
out = 0
i = 0
idx = 0
for bank in data_int:
    first = max(bank[:len(bank)-1])
    first_matches = [match.start() for match in re.finditer(str(first), data[i])]
    print(first, first_matches, data[i])
    if len(first_matches) > 1:
        idx = first_matches[-2]
    else:
        idx = first_matches[-1]
    second = max(bank[idx+1:])
    out += int(str(first)+str(second))

    i += 1
print(out)
