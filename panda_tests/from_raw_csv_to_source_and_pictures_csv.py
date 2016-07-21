# coding: utf-8
import pandas as pd


existing_csv = pd.read_csv('20000result.csv')
csv_without_na = existing_csv.dropna()
csv_without_na.to_csv('clean_20000results.csv')
csv_without_na.source.unique()
csv_without_na.keys()
csv_without_na[0]
csv_without_na['0']
header_csv['source'] = csv_without_na['0']
csv_without_na.to_csv('clean_20000results.csv', index=["row", "source", "pictures"])
csv_without_na.columns
csv_without_na.columns = ["ad_number", "source", "pictures"]
csv_without_na.columns
csv_without_na
csv_without_na.drop("row_number")
csv_without_na.drop("ad_number")
csv_without_na.drop("ad_number")
csv_without_na.columns
csv_without_na.drop("ad_number", 1)
final_csv = csv_without_na.drop("ad_number", 1)
final_csv
final_csv.to_csv("final_20000.csv")
get_ipython().magic(u'save from_raw_csv_to_source_and_pictures_csv 1-23')
