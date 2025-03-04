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
