#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


class Mapper:
    def __init__(self, stream):
        self.stream = stream

    @staticmethod
    def emit(key, value):
        sys.stdout.write(f"{value}\t{key}\n")

    def map(self):
        for key, value in self:
            self.emit(key, value)

    def __iter__(self):
        for line in self.stream:
            yield line.strip().split(',')


if __name__ == "__main__":
    mapper = Mapper(sys.stdin)
    mapper.map()
