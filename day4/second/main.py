import pprint

with open('input') as f:
    data = f.readlines()
    matrix = []
    for d in data:
        matrix.append([r for r in list(d.strip("\n"))])
out = 0
flag = 0
while True:
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            t, b, r, l = None, None, None, None
            tr, tl, br, bl = None, None, None, None

            if y > 0:
                t = matrix[y-1][x]
            if y < len(matrix) - 1:
                b = matrix[y+1][x]
            if x < len(row) - 1:
                r = row[x+1]
            if x > 0:
                l = row[x-1]
            if y > 0 and x < len(row) - 1:
                tr = matrix[y-1][x+1]
            if y > 0 and x > 0:
                tl = matrix[y-1][x-1]
            if y < len(matrix) - 1 and x < len(row) - 1:
                br = matrix[y+1][x+1]
            if y < len(matrix) - 1 and x > 0:
                bl = matrix[y+1][x-1]

            if [t, b, r, l, tr, tl, br, bl].count("@") < 4 and col == "@":
                matrix[y][x] = "."
                out += 1

    if out > flag:
        flag = out
    else:
        break
print(out)
