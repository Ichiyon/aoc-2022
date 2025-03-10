# problem 3

import os

# get the intersection of the two lists sent
#def intersection(lst1, lst2):
 #   lst3 = [value for value in lst1 if value in lst2]
 #   return lst3

# splitter: string -> string string 
# purpose: split the string 'pouches' into two equal size substrings
# example: splitter('abcd') -> 'ab' 'cd'
def splitter(pouches):
    left_pouch = pouches[0:(int(len(pouches)/2))]
    right_pouch = pouches[(int(len(pouches)/2)) : len(pouches)]
    return [left_pouch, right_pouch]

# setify: list list -> set set
# purpose: converts the two lists provided into sets
# example: setify([1,2,3], [4,5,6]) -> {1,2,3} {4,5,6}
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

# dummy function to hold part one of the problem so I didn't have to erase
# or comment it out
def part1():
    
    dupe_letters = [set.intersection(*setify(*splitter(x[0]))) for x in splitList]
    dupe_letters = [list(x) for x in dupe_letters]

    priority_number_list = [priority.get(x[0]) for x in dupe_letters]
    sum(priority_number_list)

letter_list = [set(x) for x in splitList]
letter_set = [set(x[0]) for x in splitList]

set_group_intersection = [set.intersection(letter_set[x], letter_set[x+1],
                                           letter_set[x+2]) for x in range(0,300,3)]

list_group_intersection = [list(x) for x in set_group_intersection]
priority_number_list = [priority.get(x[0]) for x in list_group_intersection]
sum(priority_number_list)


