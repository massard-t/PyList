# coding: utf-8
import azure.storage.blob
import re
import time
import datetime


blob_service = azure.storage.blob.BlockBlobService(account_name, account_key)
current_blobs = []
for blob in blob_service.list_blobs(container_name):
    current_blobs.append(blob.name)

def g_timestamp(name):
    matches = re.search("/\d{8}/", name)
    if matches:
        return (matches.group(0)[1:-1], name)
    return False

blobs_to_delete = map(timestamp_check_deletion, current_timestamps)

def timestamp_check_deletion(blob_timestamp):
    date_format = "%Y%m%d"
    today = time.strftime(date_format)
    today_date = datetime.datetime.strptime(today, date_format)
    blob_date = datetime.datetime.strptime(blob_timestamp[0], date_format)
    if (abs((today_date - blob_date).days)) != 0:
        return blob_timestamp


blobs_to_delete = map(timestamp_check_deletion, current_timestamps)
filter(None, blobs_to_delete)
# DONE !
