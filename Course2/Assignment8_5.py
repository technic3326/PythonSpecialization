#Assignment 8.5   
fileName =  raw_input("Enter the File name:")
#reading the file
try:
    fileHandle =  open(fileName)
except Exception as e:
    print"Please enter a valid file name {}".format(e)

wordList = list()
count = 0
try:
    for line in fileHandle:
        if line.startswith('From '):
            count = count + 1
            line = line.rstrip()
            wordList = line.split()
            print wordList[1]
            
    print "There were", count, "lines in the file with From as the first word"     
except Exception as e:
    print "Exception caught {}".format(e)   