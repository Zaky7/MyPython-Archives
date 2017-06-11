#Counter is a subclass of
from collections import Counter                                                                                                                                                                                                         
'''
#Initialization using import counter
print( Counter(['B','A','B','C', 'A', 'A', 'C', 'C', 'D']) )

#initialise using the dictionary
print( Counter({'A':3,'B':2,'C':3,'D':1}))

#initializing using keyword
print(Counter(A=3,B=2,C=3,D=1))
'''

z=['blue','red','yellow','orange','blue','red']
col_count=Counter(z)

col=['blue', 'red', 'yellow']

for color in col:
    print(color,col_count[color])
