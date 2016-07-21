# coding: utf-8
import pandas as pd
data_frame_from_list = pd.DataFrame(data_to_save)
data_frame_from_list
with open('test_append_csv.csv', 'a') as f:
    data_frame_from_list.to_csv(f, header=False)
    
