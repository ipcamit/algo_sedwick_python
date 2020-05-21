# import sys

class In():
    """Replicatoion of In class in java.utils.Scanner readInt routine
    taks in a file name and generate a readInt function  which yields 
    integers from files one at a time"""

    filename = ""
    filestream = None
    _int_generator = None
    # private integer generator

    def _generator_readInt(self):
        """Private function to create generator object for integers from file
        will be called from __init__ and generator mapped to readInt()"""
        with self. filestream as fs:
            for line in fs:
                data = list(map(int,line.split()))
                for num in data:
                    yield num

    def __init__(self,filename):
        self.filename=filename
        self.filestream = open(filename)
        self._int_generator = self._generator_readInt()

    def readInt(self):
        return next(self._int_generator)

    def isInstantiated(self):
        if self.filestream!= None:
            return True
        else:
            return False


# if __name__ == '__main__':
#     import sys
#     filename = sys.argv[1]
#     in_ = In(filename)
#     for i in range(10):
#         print(in_.readInt())