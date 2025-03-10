# problem 4

import os

# divide_list: list -> list list
# purpose: divide_list takes in a list of two elements and divides that list
#   into a list containing two lists each containing a substring split by the
#   character '-'
# example: divide_list(['5-96', '6-99']) -> (['5', '96'], ['6', '99'])
def divide_list(list1):
    first_nums = list1[0]
    second_nums = list1[1]

    return first_nums.split('-'), second_nums.split('-')

# either_subset: set set -> int
# purpose: either_subset determines whether one of the two sets given is a
#   subset of the other.  returns 1 if one is, and 0 otherwise
# example: either_subset({1,2,3}, {1,2,3,4}) -> 1
def either_subset(set1, set2):
    if set1.issubset(set2) or set2.issubset(set1):
        return 1
    else:
        return 0



# flag_intersection: set set -> int
# purpose: flag_intersection takes two sets and determines if they intersect, returning
#   a 1 if they do and 0 otherwise
# example: flag_intersection({1,2,3}, {3,4,5}) -> 1
def flag_intersection(set1, set2):
    if set.intersection(set1, set2):
        return 1
    else:
        return 0

# setify: list list -> set set
# purpose: converts the two lists provided into sets
# example: setify([1,2,3], [4,5,6]) -> {1,2,3} {4,5,6}
def setify(list1, list2):
    return set(list1), set(list2)

# open and split file
f = open('input', 'rt')
input_data = f.read()
dataList = input_data.split(os.linesep)

splitList = [x.split(' ') for x in dataList]
splitList.pop()

num_list = [x[0].split(',') for x in splitList]
num_list = [divide_list(x) for x in num_list]

# create list of range taken from numbers in the input
long_num_list = [[list(range(int(x[y][0]) , int(x[y][1]) + 1)) for y in range(2)] for x in num_list]

long_num_set = [setify(x[0], x[1]) for x in long_num_list]

flag_list = [either_subset(x[0], x[1]) for x in long_num_set]

intersection_list = [flag_intersection(x[0], x[1]) for x in long_num_set]



