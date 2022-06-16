#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


class Reducer:

    def __init__(self, stream):
        self.stream = stream
        self.sum = 0
        self.acc = 1
        self.current_key = None

    @staticmethod
    def emit(key, total, prom):
        sys.stdout.write(f"{key}\t{total}\t{prom}\n")

    def reduce(self):
        for key, value in self:
            if key == self.current_key:
                self.sum += float(value)
                self.acc += 1
            else:
                if self.current_key is not None:
                    self.emit(self.current_key, self.sum, self.sum / self.acc)
                self.current_key = key
                self.sum = float(value)
                self.acc = 1
        self.emit(self.current_key, self.sum, self.sum / self.acc)

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
