#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
import json 
import pandas as pd
import argparse 
parser = argparse.ArgumentParser() 
parser.add_argument("--dataset_root", required=True) 
res = parser.parse_args() 

dataset_root = res.dataset_root

files = [] 
for file in os.listdir(dataset_root): 
    if file[-4:] == "json": 
        files.append(file) 
objs = [] 
for f in files: 
    with open(dataset_root + f, 'r') as file: 
        objs += json.load(file)
pd.DataFrame(objs).to_csv(dataset_root + "data.csv", index=False)


# In[ ]:




