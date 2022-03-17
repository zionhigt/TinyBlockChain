from pytest import fixture, raises
from chain.chain import Chain
from chain.tests.fixtures import fixture_chain_item


def test_inscript_bad_token():
    chain = Chain()
    mock = fixture_chain_item(1, "fail_token")
    with raises(chain.BlockError) as e:
        chain.inscript(**mock[0])

def test_inscript_before_previous_is_ready():
    chain = Chain()
    mocks = fixture_chain_item(2)
    with raises(chain.BlockError) as e:
        for i, mock in enumerate(mocks):
            block = chain.inscript(mock.get("data"), mock.get("token"))
            if i == 0:
                block._hash = None