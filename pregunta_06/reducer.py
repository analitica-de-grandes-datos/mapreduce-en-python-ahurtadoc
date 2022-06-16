#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream
        self.min = None
        self.max = None
        self.current_key = None

    @staticmethod
    def emit(key, min_value, max_value):
        sys.stdout.write(f"{key}\t{max_value}\t{min_value}\n")

    def reduce(self):
        for key, value in self:
            if key == self.current_key:
                self.min = min(self.min, float(value))
                self.max = max(self.max, float(value))
            else:
                if self.current_key is not None:
                    self.emit(self.current_key, self.min, self.max)
                self.current_key = key
                self.min = float(value)
                self.max = float(value)
        self.emit(self.current_key, self.min, self.max)

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
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
