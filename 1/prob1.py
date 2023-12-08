import re

file = open("Input.txt", "r")
res = 0

while True:
    line = file.readline()
    if not line:
        break
    nums = re.findall("[0-9]", line)
    print(nums)
    first = int(nums[0])
    last = int(nums[-1])
    print (10*first + last)
    res = res + 10*first + last
file.close()
print(res)
