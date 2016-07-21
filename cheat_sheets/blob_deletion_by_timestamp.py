# coding: utf-8
import azure.storage.blob
import re
import time
import datetime


def create_blob_service(ACC_NAME, ACC_KEY):
    blob_service = azure.storage.blob.BlockBlobService(account_name=ACC_NAME,
                                                       account_key)
    return blob_service


def get_blobs(blob_service, container_name):
    current_blobs = []
    for blob in blob_service.list_blobs(container_name):
        current_blobs.append(blob.name)
    return current_blobs


def g_timestamp(name):
    matches = re.search("/\d{8}/", name)
    if matches:
        return (matches.group(0)[1:-1], name)
    return False


def filter_blobs_to_delete(current_timestamps):
    blobs_to_delete = map(timestamp_check_deletion, current_timestamps)
    clean_blobs_to_delete = filter(None, blobs_to_delete)


def timestamp_check_deletion(blob_timestamp):
    date_format = "%Y%m%d"
    today = time.strftime(date_format)
    today_date = datetime.datetime.strptime(today, date_format)
    blob_date = datetime.datetime.strptime(blob_timestamp[0], date_format)
    if (abs((today_date - blob_date).days)) != 0:
        return blob_timestamp

def main():
    blob_service = create_blob_service(ACC_NAME, ACC_KEY)
    blobs = get_blobs(blob_service, CONTAINER_NAME)
    blobs_to_delete = filter_blobs_to_delete(blobs)
    print '\n'.join(blobs_to_delete)


if __name__ == '__main__':
    main()
