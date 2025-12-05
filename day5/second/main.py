with open('input') as f:
    data = f.readlines()
    ranges = []
    for line in data:
        line = line.strip("\n")
        if "-" in line:
            ranges.append(line)
    ranges = sorted(ranges, key= lambda rang: int(rang.split("-")[0]))
prev_s = 0
prev_e = 0
out = 0
for rang in ranges:
    r = rang.split('-')
    start = int(r[0])
    end = int(r[1])

    n_items = end - start + 1
    if end <= prev_e:
        continue
    
    if start <= prev_e:
        start = prev_e +1
    
    prev_e = end
    out += end - start + 1

print(out)
