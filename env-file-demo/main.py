import gdal
import os
import time

def main():
    print('the USER')
    print(os.environ.get('USER'))
    print('the PASSWORD')
    print(os.environ.get('PASSWORD'))
    time.sleep(60*5)


if __name__ == "__main__":
    main()