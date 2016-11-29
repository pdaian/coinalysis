import os

def draw(directory, block_number, block_hash):
    data = ""
    simple = open(os.path.join(directory,'simple_txs')).read().strip().splitlines()
    for tx in simple:
        data += tx.split(",")[1] + "\n"
    return data.strip()

