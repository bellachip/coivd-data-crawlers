#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:45:04 2020

@author: Bella
"""


import pandas as pd
import numpy as np



df = pd.read_csv("data/OR_death_cases.csv")

print(df.dtypes)

df_sorted_descending = df.sort_values(['cases'], ascending=False)

print(df_sorted_descending.head(15))

