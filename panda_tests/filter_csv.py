# coding: utf-8
import pandas as pd
full_csv = pd.csv_reader("porsche.csv")
full_csv = pd.read_csv("porsche.csv")
keep_col = ["source", "pictures"]
new_csv = full_csv[keep_col]
new_csv.to_csv("clean.csv", index=False)
get_ipython().magic(u'pinfo %save')
