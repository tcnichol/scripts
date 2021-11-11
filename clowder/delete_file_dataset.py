import json
import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets
from pyclowder.extractors import Extractor

# url = sys.argv[1]
# api_key = sys.argv[2]
# file_id = sys.argv[3]

url = 'https://clowder.ncsa.illinois.edu/clowder'
api_key = 'eb761935-44db-45e0-a768-75f38ad8593f'
file_id = '600df0435e0ed582248a5f1d'


client = pyclowder.datasets.ClowderClient(host=url, key=api_key)

if __name__ == '__main__':
    data = dict()

    data['key'] = api_key
    data['limit'] = 0
    all_datasets = client.get('/datasets?limit=0')
    print('all datasets')
    deleteFile = client.post('/files/'+file_id+'/remove', content=data, params=data)
    print('done')
