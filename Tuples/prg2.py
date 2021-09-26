# fname = input("Enter file:")
# hand = open(fname + '.txt')
hand = open('Tuples/test.txt')

counts = dict()
for line in hand:
    words = line.split()
for word in words:
    counts[word] = counts.get(word,0) + 1

# c = {'a':12, 'b':8, 'c':11, 'd':22}
print( sorted([(v, k) for k, v in counts.items()], reverse=True))