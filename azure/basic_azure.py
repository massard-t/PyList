# coding: utf-8
import os
import azure
import azure.storage
import azure.storage.blob
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings


def create_blob(acc_name, acc_key):
    """
    @input:
      acc_name -> String
      acc_key -> String
    @output:
      BlobService Object or Error
    """
    blob_service = azure.storage.blob.BlockBlobService(account_name=acc_name, account_key=acc_key)
    return blob_service


def create_container(blob_service, public, cont_name):
    """
    @input:
      blob_service -> BlobService Object
      public -> Boolean
      cont_name (optionnal) -> String
    @output:
      [string], string
    """
    if public is True:
        blob_service.create_container(cont_name, public_access=PublicAccess.Container, content_settings=ContentSettings(content_type='video/avi'))
    else:
        blob_service.create_container(cont_name, content_settings=ContentSettings(content_type='video/avi'))
    return blob_service



def list_blobs_in_container(blob_service, cont_name):
    """
    @input:
      blob_service -> BlobService Object
      cont_name -> String
    @output:
      [string], string
    """
    generator = blob_service.list_blobs(cont_name)
    blobs = []
    for blob in generator:
        blobs.append(blob.name)
    ret = blobs
    return ret


def list_containers(blob_service):
    """
    @input:
      blob_service -> BlobService Object
    @output:
      [string], string
    """
    containers = blob_service.list_containers()
    res = []
    for container in containers:
        res.append(container.name)
    return res, blob_service.name


def download_every_blob(blob_service, container, dest=os.getcwd()):
    """
    @input:
      blob_service -> BlobService Object
      container -> String
      dest (optionnal) -> String
    @output:
      None
    """
    result = blob_service.list_blobs(container)
    if not os.path.exists(dest):
        os.makedirs(dest)
    for b in result.items:
        r = blob_service.get_blob_to_path(container, b.name, b.name)


def remove_blob(blob_service, container, to_delete):
  """
  @input:
    blob_service -> BlobService Object
    container -> String
    to_delete -> String or List
  @output:
    None
  """
  if type(to_delete) != list:
    to_delete = [to_delete]
  for blob in to_delete:
    blob_service.delete_blob(container, blob)
