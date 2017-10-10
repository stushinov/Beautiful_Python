
# As a person who come's from languages such as C# and Java, I misunderstood how the for-loop in python worked.

# The misunderstood range function.

# As a novice in python
# I thought that
#
#                   for(int i = 0; i <=10; i++) {
#                       #code here
#                   }
#

# Is the same as
#
#                   for x in range(10):
#                       #code here
#


# Naturally I was wrong. Therefore this led to, slow and ugly to read python code.


# Let me show you what I mean:


# How does one print the elemnts of a list using a for-loop.
names = ['Jhonatan', 'Marrie', 'Steve', 'Ashley']

# The wrong way
for i in range(len(names)):
    print(names[i])

# This is the way most of python newbies will do it.
# It does seem logical to take the length of a list and do iterations matching its length
# taking and printing the i-th element of the list.



# The correct way
for name in names:
    print(name)


# A thing one might not realize when they just get into python, is that
# although it is called a 'for' loop in python the 'for' loop is more like a 'for each' loop
# respectively to languages such as Java, C#, JS.