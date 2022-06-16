#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream
        self.value = 0
        self.current_key = None

    @staticmethod
    def emit(key, value):
        sys.stdout.write(f"{key}\t{value}\n")

    def reduce(self):
        for key, value in self:
            if key == self.current_key:
                self.value += int(value)
            else:
                if self.current_key is not None:
                    self.emit(self.current_key, self.value)
                self.current_key = key
                self.value = int(value)
        self.emit(self.current_key, self.value)

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
