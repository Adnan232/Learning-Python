# import re

# inp = input ('Enter File Name: ')
# if len(inp) < 1 : inp = 'test.txt'

# fname = open(inp)
# sumNum = 0
# numList = list()
# for line in fname:
#   reqNum = re.findall('([0-9]+)', line)
#   if len(reqNum) < 1: continue
#   newList = list()
#   for num in reqNum:
#     newList.append(int(num))
#   # print (newList)
#   sumNum += sum(newList)

# print(sumNum)

# import re

# #Extracting Digits and Summing them
# hand = open("test.txt")
# numlist = []

# for line in hand:
#     line = line.rstrip()
#     extract = re.findall("([0-9]+)", line)

#     if len(extract) < 1 : continue

#     for i in range(len(extract)):
#         num = int(extract[i])
#         numlist.append(num)

# print(sum(numlist))

import re

hand = open("mbox.txt")
for i in hand:
  line = i.rstrip()
  if re.search("From:", line):
    print(line)