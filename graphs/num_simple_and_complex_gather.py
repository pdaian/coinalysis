import os

def draw(directory, block_number, block_hash):
    num_complex = len([os.path.join(directory,o) for o in os.listdir(directory) if not os.path.isdir(os.path.join(directory,o))])-2
    num_simple = len(open(os.path.join(directory,'simple_txs')).read().strip().splitlines())
    if block_number % 100 is 0:
        print "Processed", block_number, num_simple, num_complex, block_hash
    return str(block_number) + "," + str(num_simple) + "," + str(num_complex)

