# In 'analyzer', define a function that calculates the average of the data.
from functools import reduce

def calculate_average(data):
    return reduce(lambda x, y: x+y, data)/len(data)


