# coding: utf-8
import pandas as pd


def filter_chosen_columns(csv_source, csv_dest, columns):
    full_csv = pd.csv_reader(csv_source)
    full_csv = pd.read_csv(csv_source)
    new_csv = full_csv[columns]
    new_csv.to_csv(csv_dest, index=False)
