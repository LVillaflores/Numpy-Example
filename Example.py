import numpy as np

a = np.arange(15).reshape(3, 5)  # Create array using numpy with 3 rows and 5 columns
b = np.arange(15) ** 2  # Array with range 15 raised to 2
b = b.reshape(3, 5)  # Reshape array to have 3 rows and 5 columns
c = np.arange(20)

print('Array a')

for i in a:  # Iterate over values of array a
	print(i ** (1 / 3.))  # Raise values by 1/3

print('--------------------------------------------------------')
print('Values of array b:')

for element in b.flat:  # Iterate over all elements of the array
	print(element)  # Divides each element by 3 then prints out

for e in c:
	print(e)
