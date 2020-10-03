import pyclowder
import sys
import pyclowder.files

def main():
    url = 'https://clowder.ncsa.illinois.edu/clowder'
    userkey = sys.argv[1]
    client = pyclowder.files.ClowderClient(host=url, key=userkey)
    client


if __name__ == '__main__':
    main()