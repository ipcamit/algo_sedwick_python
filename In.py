# import sys
import urllib.request
class In():
    """Replicatoion of In class in java.utils.Scanner readInt routine
    taks in a file name and generate a readInt function  which yields 
    integers from files one at a time"""

    filename = ""
    filestream = None
    _int_generator = None
    url = None
    request= None
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
        if ('https://' in filename) or ('http://' in filename):
            self.url =  filename
            header ={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            self.request = urllib.request.Request(self.url,data=None,headers=header)
        else:
            self.filename=filename
            self.filestream = open(filename)
            self._int_generator = self._generator_readInt()

    def readInt(self):
        return next(self._int_generator)

    def readAll(self):
        if self.url !=None:
            self.filestream = urllib.request.urlopen(self.request).read().decode('utf-8')
            return self.filestream
        else:
            self.filestream.read()

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