# problem 3

import os

# get the intersection of the two lists sent
#def intersection(lst1, lst2):
 #   lst3 = [value for value in lst1 if value in lst2]
 #   return lst3

# split the string 'pouches' into two equal size substrings
def splitter(pouches):
    left_pouch = pouches[0:(int(len(pouches)/2))]
    right_pouch = pouches[(int(len(pouches)/2)) : len(pouches)]
    return [left_pouch, right_pouch]

def setify(list1, list2):
    return set(list1), set(list2)



# programmatically create dictionary of letters and priorities
ascii_low = list(range(97, 123))
ascii_up = list(range(65, 91))
priority_list = list(range(1, 53))

ascii_both = ascii_low + ascii_up
key_list = [chr(d) for d in ascii_both]

priority = dict(zip(key_list, priority_list))

# open and split file
f = open('input', 'rt')
input_data = f.read()
dataList = input_data.split(os.linesep)

splitList = [x.split(' ') for x in dataList]
splitList.pop()

dupe_letters = [set.intersection(*setify(*splitter(x[0]))) for x in splitList]
