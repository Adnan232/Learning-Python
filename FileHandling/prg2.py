fileName = input('Enter File Name: ')
try:
    fhand = open(fileName + '.txt')
except:
    print('Invalid File Name!!!')
count = 0
plus = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    end = float(line[(line.find(':')+1):])
    plus = plus + end
    count = count + 1
print('Number : ', (plus/count))
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# plus = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     startPos = line.find(':')
#     piece = line[startPos+1:]
#     end = float(piece)
#     plus = plus+end
#     count = count+1
    
# print("Average spam confidence:", plus/count)