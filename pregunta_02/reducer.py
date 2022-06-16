#
# >>> Escriba el codigo del reducer a partir de este punto <<<
# reducer

import sys

if __name__ == '__main__':
    curkey = None
    max_value = 0

    for line in sys.stdin:
        key, value = line.split('\t')
        if key == curkey:
            if int(value) > max_value:
                max_value = int(value)
        else:
            if curkey is not None:
                sys.stdout.write(f"{curkey}\t{max_value}\n")
            curkey = key
            max_value = 0
    sys.stdout.write("{}\t{}\n".format(curkey, max_value))
