with open("input") as f:
    data = f.readlines()

pos = 50
out = 0
for rot in data:
    suff = rot[0]
    if int(rot[1:]) % 100 == 0:
        out+= int(rot[1:]) // 100
        continue
    cycles = int(rot[1:])//100
    out += cycles
    rem = int(rot[1:]) % 100
    print(out, rem, cycles, pos, rot)
    if suff == "R":
        pos += rem
        if pos == 100:
            out+=1
            pos = 0
            continue
        elif pos > 100:
            pos -= 100
            out += 1
    elif suff == "L":
        if pos == 0:
            pos -= rem
            pos += 100
            continue
        pos -= rem
        if pos == 0:
            out += 1
            continue
        elif pos < 0:
            pos += 100
            out += 1


print(out)
