# coding: utf-8
for hit in hits:
    curr = []
    curr.append(hit["_source"]["source"])
    curr.append(hit["_source"]["pictures"])
    data_to_save.append(curr)
    
