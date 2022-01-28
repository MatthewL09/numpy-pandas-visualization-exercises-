from pydataset import data
import pandas as pd
import numpy as np



## MPG dataframe
data('mpg', show_doc=True)

mpg = data('mpg')
# Number 2a - 234 rows x 11 columns
mpg.describe

# Number 2b. - Object Type
mpg.columns.dtype

# Number 2c. 
mpg.info
mpg.describe

# Number 2d.
mpg = mpg.rename(columns={'cty': 'city'})

#Number 2e.
mpg = mpg.rename(columns={'hwy': 'highway'})

#Number 2f. - no cars have better city than highway mpg
mpg[mpg.city > mpg.highway].any()

#Number 2g.
mpg['mileage_difference'] = mpg.highway - mpg.city
mpg.mileage_difference

#Number 2h. Two returned rows. honda & volkswagon
mpg.nlargest(n=1, columns='mileage_difference',keep='all')

#Number 2i.
mpg['average_mileage'] = (mpg.highway + mpg.city) / 2
mpg.average_mileage
