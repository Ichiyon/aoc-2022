import os

f = open('input', 'rt')
input_data = f.read()
dataList = input_data.split(os.linesep + os.linesep)

splitList = [x.split('\n') for x in dataList]
splitList = [list(filter(lambda n: n != '', x)) for x in splitList]
intList = [[int(y) for y in x] for  x in splitList]
sumList = [sum(x) for x in intList]
sumList.sort()
print(sumList[254])
print(sumList[254] + sumList[253] + sumList[252])




# newList = [x.count('') for x in splitList]
