from chain.tests.fixtures import fixture_block


def test_sign():
    block, mock = fixture_block()
    block.sign()
    assert block._hash.hexdigest() == mock.get("hash")
    assert block._data == mock.get("data")
    assert block.isSigned == True

def test_iam_not_signed():
    block, mock = fixture_block()
    assert block.iam() == None
    assert block._data == mock.get("data")
    assert block.isSigned == False

def test_iam_signed():
    block, mock = fixture_block()
    block.sign()
    assert block.iam() == mock.get("hash")
    assert block._data == mock.get("data")
    assert block.isSigned == True

def test_get():
    block, mock = fixture_block()
    assert block.get() == [mock.get("head_hash"), mock.get("data")]