import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Number 1 - 5
len(a[a < 0])

# Number 2 - 5

len(a[a > 0])

# Number 3 - 3
b = a[a > 0]
len(b[b % 2 == 0])

# Number 4 - 10
plus_three = a + 3
plus_three
len(plus_three[plus_three > 0])

# Number 5 - 74.0 , 144.0
squared = a ** 2
squared.mean(), squared.std()

# Number 6
mean = a.mean()
mean
a - mean

# Number 7
score = (a - a.mean()) / a.std()
score



import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = a.sum()
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = a.min()
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = a.max()
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = a.mean()
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = a.prod()
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = a**2
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = a[a % 2 != 0]
odds_in_a


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a% 2 ==0]
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

b.sum(), b.min(), b.max(), b.prod()

average = b.sum() / (len(b))
average

squares = b ** 2
squares


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = b.prod()
product_of_b

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b**2
squares_of_b


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 ==1]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 ==0]
evens_in_b

# Exercise 9 - print out the shape of the array b.

b.shape

# Exercise 10 - transpose the array b.

b.transpose()


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(6,)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(1,6)

## Setup 3
c = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

c

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c.min(), c.max(), c.sum(), c.prod()

# Exercise 2 - Determine the standard deviation of c.

c.std()

# Exercise 3 - Determine the variance of c.

c.var()

# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

c.transpose()

# Exercise 6 - Get the dot product of the array c with c. 

c.dot(c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

(c * c.transpose()).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

(c * c.transpose()).prod()

## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

d

# Exercise 1 - Find the sine of all the numbers in d

np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)

# Exercise 4 - Find all the negative numbers in d

negative = d[d < 0]

negative

# Exercise 5 - Find all the positive numbers in d

positive = d[d > 0]

positive

# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.

values = (np.unique(d))

len(values)

np.l(values)

# Exercise 8 - Print out the shape of d.

d.shape

# Exercise 9 - Transpose and then print out the shape of d.

print(d.transpose())

# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape (9,2)