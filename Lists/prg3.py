fhand = open("Lists/mbox.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    #To avoid error due to Empty Line
    if len(line) < 1: continue 
    # if line == "": continue
        
    words = line.split()
    # if len(words) < 3 or words[0] !="From": continue #Another Guardian line
    if words[0] != "From:" :
        continue
    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")