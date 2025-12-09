with open('input') as f:
    data_as_list = []
    data = f.readlines()
    for d in data:
        data_as_list.append(list(d.strip("\n")))
out = 0
for i in range(1,len(data_as_list)):
    line = data_as_list[i]
    for j in range(len(line)):
        if line[j] == '.' and data_as_list[i-1][j] == 'S':
            line[j] = '|'
        if line[j] == '.' and data_as_list[i-1][j] == '|':
            line[j] = '|'
        if line[j] == '^' and data_as_list[i-1][j] == '|':
            line[j - 1] = '|'
            line[j + 1] = '|'
            out += 1

print(out)

