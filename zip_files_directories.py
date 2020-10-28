import zipfile
from zipfile import ZipFile
import os

def create_files():

    content_1 = "this is the content of the first text file"


    content_2 = "this is the content of the second text file"

    with open('test.txt', 'w') as f:
        f.write(content_1)
        f.close()
    with open('test2.txt', 'w') as f1:
        f1.write(content_2)
        f1.close()


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths


def main():

    create_files()
    # path to folder which needs to be zipped

        # writing files to a zipfile
    file_paths  = ['test.txt',  'test2.txt']
    with ZipFile('test.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

if __name__ == "__main__":
    main()