import pyclowder
import sys
import pyclowder.files

def main():
    url = 'https://clowder.ncsa.illinois.edu/clowder'
    userkey = sys.argv[1]
    path_to_file = sys.argv[2]
    dataset_id = sys.argv[3]
    file_id = pyclowder.files.upload_to_dataset(None, url, userkey, dataset_id=dataset_id,filepath=path_to_file)
    print('uploaded file', file_id)


if __name__ == '__main__':
    main()