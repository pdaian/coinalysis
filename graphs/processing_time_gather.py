import os

def draw(directory, block_number, block_hash):
    processing_time = float(open(os.path.join(directory,'processing_time')).read().strip())
    if block_number % 100 is 0:
        print "Processed", block_number, processing_time, block_hash
    return str(block_number) + "," + str(processing_time)

