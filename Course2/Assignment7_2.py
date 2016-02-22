# Assignment 7.2
fileName =  raw_input("Enter the File name:")
count = 0
number = 0
try:
    fileHandle = open(fileName)
except:
    print "Please enter a valid file Name"
    exit()
 
try:
    for line in fileHandle:
        if not line.startswith("X-DSPAM-Confidence"):
            continue
        else:
            count = count + 1
            interestedLine = line
            position = interestedLine.find('0')
            number = number + float(interestedLine[position:])
             
    averageOf = number/count
    print "Average spam confidence: ",averageOf
except Exception as e:
    print "Error in processing line {}".format(e)