#Assignment 9.4
fileName = raw_input("Please enter the file name:")
try:
    fileHandle = open(fileName)
except Exception as e:
    print "Enter a valid file name"
    exit()
 
wordList = list()  
emailDict = dict() 
try:
    for line in fileHandle:
        line = line.rstrip()
        if line.startswith("From "):
            wordList = line.split()
            key = wordList[1]
            emailDict[key] = emailDict.get(key,0)+1
    
    maxKey = None
    maxValue = None
    for email,count in emailDict.items():
        if maxValue is None or count > maxValue:
            maxKey = email
            maxValue = count
    print maxKey, maxValue
             
except Exception as e:
    print "Exception caught {}".format(e)