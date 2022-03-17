from chain._config import HASH_METHOD


class Block:
    _data = None
    _head_hash = None
    _hash = None
    isSigned = False

        
    class AlreadyLinkError(Exception):
        def __init__(self):
            super().__init__("Cannot change my link")


    class NoBlockToLink(Exception):
        def __init__(self):
            super().__init__("Previous block not ready yet")


    class AlreadySignError(Exception):
        def __init__(self):
            super().__init__("Cannot change my signature")


    class GraveeDansLaRocheError(Exception):
        def __init__(self):
            super().__init__("Cannot change my data")


    def __init__(self, head_hash):
        if self._head_hash is None:
            self._head_hash = head_hash
        else:
            raise self.AlreadyLinkError()

    def get(self):
        return [self._head_hash, self._data]

    def build(self, data):
        if not self.isSigned:
            if self._data is None:
                self._data = data
        else:
            raise self.GraveeDansLaRocheError()
    
    def sign(self):
        self.isSigned = True
        if self._hash is None:
            self._hash = HASH_METHOD(str(self.get()).encode())
        else:
            raise self.AlreadySignError()
        
    
    def iam(self):
        if self._hash is not None:
            return self._hash.hexdigest()
        else:
            return None

    def read(self):
        return " | ".join((str(self.iam()), self._data))


