import pyclowder
import time
import os

def delete_folder_contents(path_to_folder):
    files = os.listdir(path_to_folder)
    for file in files:
        path_to_file = os.path.join(path_to_folder, file)
        os.remove(path_to_file)

def main():
    print('running')
    delete_folder_contents('/Users/helium/ncsa/scripts/extractor-mount/extra')
    time.sleep(60*3)

if __name__ == "__main__":
    main()