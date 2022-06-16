#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


class Mapper:
    def __init__(self, stream):
        self.stream = stream

    @staticmethod
    def emit(key, value1, value2):
        sys.stdout.write(f"{key.zfill(4)},{value1},{value2}\n")

    def map(self):
        for col1, col2, col3 in self:
            self.emit(col3, col2, col1)

    def __iter__(self):
        for line in self.stream:
            yield line.strip().split()


if __name__ == "__main__":
    mapper = Mapper(sys.stdin)
    mapper.map()
