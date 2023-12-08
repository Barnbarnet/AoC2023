import re

file = open("Input.txt", "r")
res = 0

while True:
    line = file.readline()
    if not line:
        break
    nums = re.findall("[0-9]|oneight|eightwo|twone|one|two|three|four|five|six|seven|eight|nine", line)
    print(nums)
    for i in range(len(nums)):
        if nums[i] == "one":
            nums[i] = 1
        elif nums[i] == "two":
            nums[i] = 2 
        elif nums[i] == "three":
            nums[i] = 3
        elif nums[i] == "four":
            nums[i] = 4 
        elif nums[i] == "five":
            nums[i] = 5
        elif nums[i] == "six":
            nums[i] = 6 
        elif nums[i] == "seven":
            nums[i] = 7
        elif nums[i] == "eight":
            nums[i] = 8
        elif nums[i] == "nine":
            nums[i] = 9

    for i in range(len(nums)):
        if nums[i] == "twone":
            nums[i] = 2
            nums.insert(i+1, 1)
        if nums[i] == "oneight":
            nums[i] = 1
            nums.insert(i+1, 8)
        if nums[i] == "eightwo":
            nums[i] = 8
            nums.insert(i+1, 2)    
    print (nums)                                                                     
    first = int(nums[0])
    last = int(nums[-1])
    print (10*first + last)
    res = res + 10*first + last
    print(res)
file.close()
print(res)
