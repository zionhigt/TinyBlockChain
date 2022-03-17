from re import M
from chain.block import Block
from chain._config import HASH_METHOD


def fixture_block():
    mock = {
        "head_hash": HASH_METHOD(b"TEST_HEAD"),
        "data": "TEST_DATA"
    }
    mock_hash = HASH_METHOD(str([mock.get("head_hash"), mock.get("data")]).encode()).hexdigest()
    mock.update({"hash": mock_hash})

    block = Block(mock.get("head_hash"))
    block.build(mock.get("data"))

    return block, mock
    
def fixture_chain_item(many=None, token=None):
    if many is not None and type(many) is int:
        mocks = []
        for i in range(ord("A"), ord("Z") + 1):
            if i - ord('A') == many:
                break
            
            a = chr(i)
            template = {
                "data": f"T{a}T{a}",
                "token": token
            }
            mocks.append(template)
            
    return mocks
