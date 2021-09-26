# xfile = open('prg1_file.txt')
# for line in xfile:
#     line = line.rstrip()
#     if line.endswith('.com'):
#         print(line)
# # print(len(mail))
# # text = 'dc.detective.conan.1995@gmail.com'
# # print((mail[mail.find(text):len(text)]))
# # for i in xfile:
# #     print(i)
# # print(mail)
import re

actual_file = open("FileHandling/prg1_file.txt")
parse_list = list()
for line in actual_file:
     a = re.findall('[0-9]+',line)
     parse_list = parse_list + a

sum = 0
for b in parse_list:
    sum = sum + int(b)

print(sum)