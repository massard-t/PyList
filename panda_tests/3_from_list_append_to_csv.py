# coding: utf-8
import pandas as pd


def write_to_csv(data_to_save, csv_file):
    data_frame_from_list = pd.DataFrame(data_to_save)
    try:
        with open(csv_file, 'a') as f:
            data_frame_from_list.to_csv(f, header=False)
    except Exception:
        return False
    return True
