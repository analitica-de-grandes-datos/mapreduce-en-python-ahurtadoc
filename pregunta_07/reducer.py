#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream

    @staticmethod
    def emit(key, value, sorted_value):
        sys.stdout.write(f"{key}   {value.strip()}   {int(sorted_value)}\n")

    def reduce(self):
        for key, value in self:
            original_key, sorted_value = key.split("%")
            self.emit(original_key, value, sorted_value)

    def __iter__(self):

        for line in self.stream:
            #
            # Lee el stream de datos y lo parte
            # en (clave, valor)
            #
            yield line.split(",")


if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()
