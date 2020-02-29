# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import os
import csv
import numpy as np
import pandas as pd


# %%
index = pd.read_csv('passport-index-matrix.csv',index_col ='Passport')
index


# %%
rankIndex = index.clip_lower(0)
score = rankIndex.sum(axis=1)

#score.sort_values(by = '0', ascending = False)
rank = score.sort_values(ascending = False)
rank = pd.DataFrame(rank)
rank['Rank'] = np.arange(1, len(score)+1)
#rank
rank.to_csv('OrigRank.csv')


# %%
#np.repeat(score, len(score), axis=1)
#a= np.tile(score, (len(score),1))
#b = np.transpose(a)
rankIndex.iloc[0,1]


# %%
for i in range(len(score)):
    for j in range(len(score)):
        rankIndex.iloc[j,i] = rankIndex.iloc[j,i]*score[i]
    
rankIndex


# %%
rankIndex = rankIndex/100


# %%
passScore = rankIndex.sum(axis=1)
passScore = passScore.sort_values(ascending = False)
passScore


# %%
passRank = pd.DataFrame(passScore)
passRank['Rank'] = np.arange(1, len(passScore)+1)
passRank.to_csv('PassportRank1.csv')

