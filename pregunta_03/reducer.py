#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream

    @staticmethod
    def emit(key, value):
        sys.stdout.write(f"{value.strip()},{key}\n")

    def reduce(self):
        for key, value in self:
            self.emit(key, value)

    def __iter__(self):

        for line in self.stream:
            #
            # Lee el stream de datos y lo parte
            # en (clave, valor)
            #
            yield line.split("\t")


if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()
