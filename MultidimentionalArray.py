import numpy as np

# array = np.array('A')
# array = np.array([['A', 'B', 'C'], 
#                   ['D', 'E', 'F'], 
#                   ['G', 'H', 'I']])

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print(array.ndim)
word = array[0,0,2] + array[0,2,1]+ array[0,2,2]+ array[1,2,2] +array[0,0,0]+ array[0,2,0]
print(word)