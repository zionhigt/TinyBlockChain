from chain.chain import Chain


if __name__ == '__main__':
    chain = Chain()

    data = [
        "TITI",
        "TATA",
        "TUTU"
    ]

    # You may turn token to None until proof of work will developed
    token = "FAIL"
    for d in data:
        try:
            chain.inscript(d, token);
        except Chain.BlockError as err:
            print("Block Error : ")
            print(err)
    
    chain.read()
