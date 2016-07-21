# coding: utf-8
import pandas as pd


f = pd.read_csv("http_only.csv")
f["pictures"]
f
original = pd.read_csv("porsche.csv")
original
original.columns.values
headers = list(original.columns.values)
headers
headers.remove("address.country")
headers
clean_headers_one = ['title', 'source', 'ref', 'pictures', 'active']
clean_headers_one.sort()
clean_headers_one
f[clean_headers_one]
header_pos = []
for header in clean_headers_one:
    header_pos.append([header, headers.index(header)])
    
header_pos
headers_without_active = header_pos[1:]
headers_without_active
final_headers = headers_without_active[0] + headers_without_active[2:]
final_headers
final_headers = [headers_without_active[0]] + headers_without_active[2:]
final_headers
wanted_headers_pos = []
wanted_headers_pos = [30, 41, 42]
f[wanted_headers_pos]
new_reader = pd.read_csv("porsche.csv")
filtered_reader = new_reader[wanted_headers_pos]
filtered_reader.columns.values
new_reader = pd.read_csv("porsche.csv")
new_read[30]
new_reader[30]
get_ipython().magic(u'save test_pandas_csv')
get_ipython().magic(u'save test_pandas_csv 1-35')
