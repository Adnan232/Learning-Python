str = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008   "
demo = str.rstrip()
demoList = demo.split()
# for i in demoList:
#     if 'uct.ac.za' in i:
#         pos = i.find('@')
#         print(i[pos+1:])
email = demoList[1]
emailList = email.split('@')
print(emailList[1])