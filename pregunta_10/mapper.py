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
    def emit(key, value):
        sys.stdout.write(f"{key},{value}\n")

    def map(self):
        for col1, col2 in self:
            value = col1.zfill(2)
            letters = col2.strip().split(',')
            for letter in letters:
                self.emit(letter, value)

    def __iter__(self):
        for line in self.stream:
            yield line.strip().split()


if __name__ == "__main__":
    mapper = Mapper(sys.stdin)
    mapper.map()
