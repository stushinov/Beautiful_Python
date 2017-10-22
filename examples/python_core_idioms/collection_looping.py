
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


# ------------------------------------------------------------------------------ #


# How does one print the elements of a list using a for-loop.
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


# ------------------------------------------------------------------------------ #


# Okay we get how to print the elements of a list but what happens if one wants to
# print both the element and its index, we must iterate over the list using its
# length in order to obtain each element and its index right ?!


# The wrong way
for i in range(len(names)):
    print(i, ' --> ', names[i])


# Nope, by looking into python's built-in functions we will find one whose name is
# enumerate(). What enumerate() does is to return
# a tuple containing the elements' index and the element itself.
# Let's see it in an example.


# The correct way
for i, name in enumerate(names):
    print(i, ' --> ', name)


# Isn't the code more readable now ?
# Yes it is and it is also faster !

# ------------------------------------------------------------------------------ #


# Let's get to the kinks. What if for example we had two lists (with different lengths)
# and we had to iterate over them ?


colors = ['red', 'blue', 'green', 'yellow']

animals = ['Lion', 'Monkey', 'Platypus', 'Crocodile', 'Elephant']


# The wrong way
for i in range(min(len(colors), len(animals))):
    print('The color is: ', colors[i], ' The animal is: ', animals[i])


# The most obvious way to do this is by taking the lengths of the two collections,
# compare them to see which one is smaller and then use it in the 'for' loop.

# Isn't it ugly ? 'range(min(len(collection_A), len(collection_B)))'.
# How about readability ? Performance ? Yes it is ugly, unreadable and slow,
# so let's fix it by introducing the zip() function.


# The correct way
for color, animal in zip(colors, animals):
    print('The color is: ', color, ' The animal is: ', animal)


#TODO: Any grammar mistakes here ?

# In a brief, what the 'zip()' function does is to take two collections
# and start iterating over them. When there are no more values in one of the
# two collections it just stops iterating. Pretty neat isn't.

#TODO: Can zip take more than 2 collections ?