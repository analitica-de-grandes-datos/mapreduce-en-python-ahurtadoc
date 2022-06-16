#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


class Mapper:
    def __init__(self, stream):
        self.stream = stream

    @staticmethod
    def emit(key, sort_value, value):
        sys.stdout.write(f"{key}%{sort_value.zfill(4)},{value}\n")

    def map(self):
        for col1, col2, col3 in self:
            self.emit(col1, col3, col2)

    def __iter__(self):
        for line in self.stream:
            yield line.strip().split()


if __name__ == "__main__":
    mapper = Mapper(sys.stdin)
    mapper.map()
