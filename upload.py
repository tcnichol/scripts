import pyclowder
import sys
import pyclowder.files
import pyclowder.datasets

def main():
    url = 'https://clowder.ncsa.illinois.edu/clowder'
    userkey = sys.argv[1]
    path_to_file = sys.argv[2]
    dataset_id = sys.argv[3]
    print(userkey, path_to_file, dataset_id)
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)
    file_id = client.post_file("/uploadToDataset/%s" % dataset_id, path_to_file)
    print("uploaded file", file_id)


if __name__ == '__main__':
    main()