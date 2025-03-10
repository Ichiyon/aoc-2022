# problem 2

import os

rock = {
    'name' : 'rock',
    'weakTo' : 'paper',
    'strongTo' : 'scissors',
    'value' : 1
}

paper = {
    'name' : 'paper',
    'weakTo' : 'scissors',
    'strongTo' : 'rock',
    'value' : 2
}

scissors = {
    'name' : 'scissors',
    'weakTo' : 'rock',
    'strongTo' : 'paper',
    'value' : 3
}

decryption = {
    'A' : rock,
    'B' : paper,
    'C' : scissors,
    'X' : rock,
    'Y' : paper,
    'Z' : scissors

}

reference = {
    'paper' : 'Y',
    'rock' : 'X',
    'scissors' : 'Z'
}

strategy_play = {
    'X' : 'lose',
    'Y' : 'tie',
    'Z' : 'win'
}

# rps_compare: list -> int
# purpose: rps_compare determines which player wins a rock paper scissors game
#   and returns a value based on the outcome and item chosen.  The string that
#   makes up each list element are compared to the decryption dictionary to get
#   which item was chosen (which is also a dictionary containing the value of the choice)
# example: rps_compare(['A', 'X']) = rps_compare(rock, rock) -> 4
def rps_compare(choices):
    npc = decryption.get(choices[0])
    pc = decryption.get(choices[1])
    
    # win, loss, and tie respectively
    if pc['strongTo'] == npc['name']:
        return  pc['value'] + 6
    elif pc['weakTo'] == npc['name']:
        return  pc['value'] + 0
    else:
        return pc['value'] + 3

# compare_pt2: list -> int
# purpose: determines the desired win-loss state and sends the values necessary
#   to achieve it to rps_compare
# example: compare_pt2(['A', 'Y']) -> 4
    
def compare_pt2(strategy):
    npc = decryption.get(strategy[0])
    desired_state = strategy_play.get(strategy[1])
    if desired_state == 'tie':
       return rps_compare(list((strategy[0], strategy[0])))
    elif desired_state == 'lose':
        pc = npc['strongTo']
        return rps_compare(list((strategy[0], reference.get(pc))))
    else:
        pc = npc['weakTo']
        return rps_compare(list((strategy[0], reference.get(pc))))
    
f = open('input', 'rt')
input_data = f.read()
dataList = input_data.split(os.linesep)

splitList = [x.split(' ') for x in dataList]

# the final element is empty because it contains a line ending
# so remove it
splitList.pop()

sum([rps_compare(x) for x in splitList])
sum([compare_pt2(x) for x in splitList])
