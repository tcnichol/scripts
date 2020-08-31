import pyclowder
import sys

import pyclowder.datasets

def main():
    url = 'https://clowder.ncsa.illinois.edu/clowder'
    userkey = sys.argv[1]
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)
    matching_datasets = []
    all_datasets = client.get('/datasets')
    search_results = client.get('/search',params={'query':'test 1','resource_type':'dataset'})
    for entry in search_results['results']:
        name = entry['name']
        if name == 'test 1':
            matching_datasets.append(entry)
    print('got matching datasets', len(matching_datasets))

if __name__ == '__main__':
    main()
