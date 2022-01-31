from pydataset import data
import pandas as pd
import numpy as np

## STUDENT GRADES DATAFRAME
## NUMBER 1
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})\

df

#Number 1a.
df['passing_english'] = df.english > 70

#Number 1b.
df.sort_values('passing_english')

#Number 1c.
df.sort_values(by=['passing_english', 'name'])

#Number 1d.
df.sort_values(by=['passing_english', 'english']), ascending == [False, False]

#Number 1e.
df['overall_grade'] = ((df.english + df.math + df.reading) / 3).astype(int)
df

df['overall_grade'] = round(df[['math', 'english', 'reading']].mean



pd.options.display.float_format = '{:.2f}'.format
df


## MPG dataframe
data('mpg', show_doc=True)

mpg = data('mpg')
mpg
# Number 2a - 234 rows x 11 columns
mpg.shape

# Number 2b. - Object Type
mpg.columns.dtype

# Number 2c. 
mpg.info
mpg.describe

# Number 2d. ## could put them both together rename(columns{'cty': 'city', 'hwy': 'highway'})
mpg = mpg.rename(columns={'cty': 'city'})

#Number 2e.
mpg = mpg.rename(columns={'hwy': 'highway'})

#Number 2f. - no cars have better city than highway mpg
bool_series = mpg.city >mpg.highway
bool_series.head()
mpg[bool_series
]
mpg[mpg.city > mpg.highway].any()

#Number 2g.
mpg['mileage_difference'] = mpg.highway - mpg.city
mpg.mileage_difference

#Number 2h. Two returned rows. honda & volkswagon
mpg.nlargest(n=1, columns = 'mileage_difference',keep='all')

#Number 2i. - average mileage
mpg['average_mileage'] = (mpg.highway + mpg.city) / 2
mpg.average_mileage

mpg[['city', 'highway']].mean(axis=1)

# Number 2j. - volkswagon Jetta 6cyl has lowest. volkswagon jetta 4cyl has highest
mpg[mpg['class'] == 'compact'].nsmallest(n=1, columns = 'highway' , keep = 'all')
mpg.nsmallest(1, 'highway', keep='all').head(1)

mpg[mpg['class'] == 'compact'].nlargest(n=1, columns = 'highway', keep = 'all')

#Number 2k. - Dodge caravan
mpg[mpg['manufacturer'] =='dodge'].nlargest(n=1, columns = 'average_mileage', keep='all')

bool_series = mpg.manufacturer =='dodge'
bool_series.head
dodges = mpg[bool_series]
dodges.shape


## MAMMALS DATAFRAME

mammals = data('Mammals')
mammals.sample(4)

#Number 3a -- 107 rows, 4 columns
mammals.info()

# Number 3b. -- dtypes bool(2), float64(2)
mammals.info()

#Number 3c.
mammals.info()
mammals.describe()

mammals.weight.hist()


#Number 3d -- weight is 55

mammals.speed.hist()

mammals.nlargest(1,'speed', keep= 'all').weight

mammals[mammals.speed == mammals.speed.max()].weight.values[0]

#Number 3e. %9.35

bool_series = mammals.
percentage = (mammals[mammals.specials])['specials'].count() / mammals['specials'].count() * 100
percentage.round(2)
round((len(fast_hoppers) / len(mammals))) * 100, 2


# Number 3f. %6.54

faster_than = mammals[(mammals.hoppers) & (mammals.speed > mammals.speed.median())]['specials'].count()
percent_faster = faster_than / mammals.specials.count() * 100
percent_faster