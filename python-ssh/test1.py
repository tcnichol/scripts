import sys
import time

def main():
    with open('blah1.txt', 'w') as f:
        f.write('blah blah blah')
        f.close()
    for i in range(0,100):
        print(i)
        time.sleep(5)
    print('done')

if __name__ == '__main__':
    main()