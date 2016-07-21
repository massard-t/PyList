# coding: utf-8
import pandas as pd


def filter_by_content(csv_name, columm_name, text_to_find, csv_dest):
    data = pd.read_csv(csv_name)
    newdata = data[text_to_find in data[column_name]]
    newdata = data[data[column_name].str.contains("http:")]
    content_http = data.query('"http:" in pictures')
    only_http = data_no_na[data_no_na[column_name].str.contains('http:')]
    only_http.to_csv("processed_file_only_http.csv", index=False)
    http_sources = only_http.source.unique()
    with open("sources_http.txt", 'w') as f:
        f.write('\n'.join(list(http_sources)))
    
