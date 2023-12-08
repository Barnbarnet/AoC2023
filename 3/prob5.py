import re

file = open("Miniput2.txt", "r")
res = 0
line0 = ""
line1 = "init"
line2 = ""

while True:
    line2 = file.readline()
    if not line1:
        break
    elif line1 != "init":
        print(line1)
        nums = re.findall("[0-9]+", line1)

        for i in range(len(nums)):   
            b = len(nums[i])
            a = re.search(nums[i], line1)
            beg = int(a.start())
            stp = int(a.end())

            #print(line0[beg-1:stp+1])
            print(line1[stp+1])
            #print(line2[beg-1:stp+1])
            Neighbour = ""
            if line1[beg -1]:
                Neighbour = Neighbour + line1[beg - 1]
            if line1[stp] and line1[stp] != "\n":
                Neighbour = Neighbour + line1[stp + 1]
            Neighbour =  Neighbour +line0[beg-1:stp] +line2 [beg-1:stp]
            print(nums[i])
            print (Neighbour)
            signs = re.findall("[^\.]", Neighbour)
            if signs: 
                res = res + int(nums[i])
                print ("Adding %s !" % nums[i])

    line0 = line1
    line1 = line2
    
print(res)