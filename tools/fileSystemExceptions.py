class BasePathException(OSError):
    def __init__(self, path):
        self._path = path


class PathNotExistsException(BasePathException):
    def __str__(self):
        return f"Path <{self._path}> not exists"



class PathExistsException(BasePathException):
    def __str__(self):
        return f"Path <{self._path}> exists"


class PathExistsAsFileException(BasePathException):
    def __str__(self):
        return f"Path <{self._path}> exists as file, not as a directory"
