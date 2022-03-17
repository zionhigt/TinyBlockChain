from chain.chain import Chain


if __name__ == '__main__':
    chain = Chain()

    data = [
        "TITI",
        "TATA",
        "TUTU"
    ]

    token = "e"
    for d in data:
        try:
            chain.inscript(d, token);
        except Chain.BlockError as err:
            print("Block Error : ")
            print(err)
    
    chain.read()
