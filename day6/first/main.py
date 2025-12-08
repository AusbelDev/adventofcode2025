import numpy as np
import re
with open("input") as f:
    data = []
    for d in f.readlines():
        data.append([re.findall(r'\d+|[\+\*]+', d)])

out = 0
for op in np.squeeze(np.array(data)).T:
    if op[-1] == '+':
        s = 0
        for m in op[:len(op)-1]:
            s += int(m)
    elif op[-1] == '*':
        s = 1
        for m in op[:len(op)-1]:
            s *= int(m)
    out += s

print(out)
