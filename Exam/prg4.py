text = open("text.txt", "r") 
d = dict() 
count=0
# for line in text:
#   count+=1 
#         line = line.strip()  
#         line = line.lower() 
#         words = line.split(" ")  
#         for word in words: 
#              if word in d: 
#                 d[word] = d[word] + 1
#              else: 
#                  d[word] = 1
# for key in list(d.keys()): 
#     print(key, ":", d[key])
# print(count)
line = text.readlines()
# for l in line:
#   l = l.strip()
#   count+=1
# print(count)
print(len(line))