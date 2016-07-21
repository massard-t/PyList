# coding: utf-8
import pandas as pd


f = pd.read_csv("http_only.csv")
original = pd.read_csv("porsche.csv")
headers = list(original.columns.values)
clean_headers_one = ['title', 'source', 'ref', 'pictures', 'active']
header_pos = []
for header in clean_headers_one:
    header_pos.append([header, headers.index(header)])
headers_without_active = header_pos[1:]
final_headers = [headers_without_active[0]] + headers_without_active[2:]
wanted_headers_pos = [30, 41, 42]
new_reader = pd.read_csv("porsche.csv")
filtered_reader = new_reader[wanted_headers_pos]
new_reader = pd.read_csv("porsche.csv")
