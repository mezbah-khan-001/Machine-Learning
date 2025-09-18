   # Helo wrold 
   # lets code the program .... 
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
# Unused imports removed to speed up import time and shrink dependencies
from pathlib import Path
# Optional pretty printer, falls back to built-in print if not available
try:
    from icecream import ic  # type: ignore
except ImportError:  # pragma: no cover
    def ic(*args, **kwargs):
        print(*args)

    # lets load the dataset ---> 
data_path = Path('IMCD_DATA.csv')
if data_path.exists() : 
    data = pd.read_csv(data_path) 
    ic(data.head())
else : 
    raise FileNotFoundError (f'This file path {data_path} doest founded .... ')

   # lets check the dataas informations ---> 
print(data.head(5))
   
   # The dataset have some NaN Vaues and  float64(2), int64(1), object(13)

   # Lets check the datas outliers and NaN values also 
ic (data.isnull().sum())  # The [Certificate,Meta_score,Gross] columns have NaN values 
ic (data.describe())      # the columns seems to have NaN values lets identify 
ic (data.columns)
   
   # lets check the datas outliers with graph --> 
plt. figure(figsize=(10,7))
sns . boxplot(x='Meta_score',data = data,color='g')  # The columns have just 1000 rows, So doest need (Boxnplot)
plt . title('This is Meta_score columns outliers graph ')
plt. grid(True) 
plt . show()   # The data is clean 

    # lets fill the NaN values with mean and mode 
ic(data['Certificate'].dtype)  # object
data['Certificate'].bfill(inplace=True)  # Correct use of bfill

ic(data['Meta_score'].dtype)  # Float
data['Meta_score'].fillna(data['Meta_score'].mode()[0], inplace=True)  # Mode fill for numeric data

ic(data['Gross'].dtype)  # Object
data['Gross'].ffill(inplace=True)  # Correct use of ffill

    # Lets recheck the datas structure 
ic (data.info())   # Everything is good 
   
   # Lets encode the data --> 
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder() 
output_01 = pd . DataFrame() 
data_columns_01 = data.select_dtypes(['object']).columns
for col in data_columns_01 : 
    output_01[col + "en"] = label.fit_transform(data[[col]])
    ic (output_01) 
   
   # lets replace the datas--> 
data = data.drop(columns=data_columns_01)    # Drop original object columns
data = pd.concat([data, output_01], axis=1)  # Concatenate the encoded columns
ic(data.info())
  
   # Lets select the features for systemical functions ---> 
x = data[['Series_Titleen','Released_Yearen']]

movie_rating =data.groupby('Series_Titleen')['IMDB_Rating'].mean() 
def recommend_movie(top_n=5):
   top_movies = movie_rating.sort_values(ascending=False).head(top_n)
   print(f"Top {top_n} recommended movies based on average ratings:")
   print(top_movies)

# Example usage
recommend_movie(top_n=5)
   

      # Top 5 recommended movies based on average ratings:
      # Series_Titleen  ---> 
      # 875 :   9.3
      # 786 :   9.2
      # 766 :   9.0
      # 787 :   9.0
      # 1   :   9.0