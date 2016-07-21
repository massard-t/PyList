# coding: utf-8


existing_csv = pd.read_csv('test_append_csv.csv')
existing_csv.dropna()
existing_csv
csv_without_na = existing_csv.dropna()
csv_without_na
csv_without_na.to_csv('clean_csv.csv')
