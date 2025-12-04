with open("input") as f:
    data = f.read()
    data_list = data.split(",")

out = 0
for ids_range in data_list:
    start, end = ids_range.split('-')
    for id in range(int(start), int(end) + 1):
        id_str = str(id)
        id_len = len(id_str)
        half_len = int(id_len / 2)
        for i in range(1, half_len + 1):
            if id_len % i == 0 and id_str.count(id_str[:i]) == id_len//i:
                print(i, id)
                out += id
                break

print(out)
