# coding: utf-8
import pandas as pd


data = pd.read_csv(csv_name)
newdata = data["http:" in data['pictures']]
newdata = data[data['pictures'].str.contains("http:")]
data['pictures']
data['pictures']
content_http = data.query('"http:" in pictures')
content_http
data['pictures']
data[data['pictures'].str.contains("http:")]
data.dropna
data.dropna()
data[data['pictures'].str.contains("http:")]
data['pictures']
data_no_na = data.dropna()
data_no_na
data_no_na['pictures']
data_no_na[data_no_na['pictures'].str.contains('http:')]
only_http = data_no_na[data_no_na['pictures'].str.contains('http:')]
only_http
only_http.to_csv("processed_file_only_http.csv", index=False)
http_sources = only_http.source.unique()
http_sources
with open("sources_http.txt", 'w') as f:
    f.write('\n'.join(list(http_sources)))
    
