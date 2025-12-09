import numpy as np
with open("input") as f:
    data = []
    lines = f.readlines()
    max_l = len(sorted(lines, key=lambda s: len(s))[-1]) - 1
    for d in lines[:len(lines)-1]:
        data.append(list(d.strip("\n").ljust(max_l, " ")))

out = 0
ops = list(lines[-1].replace(' ', '').strip("\n"))
operation_idx = 0
s = 1 if ops[0] == '*' else 0
for op in np.array(data).T:
    n_str = "".join(op).strip(' ')
    if len(n_str) == 0:
        operation_idx += 1
        out += s
        if ops[operation_idx] == '*':
            s = 1
        else:
            s = 0
        continue
    if ops[operation_idx] == '+':
        s += int(n_str)
    if ops[operation_idx] == '*':
        s *= int(n_str)

out += s
print(out)
