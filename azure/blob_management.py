# coding: utf-8
import basic_azure
import azure
import azure.storage
import azure.storage.blob


basic_azure.create_blob()
acc_name="account_name"
acc_key="account_key"
cont_name = "container_name"
blob_service = azure.storage.blob.BlockBlobService(account_name=acc_name, account_key=acc_key)


generator = blob_service.list_blobs(cont_name)
for blob in generator:
    print blob.name
    
def check_blobs(blob_service):
    generator = blob_service.list_blobs(cont_name)
    for blob in generator:
        print blob.name
        
check_blobs(blob_service)
