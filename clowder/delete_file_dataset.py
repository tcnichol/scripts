import json
import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets
from pyclowder.extractors import Extractor

url = sys.argv[1]
api_key = sys.argv[2]
file_id = '61097c7b5e0e0d2b3985e763'

client = pyclowder.datasets.ClowderClient(host=url, key=api_key)

if __name__ == '__main__':
    data = dict()
    data['key'] = api_key
    deleteFile = client.post('/files/'+file_id+'/remove', content=data, params=data)
    print('done')
