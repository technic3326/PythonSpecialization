fileName = raw_input("Please Enter a file name:")

try:
    fileHandle = open(fileName)
except Exception as e:
    print "Please enter a valid file name {}".format(e)

wordList = list()
timeList = list()
time_seprator = ":"
hourMap = dict()

try:
    for line in fileHandle:
        line = line.rstrip()
        if line.startswith("From "):
            wordList = line.split()
            for i in wordList:
                if time_seprator not in i:continue
                timeList.append(i)
    
    for i in timeList:
        index = i.find(time_seprator)
        hourString = i[:index]
        hourMap[hourString] = hourMap.get(hourString,0) + 1

    sortedList = list()
    
    for k,v in hourMap.items():
        sortedList.append((k,v)) 
    
    sortedList.sort() 
    
    for k,v in sortedList:
        print k,v
except Exception as e:
    print "Exception caught {}".format(e)
                    