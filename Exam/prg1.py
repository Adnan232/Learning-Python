# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     long_word = []
#     for word in words:
#         if len(word) == max_len:
#             long_word.append(word)
#     return long_word
# print(longest_word('prg1.txt'))

text = open("prg1.txt", "r") 
d = dict() 
for line in text: 
        line = line.strip()  
        line = line.lower() 
        words = line.split(" ")  
        for word in words: 
             if word in d: 
                d[word] = d[word] + 1
             else: 
                 d[word] = 1
for key in list(d.keys()): 
    print(key, ":", d[key])
