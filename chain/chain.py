from .block import Block
from hashlib import sha3_512


class Chain:
    _blocks = []
    _expected_token = None

    class BlockError(Exception):
        def __init__(self, block_error):
            super().__init__(block_error)

    class TokenError(Exception):
        def __init__(self):
            super().__init__("This token cannot be writting")

    def inscript(self, data, token):
        try:
            if token != self._expected_token:
                raise self.TokenError()

            if len(self._blocks):
                previous_hash = self._blocks[-1].iam()
                if previous_hash is None:
                    raise Block.NoBlockToLink()
            else:
                previous_hash = sha3_512(b"first block in the chain !!!").hexdigest()

            block = Block(previous_hash)
            block.build(data)
            block.sign()
            self._blocks.append(block)
            return block

        except (Block.AlreadyLinkError, Block.NoBlockToLink, Block.AlreadySignError, Block.GraveeDansLaRocheError, self.TokenError) as err:
            raise self.BlockError(err)

    def read(self):
        for block in self._blocks:
            print(block.read())

