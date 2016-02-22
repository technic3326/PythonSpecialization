#Assignemnt8.4
stuff = list()
print dir(stuff)
 
x = range(5)
print type(x)
 
fileName =  raw_input("Enter the File name:")
#reading the file
try:
    fileHandle =  open(fileName)
except Exception as e:
    print"Please enter a valid file name {}".format(e)
 
wordList = list()
try:
    for line in fileHandle:
        line = line.rstrip()
        for word in line.split():
            if word in wordList: continue
            wordList.append(word)
    wordList.sort()
    print wordList
except Exception as e:
    print "Exception caught {}".format(e)