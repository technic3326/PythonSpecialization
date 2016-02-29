import re

fileName = raw_input("Enter the file name: ")
file_handle  = open(fileName)

num_List = list()
for line in file_handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            num_List.append(int(number))
    
print num_List

if(len(num_List) > 0):
    print sum(num_List)
else:
    print "Empty list Found"