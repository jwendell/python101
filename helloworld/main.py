import sys

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else "Python 101"
    print(f'Hello, {name}')

