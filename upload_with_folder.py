import requests
import sys
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib3.filepost import encode_multipart_formdata
import requests
import datetime
from datetime import datetime
import pyclowder
import zipfile
import pyclowder.datasets
import time

clowder_url = 'http://localhost:9000/'
user_api = 'c9b05b10-085b-46f5-8ddf-c977440900c5'

dataset_id = sys.argv[3]
folder_id = sys.argv[4]
file_path = sys.argv[5]


client = pyclowder.datasets.ClowderClient(host=clowder_url, key=user_api)

def upload_a_file_to_dataset(filepath, dataset_id):
    url = '%sapi/uploadToDataset/%s?key=%s' % (clowder_url, dataset_id, user_api)
    # url = '%sapi/uploadToDataset/%s?key=%s&folder_id=%s' % (clowder_url, dataset_id, user_api, 'blah')
    print('the url')
    print(url)
    file_exists = os.path.exists(filepath)
    print('starting upload')
    print(str(datetime.now()))
    before = datetime.now()
    if os.path.exists(filepath):
            filename = os.path.basename(filepath)
            m = MultipartEncoder(
                fields={'file': (filename, open(filepath, 'rb'))}
            )
            try:
                result = requests.post(url, data=m, headers={'Content-Type': m.content_type},
                                        verify=False)

                print(result)
                uploadedfileid = result.json()['id']
                print("uploaded file", uploadedfileid)
                print(str(datetime.now()))
                after = datetime.now()
                duration = after - before
                print(str(duration))
            except Exception as e:
                print('failed to upload file, error')
                print(e)
                print(str(datetime.now()))
    else:
        print("unable to upload file %s (not found)", filepath)


def upload_a_file_to_dataset_with_folder(filepath, dataset_id, folder_id):
    url = '%sapi/uploadToDataset/%s?key=%s&folder_id=%s' % (clowder_url, dataset_id, user_api, folder_id)
    print('the url')
    print(url)
    file_exists = os.path.exists(filepath)
    print('starting upload')
    print(str(datetime.now()))
    before = datetime.now()
    if os.path.exists(filepath):
            filename = os.path.basename(filepath)
            m = MultipartEncoder(
                fields={'file': (filename, open(filepath, 'rb')),
                        'folder_id':folder_id}
            )
            try:
                result = requests.post(url, data=m, headers={'Content-Type': m.content_type},
                                        verify=False)

                print(result)
                uploadedfileid = result.json()['id']
                print("uploaded file", uploadedfileid)
                print(str(datetime.now()))
                after = datetime.now()
                duration = after - before
                print(str(duration))
            except Exception as e:
                print('failed to upload file, error')
                print(e)
                print(str(datetime.now()))
    else:
        print("unable to upload file %s (not found)", filepath)

if __name__ == '__main__':
    upload_a_file_to_dataset_with_folder(file_path, dataset_id,folder_id)
    upload_a_file_to_dataset(file_path, dataset_id)
    upload_a_file_to_dataset_with_folder(file_path, dataset_id, 'ddd')
    upload_a_file_to_dataset(file_path, dataset_id)
    print('done')