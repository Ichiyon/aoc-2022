# problem 5
import os

#list_1 = ['r','c','h']
#list_2 = ['f','s','l','h','j','b']
#list_3 = ['q','t','j','h','d','m','r']
#list_4 = ['j','b','z','h','r','g','s']
#list_5 = ['b','c','d','t','z','f','p','r']
#list_6 = ['g','c','h','t']
#list_7 = ['l','w','p','b','z','v','n','s']
#list_8 = ['c','g','q','j','r']
#list_9 = ['s','f','p','h','r','t','d','l']



list_1 = []                    
list_2 = []        
list_3 = []    
list_4 = []    
list_5 = []
list_6 = []                
list_7 = []
list_8 = []            
list_9 = []

lists_list = {
    1 : list_1,
    2 : list_2,
    3 : list_3,
    4 : list_4,
    5 : list_5,
    6 : list_6,
    7 : list_7,
    8 : list_8,
    9 : list_9
}

# move_to: int int int -> nil
# purpose: pops item from list[pos1] and sends it to list[pos2] as many times
#   as num_moves specifies
# example: move_to(1, 2, 1) -> nil ([1, 2, 3], [1,2,4] -> [1,2], [1,2,4,3])
def move_to(num_moves, pos1, pos2):
    for x in range(num_moves):
        lists_list[pos2].append(lists_list[pos1].pop())

def move_to_pt2(num_moves, pos1, pos2):
    temp_list = []
    for x in range(num_moves):
        temp_list.extend(lists_list[pos1].pop())
    temp_list.reverse()
    lists_list[pos2].extend(temp_list)

f = open('input', 'rt')
input_data = f.read()
dataList = input_data.split(os.linesep)
dataList.pop()

# list of enumerated lists, used to get the letters assigned to each crate, the
# enumeration is used to know the position the letters will appear by the formula
# (int(pos/4) + 1)
expanded_list = [list(enumerate(x)) for x in dataList[0:8]]

# get instructions from input and put them into the instructions variable
tmp = [x.split() for x in dataList[10:]]
instructions = [[int(x) for x in y if x.isdigit()] for y in tmp]

# populate starting crate stacks
tmp = [[lists_list[int(x[0]/4) + 1].insert(0, x[1])
        for x in y if x[1].isalpha()]
       for y in expanded_list]

#[move_to(*x) for x in instructions]
[move_to_pt2(*x) for x in instructions]

print(list_1[-1],list_2[-1],list_3[-1],list_4[-1],
      list_5[-1],list_6[-1],list_7[-1],list_8[-1],list_9[-1])
