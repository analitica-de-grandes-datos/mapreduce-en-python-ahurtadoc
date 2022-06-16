#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream
        self.total = 5

    @staticmethod
    def emit(key, value1, value2):
        sys.stdout.write(f"{key}   {value1}   {int(value2)}\n")

    def reduce(self):
        for key, value1, value2 in self:
            self.emit(value2.strip(), value1, key)

    def __iter__(self):
        accumulator = 6
        for line in self.stream:
            yield line.split(",")
            accumulator -= 1
            if accumulator == 0:
                break


if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()
