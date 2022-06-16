#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        attribute = line.split(',')[2]
        sys.stdout.write(f"{attribute}\t1\n")
