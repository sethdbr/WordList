import numpy as np
def num_letters(num_rows,num_columns):
    return((num_rows + num_rows) + (num_columns + num_columns) - 4)
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
ls = []
rows,columns = data.shape
c1=0
c2=0
r1=1
r2=1
while c1 < columns:
    ls.append(str(data[0,c1]))
    c1 += 1
while c2 < columns:
    ls.append(str(data[5,c2]))
    c2 += 1
while r1 < rows-1:
    ls.append(str(data[r1,0]))
    r1 += 1
while r2 < rows-1:
    ls.append(str(data[r2,6]))
    r2 += 1
print(ls)
assert len(ls) == num_letters(rows, columns)
words = [] 
rows, columns = data.shape  
c1=0
c2=0
r1=1
r2=1
while c1 < columns-1:
    words.append(str(data[0,c1])+str(data[0,c1+1]))
    c1 += 1
while c2 < columns-1:
    words.append(str(data[5,c2])+str(data[5,c2+1]))
    c2 += 1
while r1 < rows-2:
    words.append(str(data[r1,0])+str(data[r1+1,0]))
    r1 += 1
while r2 < rows-2:
    words.append(str(data[r2,6])+str(data[r2+1,6]))
    r2 += 1
print(words)
assert len(words) == num_letters(rows, columns)
print('assertment done')
