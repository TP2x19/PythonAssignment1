#####################################
#### EXERCISE 1 30 MARKS#######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 - 10 Points##
###############

# Given the string:
s = 'fullstackslp'

# Use indexing to print out the following:
# 'f'          ----- print(s[-12])
print(s[0])
# 'p'          ----- print(s[-11])
print(s[-1])
# 'stack'
print(s[4:9])
# 'slp'       ------ print(s[9:])
print(s[-3:])
# 'cks'       ------ print(s[7:10])
print(s[-5:-2])

# Bonus: Use indexing to reverse the string
mystring = s [::-1]
print(mystring)

#the slice statement [::-1] means start at the end of the string and end at position 0,
#move with the step -1, negative one, which means one step backwards.

###############
## Problem 2 - LISTS - 5 Marks##
###############

# Given this nested list:
l = [3,7,[5,[1,4,'hello']]]
# Reassign "hello" to be "goodbye"
l[2][1][2] = "goodbye"
print(l)

###############
## Problem 3 - DICTIONARIES - 6 Marks##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1])

###############
## Problem 4 - SETS - 4 Marks##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(mylist)
newUniqueValues = set(mylist)
print(newUniqueValues)

###############
## Problem 5  - FORMATTING - 5 Marks##
###############

# You are given two variables:
age = 45
name = "Kyle"

# Use print formatting to print the following string:
#"Hello my dog's name is Kyle and he looks 45 years old"
print("Hello my dog's name is {} and he looks {} years old".format(name,age))
