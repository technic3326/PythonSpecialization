print "Hello World"
x = 2
y = 3
print "this Sum of", x, "and", y, "is:", x + y

if x > 1:
    print x, "In if"
else:
    print x, "in else"

while x > 0:
    print x, "in while"
    x = x - 1
    print "hi der"

print float(99)
print type(x)
print str(x)

#Raw input function

# ratePerHour = raw_input('Rate per hour?')
# numberOfHours = raw_input('number of Hours?')
# try:
#     salary = float(ratePerHour) * float(numberOfHours)
#     print 'your Salary is: ', salary
# except:
#     print "Error occured in calculating Salary"


for i in range(5):
    print i
    if i>2:
        print 'i is in If'
    elif i>3:
        print i
    print 'for loop i'

#Reqrite Pay Computation

def computePay(ratePerHour,numberOfHours):
    if numberOfHours > 40:
        salary = (1.5 * ratePerHour * (numberOfHours - 40)) + (ratePerHour * 40)
        return salary
    else:
        salary = ratePerHour * numberOfHours
        return salary

# inputNewRatePerHour = raw_input("Enter Rate per hour")
# inputNewNumberOfHours = raw_input("Enter number of hours")

# try:
#     newRatePerHour = float(inputNewRatePerHour)
#     newNumberOfHours = float(inputNewNumberOfHours)
#     salary = computePay(newRatePerHour, newNumberOfHours)
#    
# 
# except:
#     print "Error in Calculating salary"
# 
# print "The Final Salary is: ",salary
# 
# score = raw_input("Enter Score between 0.0 and 1.0: ")

# try:
#     scoreValue = float(score)
#     if scoreValue >= 0.9:
#          print "A"
#     elif scoreValue >= 0.8:
#          print "B"
#     elif scoreValue >= 0.7:
#         print "C"
#     elif scoreValue >= 0.6:
#          print "D"
#     elif scoreValue < 0.6:
#         print "F"
# 
# except:
#     print "Invalid Grade Entered"


smallestNumber = None
largestNumber = None

while True:
    inputNumber = raw_input("Enter the number")
    if inputNumber == "done":
        break
    if len(inputNumber)<1:
        break
    else:
        try:
            number = int(inputNumber)
            if smallestNumber is None:
                smallestNumber = number
            if largestNumber is None:
                largestNumber = number
            else:
                if number < smallestNumber:
                    smallestNumber = number
                if number > largestNumber:
                    largestNumber = number    

        except:
            print "Invalid Input" 
#         
print "Maximum is ",largestNumber
print "Minimum is ",smallestNumber
# print 'Welcome' + name

print "finish"
