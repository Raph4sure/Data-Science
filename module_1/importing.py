from module1 import add, multiply, sub
import os
import os.path
import platform
os.mkdir('name of dir') #creates a new dir inside the current directory
os.rmdir('name of dir') #removes dir from the current directory
from datetime import date, time, datetime, timedelta
import math
import random
# from random import *
import webbrowser
import calendar


"""
c = add(2,4)
d = multiply(2,4)
e = sub(2,4)

print(f"{c}")

print(f"{d}")

print(f"{e}")


print(os.getcwd())

print(os.listdir("."))

print(os.path.abspath('.'))

# print(os.environ)



print(platform.version())
print(platform.system())
print(platform.release())
print(platform.platform())
print(platform.win32_ver())


print('\n')

#os.path provides methods to extract info about paths and filenames


print(os.path.isdir(os.getcwd()))  #retrieves the current directory and checks if the dir exists
print(os.path.isfile('module1.py')) #checks if the file exists
print(os.path.exists(os.getcwd())) #retrives the current directory and checks if it exists
# print(os.path.getsize('RAG importing.py')) #retrieves the size of the file without opening it



# today = date.today()

time_now = datetime.time(datetime.now())

print (time_now)

# print(today)

print("//////////////////////////////////////////")



def main():
    
    today = datetime.now()
    
    wd = datetime.weekday(today)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    
    print(today)
    
    print(f"{today.strftime("%c")}")
    print(f"{today.strftime("%x")}")
    
    print(today.strftime('%I:%M:%S:%p'))
    print(today.strftime('%H:%M'))
    print(today.strftime('%I:%M'))
    
    print(wd)

    print(f"Today is the number {wd}")
    
    print(f"and today is {days[wd]}")

main()




#constructing a basic timedelta
my_timedelta = timedelta(days=10000, hours=8, minutes=15)
print(my_timedelta)


#printing today's date
print(datetime.now())

#print the date, 10000 days from now
print('\n\n10,000 days from now, the date would be: ' + str(datetime.now() + timedelta(days=10000)))
print("\n")


# print(dir(datetime))

# print(help(datetime))

# print(dir(math))
# print(help(math))


print("\n /////////////////////////////////////////////////")


# print(random())

# print(help(random))

print("\n /////////////////////////////////////////////////")


# returns an integer between the numbers specified, the numbers are inclusive

print(randint(3,7))

print(uniform(3,7))


print("\n /////////////////////////////////////////////////")


# The choice function

# it generates a random value from the sequence
# it used to choose a random element from a list


import random
my_list = ['NASA', 'Hannah', 7786, {'food': 'rice and beans'}]

print(random.choice(my_list))
print(choice(my_list))


#used the shuffle the elements in a list in place so they are in random order
shuffle(my_list)
print('\nAfter shuffling: ', my_list)

# The randrange function
for i in range(6):
    print(random.randrange(0, 101, 5))
    
# The sample function

c=list(range(0,20))
print(c)

#the sample function is used to return a list of unique elements choosen at random from the sequence
print(random.sample(c, 10))



# Webbrowser module
# This module is used to provide an interface to display web-based documents

# print(dir(webbrowser))

# print(help(webbrowser))



google = input("Enter Your Google search: ")
webbrowser.open_new_tab('https://www.google.ng/search?q=%s' % google)
"""


# Calendar module
# Displays the calendar

# print(dir(calendar))

# print(help(calendar))


year = 2026
month = 12

# print(calendar.month(year, month))

# print(calendar.calendar(year))

#operation 1 - calendar(year, w, l, c)
#displays the year, width of characters, number of lines per week and column seperators

# print(calendar.calendar(2024, 5, 1, 8))

#operation 2 - isleap()
calendar.isleap(2098)

#operation 3 - month(year, month, w, l)

print(calendar.month(2034, 5, 3, 1))