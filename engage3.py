# John Halstead, Ph.D., Engage3 data challenge, January 4, 2020
#%%
# libraries
import numpy as np
import pandas as pd
#%%
# data
prices = pd.read_csv("/Users/johnhalstead/PycharmProjects/engage3/prices.csv")
auditors = pd.read_csv("/Users/johnhalstead/PycharmProjects/engage3/auditors.csv")
stores=pd.read_json("/Users/johnhalstead/PycharmProjects/engage3/stores.json")
#%%
# check
print(prices.head())
print(auditors.head())
print(stores.head())
#%%
# merge prices and stores
combined = pd.merge(prices, stores, on='Store ID')
#%%
# create the pivot table for price on banner and upc by region
MyPivot = combined.pivot_table('Price',['Banner','UPC'],'Region')
print(MyPivot.head())
#%%
# export to csv
export_csv = MyPivot.to_csv (r"/Users/johnhalstead/desktop/EngageResult.csv", header=True)
#%%
# a different pivot table view on price on UPC then banner by region
MyOtherPivot = combined.pivot_table('Price',['UPC','Banner'],'Region')
print(MyOtherPivot.head())
#%%
# export the other view to csv

export1_csv = MyOtherPivot.to_csv(r"/Users/johnhalstead/desktop/EngageResultOther.csv", header=True)
#%%
# Let's try Z scores to ID outliers
from scipy import stats
zScore = np.abs(stats.zscore(MyPivot))
print(zScore)
# didn't work

