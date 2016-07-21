# coding: utf-8
import json
with open("09ff.json", 'r') as f:
    newj = f.read()
    
newj
j = json.loads(newj)
j
j["hits"]
j["hits"]["hists"]
j["hits"]["hits"]
