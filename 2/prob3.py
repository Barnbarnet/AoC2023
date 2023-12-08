import re
max_red = 12
max_blue = 14
max_green = 13
res = 0 
file = open("Input.txt", "r")

while True:
    line = file.readline()
    if not line:
        break
    list = line.split(":", 2)
    Index = (list[0].split(" "))[1]
    print(Index)
    sublist = re.split(";|,", list[1])
    t_red = 0
    t_green = 0 
    t_blue = 0
    print(sublist)
    for i in range(len(sublist)):
        print(sublist[i])
        sub_index = int(sublist[i].split(" ")[1])
        print(sub_index)

        if "green" in sublist[i] and sub_index > t_green:
            t_green = sub_index
        if "red" in sublist[i] and sub_index > t_red:
            t_red = sub_index
        if "blue" in sublist[i] and sub_index > t_blue:
            t_blue = sub_index
    

    if t_red > max_red:
        print("rejected game %s" % Index)
    elif t_green > max_green:
        print("rejected game %s" % Index)
    elif t_blue > max_blue:
        print("rejected game %s" % Index)
    else: 
        res = res + int(Index)

print(res)