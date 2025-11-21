import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
def num_letters(num_rows,num_columns):
    return((num_rows + num_rows) + (num_columns + num_columns) - 4)
    
assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns
assert num_letters(
assert num_letters(
assert num_letters(
assert num_letters(
print("assertions checked.")
