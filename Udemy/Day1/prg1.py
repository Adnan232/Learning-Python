lst = []
for i in range(0, len("Hello World")):
  if "Hello World"[i] != " ":
    lst.append("Hello World"[i])

# lst.remove("o")
# print(lst.sort())
# lst.sort(reverse=True)
lst.reverse()
print(lst)