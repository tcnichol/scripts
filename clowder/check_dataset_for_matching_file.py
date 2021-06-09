import requests
import pyclowder
import sys
import pyclowder.datasets
from pathlib import Path

url = sys.argv[1]
api_key = sys.argv[2]

current_dataset_id = '60752b30e4b091e66c15cc94'

file_name = 'QB02_20120802192627_101001000FEE1100_12AUG02192627-M1BS-500504198100_01_P007_u16rf3413_pansh.tif'

client = pyclowder.datasets.ClowderClient(host=url,key=api_key)

def find_matching_xml_file(filename, dataset_id):
    dataset_files = client.get('/datasets/'+dataset_id+'/files')
    filename_stem = Path(filename).stem
    for each in dataset_files:
        current_filename = each['filename']
        if current_filename.endswith('.xml'):
            current_stem = Path(current_filename).stem
            if current_stem == filename_stem:
                return each
    return None

if __name__ == '__main__':
    # dump_to_json()
    matching_xml = find_matching_xml_file(file_name, current_dataset_id)
    matching_xml_id = matching_xml['id']
    print('done')