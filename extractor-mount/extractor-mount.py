#!/usr/bin/env python

"""Example extractor based on the clowder code."""

import logging
import subprocess
import os
import shutil

from pyclowder.extractors import Extractor
import pyclowder.files

def delete_folder_contents(path_to_folder):
    files = os.listdir(path_to_folder)
    for file in files:
        path_to_file = os.path.join(path_to_folder, file)
        os.remove(path_to_file)



class ExtractorMount(Extractor):
    """Count the number of characters, words and lines in a text file."""
    def __init__(self):
        Extractor.__init__(self)

        # add any additional arguments to parser
        # self.parser.add_argument('--max', '-m', type=int, nargs='?', default=-1,
        #                          help='maximum number (default=-1)')

        # parse command line and load default logging configuration
        self.setup()

        # setup logging for the exctractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

    def process_message(self, connector, host, secret_key, resource, parameters):
        # Process the file and upload the results

        logger = logging.getLogger(__name__)
        inputfile = resource["local_paths"][0]
        file_id = resource['id']
        filename = resource['name']

        path_to_files = '/home/data/upload_files/'
        print('does path to destination exist?')
        print(os.path.isdir(path_to_files))

        destination = os.path.join(path_to_files, filename)
        print('destination is', destination)

        shutil.copy(inputfile, destination)

        all_files = os.listdir(path_to_files)

        num_files = len(all_files)

        print("do we have 3 or more files?")
        if num_files > 2:
            try:
                delete_folder_contents(path_to_files)
            except Exception as e:
                print("could not delete")
                logger.info(str(e))



        # These process messages will appear in the Clowder UI under Extractions.
        connector.message_process(resource, "Copied to mounted directory...")
        logger.info("current files : " + str(all_files))


        # Store results as metadata
        result = {
            'numfiles': num_files
        }
        metadata = self.get_metadata(result, 'file', file_id, host)

        # Normal logs will appear in the extractor log, but NOT in the Clowder UI.
        logger.debug(metadata)

        # Upload metadata to original file
        pyclowder.files.upload_metadata(connector, host, secret_key, file_id, metadata)

if __name__ == "__main__":
    extractor = ExtractorMount()
    extractor.start()
