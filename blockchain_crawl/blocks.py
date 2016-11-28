import config

def get_all_block_hashes(start, end, interval, rpc_connection):
    """ Return all block hashes in the interval defined in config, as list of block IDs """
    block_hashes = []

    if config.DEBUG:
        print "Gathering block hashes..."

    for start_block in range(start, end, interval):
        commands = [ [ "getblockhash", height] for height in range(start_block, min(start_block + interval, end)) ]
        batch_block_hashes = rpc_connection.batch_(commands)
        block_hashes += batch_block_hashes
        if config.DEBUG:
            print "    [+] Gathered", len(batch_block_hashes) ,"blocks", start_block, "to", min(start_block + interval, end)

    return block_hashes

def get_all_transactions(block_hash, rpc_connection):
    return rpc_connection.getblock(block_hash)['tx']
