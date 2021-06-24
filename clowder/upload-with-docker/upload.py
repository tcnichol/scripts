import pyclowder
import pyclowder.datasets
import os
import time

def main():
    print('starting script')
    userkey = os.getenv('APIKEY')
    print('this is the userkey')
    print(userkey)
    url = 'http://clowder:9000'
    client = pyclowder.datasets.ClowderClient(host=url, key=userkey)
    time.sleep(120)

    try:
        print('getting datasets')
        datasets = client.get('/datasets')
        print('obtained datasets', len(datasets))
    except:
        print('could not get datasets')

if __name__ == "__main__":
    main()