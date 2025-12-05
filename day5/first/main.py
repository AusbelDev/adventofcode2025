with open('input') as f:
    data = f.readlines()
    ranges = []
    ids = []
    for line in data:
        line = line.strip("\n")
        if "-" in line:
            ranges.append(line)
        elif line.isnumeric():
            ids.append(line)
out = 0
done = set()
for n in ids:
    for rang in ranges:
        rang = rang.split("-")
        start = int(rang[0])
        end = int(rang[1])

        if int(n) in range(start, end+1) and n not in done:
            out += 1
            done.add(n)
print(out)
