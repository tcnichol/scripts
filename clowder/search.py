import pyclowder
import sys

import pyclowder.datasets


def find_dataset_in_collection(dataset_name, collection_name):

    dataset_found = None

    url = sys.argv[1]
    userkey = sys.argv[2]
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)

    collection_results = client.get('/search',params={'query':collection_name,'resource_type':'colllection'})
    if len(collection_results) > 0:
        result = collection_results[0]
    collection_datasets = client.get('/collections/'+result['id']+'/datasets')

    for ds in collection_datasets:
        if ds['name'] == dataset_name:
            dataset_found = ds
    return ds


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
