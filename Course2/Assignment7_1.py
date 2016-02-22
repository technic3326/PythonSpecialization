# Assignment 7.1
fileName = raw_input("Enter the File name:")
try:
    fileHandle = open(fileName)
    for line in fileHandle:
        stripped = line.rstrip()
        print stripped.upper()
except:
    print "Please enter a valid file name"
    exit()