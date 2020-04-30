"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers = {}
for entry in calls:
    if entry[0] in numbers:
        numbers[entry[0]] = numbers[entry[0]] + entry[3]
    else:
        numbers[entry[0]] = entry[3]
    
    if entry[1] in numbers:
        numbers[entry[1]] = numbers[entry[1]] + entry[3]
    else:
        numbers[entry[1]] = entry[3]

max = 0
ret = None
for x in numbers:
    if int(numbers[x]) > max:
        max = int(numbers[x])
        ret = x

print(ret, " spent the longest time, ", max, " seconds, on the phone during September 2016.")
