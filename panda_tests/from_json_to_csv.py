# coding: utf-8
import json
import csv
import pandas
import sys


__author__ = 'theo'


def import_json(json_name="req1.json"):
    with open(json_name, 'r') as f:
        content = f.read()
    return content

def get_result_list(content):
    j_data = json.loads(content)
#   j_data.keys()
    l_j_results = j_data['hits']['hits']
    print("%s results !"%str(len(l_j_results)))
    return l_j_results, len(l_j_results)

def result_list_to_rows(l_j_results):
    rows = []
    for result in l_j_results:
        row = []
        if result['fields'].has_key('pictures'):
            pictures = result['fields']['pictures']
        else:
            pictures = None
        source = result['fields']['source'][0]
        row.append(source)
        row.append(pictures)
        rows.append(row)
    return rows


def rows_to_csv(rows, csv_name="20000result.csv"):
    csv_headers=["row_number", "source", "pictures"]
    data_to_save = []
    data_frame_from_list = pandas.DataFrame(rows)
    data_frame_from_list
    data_frame_from_list.to_csv(csv_name, headers=csv_headers)
    print("Created %s" % csv_name)

def main(): # TODO: Allow argument management
    content = import_json()
    l_j_results, len_l_j_results = get_result_list(content)
    rows = result_list_to_rows(l_j_results)
    rows_to_csv(rows)


if __name__ == '__main__':
    main()