# str1 = "Hello"
# str2 = "123"

# try :

#     print(str1 + str2)
#     print(str1 + "123")
#     print(str2 + 123)    
# except :
#     print("Invalid String Addition")
# a = "AdnanHabib"
# # print(a[0:6])
# print(a[10:0])

# apple = 'Apple'

# ans = input("Enter Item Name: ")
# print(ans.upper())
# print(ans.lower())
# print(ans.capitalize())
# print(ans.count('a', 0, 40))


# Item = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
# temp = 0
# for i in Item:
#     if ans == i:
#         print("YES, Item Available")
#         temp = 1
#         break
# if temp == 0:
#     print("No")

# url = 'https://docs.python.org/3/library/stdtypes.html#string-methods'
# print (url[(url.find('library')) : url.find('/stdtypes', url.find('library'))])
text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find('0.8475'):len(text)]))