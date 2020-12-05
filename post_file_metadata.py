import json
import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets
from pyclowder.extractors import Extractor

def main():
    # the file is called "metadata.json"
    with open('metadata.json', 'r') as f:
        md = json.load(f)



    url = 'http://localhost:9000'
    userkey = 'db17eab4-30cc-4fda-a4f0-3f4d3656a2f6'
    file_id = '5fc54f39e84aed8c7636f158'
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)

    #metadata = Extractor.get_metadata(md, 'file', file_id, url)

    result = client.post('/files/'+file_id+'/metadata',content=md, params=md)
    print(result)



if __name__ == '__main__':
    main()