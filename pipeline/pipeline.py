import sys
import pandas as pd

print("Arguments passed: ", sys.argv)
month=sys.argv[1]
print("Month: ",month)

df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
df['Month']=month
df.to_parquet(f'data_{month}.parquet')
print("DataFrame:\n",df)