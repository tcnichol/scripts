import pyclowder
import sys

import pyclowder.datasets

def main():
    url = sys.argv[1]
    userkey = sys.argv[2]
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)
    matching_datasets = []
    all_datasets = client.get('/datasets')
    search_results = client.get('/search',params={'query':'jan 24','resource_type':'dataset'})
    for entry in search_results['results']:
        name = entry['name']
        if name == 'test 1':
            matching_datasets.append(entry)

    # this does not currently work
    search_for_space_results = client.get('/search', params={'query':'PDG', 'resource_type':'space'})
    print('got matching datasets', len(matching_datasets))
    all_spaces = client.get('/spaces')
    print('got all spaces')

if __name__ == '__main__':
    main()
