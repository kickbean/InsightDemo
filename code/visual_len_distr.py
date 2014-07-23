'''
Created on May 6, 2014

@author: Songfan
'''
import pandas as pd
import matplotlib

len_df = pd.DataFrame.from_csv('../data/len.csv',index_col='subject')
#print len_df
print len_df['toyota']
#print len_df['s002']
len_df.plot()