import os

def draw(directory, block_number, block_hash):
    fee_range = [.02, .05]
    amts = {.01 : 0, 0.0342: 0, .1 : 0, 1 : 0, 10 : 0, 100 : 0}
    simple_txs = open(os.path.join(directory,'simple_txs')).read().strip().splitlines()
    for tx in simple_txs:
        tx_amount = float(tx.split(",")[1])
        for amount in (0.01, 0.0342, .1, 1, 10, 100):
            if (tx_amount <= (amount - (amount * fee_range[0]))) and (tx_amount >= (amount - (amount * fee_range[1]))):
                amts[amount] += 1
    if block_number % 100 is 0:
        print "Processed", block_number, amts, block_hash
    return str(block_number) + "," + str(amts[0.01]) + "," + str(amts[0.0342]) + "," + str(amts[0.1]) + "," + str(amts[1]) + "," + str(amts[10]) + "," + str(amts[100])

