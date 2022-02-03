import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets
import time
import datetime
import os

import environment


def main():

    print('environment variables')

    for k, v in os.environ.items():
        print(f'{k}={v}')

    CLOWDER_URL = os.environ.get('clowder_url')
    CLOWDER_KEY = os.environ.get('api_key')
    SPACE_ID = os.environ.get('space_id')

    print('current time')
    collection_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    print(collection_name)

    client = pyclowder.datasets.ClowderClient(host=CLOWDER_URL, key=CLOWDER_KEY)

    # creating collection in a space
    data = dict()
    data["name"] = collection_name
    data["description"] = ''
    data["space"] = SPACE_ID
    collection_result = client.post("/collections", content=data, params=data)
    collection_id = collection_result['id']

    # creating a dataset in the space and collection
    data = dict()
    dataset_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    data["name"] = dataset_name
    data["description"] = ''
    data["space"] = [SPACE_ID]
    if collection_id:
        data["collection"] = [collection_id]
    result = client.post("/datasets/createempty", content=data, params=data)
    data["name"] = "brand new dataset"
    data["description"] = "this is new"
    data["collection"] = collection_id

    result = client.post("/datasets/createempty", content=data, params=data)

    # TODO upload files





if __name__ == '__main__':

    cycles = 0

    while cycles < 5:
        print('sleeping')
        time.sleep(60*2)
        main()