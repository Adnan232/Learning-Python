#Tuples is immutable data structure like string
#Functions: count, index.

# tup = (1, 2, 3, 4)
# print(tup)
# (name, age) = ("Adnan Habib", 21)
# print(name, age)


di = dict()
lst = list()
inp = None
tup = tuple()
while inp != 'done':
    inp = input("Enter Name: ")
    if inp !='done': lst.append(inp)
print(lst)
tmp = list()
for name in lst:
    di[name] = di.get(name, 0) + 1
print(di)
for k, v in di.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)