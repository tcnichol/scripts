import pyclowder.datasets
import os
import requests
import sys
import subprocess

url = sys.argv[1]
userkey = sys.argv[2]

client = pyclowder.datasets.ClowderClient(host=url, key=userkey)

def download_file_to_location(file_url, file_location):
    r = requests.get(file_url, stream=True)
    if r.ok:
        with open(file_location, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        pass

dataset_id = '60b660b1e4b0ea7048d68f1a'


dataset_files = client.get('/datasets/' + dataset_id + '/files')

# create download directory

download_directory = os.path.join(os.getcwd(),'current-downloads')

if not os.path.isdir(download_directory):
    subprocess.run(['mkdir',download_directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for f in dataset_files:
    file_id = f['id']
    filename = f['filename']
    download_url = url+'/api/files/'+file_id+'/blob?key='+userkey
    download_file = requests.get(download_url)
    location_to_downlod = os.path.join(download_directory, filename)
    try:
        download_file_to_location(download_url, location_to_downlod)
    except Exception as e:
        print(e)


print('done')

