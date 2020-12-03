import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets

def main():
    url = 'http://localhost:9000'
    userkey = sys.argv[1]
    # path_to_file = sys.argv[2]
    new_dataset_name = 'new'
    parent_id = '5f4d560b5e0e676273bc95d4'
    print(userkey, new_dataset_name)
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)
    data = dict()
    data["name"] = "brand new dataset"
    data["description"] = "this is new"
    data["collection"] = parent_id

    result = client.post("/datasets/createempty", content=data, params=data)
    print('done')



if __name__ == '__main__':
    main()