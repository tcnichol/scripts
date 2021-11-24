import time

def main():
    test = 'this is only a test'
    with open('/home/data/test.txt', 'w') as f:
        f.write(test+'\n')
    time.sleep(100)


if __name__ == '__main__':
    main()
