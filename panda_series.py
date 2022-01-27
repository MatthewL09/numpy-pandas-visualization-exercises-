from lzma import MODE_FAST
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(fruits)
## EXERCISES PART 1

# 1 
fruits
fruits.size
fruits.shape
fruits.count()

#2
fruits.index
# operational output as if you call range

list(fruits.index)

#3
fruits.values

#4
type(fruits.values)
fruits.dtype
#'O' points to an object, or a string type

fruits.dtype == 'O'

#5
print(fruits.head(5))
# 5 is the DEFAULT

fruits.tail(3)

fruits.sample(2)

#6
fruits.describe()
# looking a categorical values instead of numerical values


#7
fruits.unique()
fruits.value_counts()
fruits.value_counts().index

#8
fruits.value_counts()

#9
fruits.mode()
fruits.value_counts().nlargest(n=1, keep='first')

# everything excluding kiwi and mango occur once
fruits.value_counts().head(1)

#10
fruits.value_counts().nsmallest(n=1, keep='all')

## EXERCISES PART 2
#

#1
fruits.str.capitalize()

#2

fruits.apply(lambda x: str(x.count('a')))
                    #^x + 'count of a:'
fruits.str.count('a').sum()

#3
vowels = list('aeiou')
vowels
def count_vowels(fruit):
    return len([letter for letter in fruit.lower() if letter in vowels])

count_vowels()

v_counts = fruits.str.lower().str.count('[aeiou]')
v_counts

a = fruits.str.count('a')
e = fruits.str.count('e')
i = fruits.str.count('i')
o =fruits.str.count('o')
u = fruits.str.count('u')

a + e + o + i + u

#4
length = fruits.str.len().max()
length
max(fruits, key = len)

# 5 
more_than_five = fruits[fruits.str.len() > 4]
more_than_five

fruits.str.len() > 4

#6
list(lambda f: (f.count('o') >1], fruits))


def ele(x):
    count = [0]
    vowel = 'aeiou'
    for vowel in x:
        count +=1
    return count

print(fruits[fruits.str.count('o')>1])

fruits.apply(lambda fruit: fruit.count('o') > 1)

#7
fruits[fruits.str.contains('berry')]

fruits.apply(lambda x: 'berry' in (x))

#8
fruits[fruits.str.contains('apple')]

#9
vowel_counts = fruits.str.count('[aeiou]')
vowel_counts

def v_count(word):
    v_count=0
    for vowel in 'aieouAEIOU':
        vowel_count += word.count(vowel)
    return v_count

print(max(fruits, key=vowel_count))

## EXERCISE 3
letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters)
letters

#1
letters.value_counts().nlargest(n=1, keep='first')

#2
letters.value_counts().nsmallest(n=1, keep='first')

#3
vowels = list('aeiou')

letters.str.lower().str.count('[aeiou]').sum()

(letters.str.lower().isin(['a', 'e', 'i','o', 'u'])).sum()

#4
letters.str.lower().str.count('[^aeiou]').sum()

(~letters.str.lower().isin(['a', 'e', 'i','o', 'u'])).sum()

#5
letters.str.upper()

#6
letters.value_counts().head(6)

letters.value_counts().head(6).plot( kind = 'barh',
color = 'blue',
ec= 'green',
width = .8)

plt.title('Top 6 letters')

## NEW SERIES

numbers = pd.Series(list(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']))

numbers_as_floats = numbers.str.replace('$','').str.replace(',','').astype('float')
numbers_as_floats

numbers_as_floats.size

#4
max = numbers_as_floats.max()

# 5
min = numbers_as_floats.min()

# 6
max - min

#7
pd.cut(numbers_as_floats)

#8


# ANOTHER SERIES
exam_scores = pd.Series(list(    [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]))
exam_scores

#1

#1

#3
exam_scores.plot.hist(colo ='thistle')

#4
curve = 100 - exam_scores.max()
curve

curved_score = 

# define bin edges
bin_edges = [0, 70, 75, 80, 90, 101]

bin_labels = ['F', 'D', 'C', 'B', 'A']

pd.cut