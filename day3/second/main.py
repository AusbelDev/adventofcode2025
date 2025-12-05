import re
with open("input") as f:
    data = f.readlines()
    data_int = []
    for d in data:
        data_int.append([int(n) for n in list(d.strip("\n"))])

out = 0
rem = 12

def find(rem, sub_s, jolt):
    if rem == 0:
        return jolt
    else:
        for i in range(9,0,-1):
            if str(i) in sub_s:
                top_idx = [match.start() for match in re.finditer(str(i), sub_s) if len(sub_s) - match.start() >= rem]
                if len(top_idx) >= 1:
                    sub_s = sub_s[top_idx[0]+1:]
                    jolt.append(i)
                    rem -= 1
                    break

        return find(rem, sub_s, jolt)

for bank in data_int:
    jolt = []
    s = "".join([str(n) for n in bank])
    o = find(rem, s, jolt)
    print(o)
    out += int(''.join([str(n) for n in o]))

print(out)
