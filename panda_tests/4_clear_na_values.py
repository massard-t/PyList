# coding: utf-8
import panda as pd


def clear_na_from_csv(csv_source, csv_dest):
    existing_csv = pd.read_csv(csv_source)
    csv_without_na = existing_csv.dropna()
    csv_without_na.to_csv(csv_dest)

