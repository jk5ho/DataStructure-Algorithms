"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

def areaCode(number):
  i = 1
  output = ""
  while(number[i] != ")"):
    output += number[i]
    i += 1
  return output

def mobilePrefix(number):
  return number[0:4]

output = set()
for entry in calls:
  if entry[0][0] == "(" and areaCode(entry[0]) == "080":
    if(entry[1][0] == "("):
      output.add(areaCode(entry[1]))
    elif(entry[1][0] == "9" or entry[1][0] == "8" or entry[1][0] == "7"):
      output.add(mobilePrefix(entry[1]))

codeList = list(output)
codeList.sort()

print("The numbers called by people in Bangalore have codes: ")
for code in codeList:
  print(code)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

total = 0
local = 0

output = set()
for entry in calls:
  if entry[0][0] == "(" and areaCode(entry[0]) == "080": 
    total += 1
    if entry[1][0] == "(" and areaCode(entry[1]) == "080": 
      local += 1

print("\n", (local/total)*100, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
