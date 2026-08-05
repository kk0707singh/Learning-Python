# array library
import array
arr = array.array('i', [1,2,3,4])
print(arr)

# math function library
import math
print(math.sqrt(9))
print(math.pi)
print(math.sqrt(49))

# random library
import random
print(random.randint(20,30))
fruits = ['apple', 'banana', 'kela', 'keli']
print(random.choice(fruits))

# file and directory access
import os
print(os.getcwd())
print(os.path.exists("/Users/a2251/Desktop/Python Programing/Chapter-11-Standard-Library-Overview/source.txt"))


# high level operations on file and collection of files
import shutil
shutil.copyfile('/Users/a2251/Desktop/Python Programing/Chapter-11-Standard-Library-Overview/source.txt', '/Users/a2251/Desktop/Python Programing/Chapter-11-Standard-Library-Overview/destination.txt')



# data serialisation 
import json
data = {'name':'Krishna', 'age': 25}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))


# working with csv library:
import csv
with open('/Users/a2251/Desktop/Python Programing/Chapter-11-Standard-Library-Overview/example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Krishna', 26])


with open('/Users/a2251/Desktop/Python Programing/Chapter-11-Standard-Library-Overview/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



# date-time library:
from datetime import datetime, timedelta
now = datetime.now()
print(now)

yesterday_date = now-timedelta(days=1)
print(yesterday_date)

# time:
import time
print(time.time())
# time.sleep(10)

print(time.time())



# regular expression: we are going to match for example digit:

import re
patterns = r'\d+'
text = 'there are 456 apple and 12 is rotten'
match = re.search(patterns,text)
print(match.group())