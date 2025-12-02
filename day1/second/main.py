with open("input") as f:
    data = f.readlines()

rotation = 50
out = 0
for rot in data:
    if rot[0] == "L":
        rotation -= int(rot[1:])
        if rotation < 0:
            out += int(rot[1:])//100
            rotation = 100*(abs(rotation)//100) + rotation
    elif rot[0] == "R":
        rotation += int(rot[1:])
        if rotation > 99:
            out+=int(rot[1:])//100
            rotation = rotation - 100*(abs(rotation)//100)
    if rotation == 0:
        out+=1

print(out)
