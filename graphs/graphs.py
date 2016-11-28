import blocks, transactions, config, os, json, threading, cache, time

def gather_data(block_start, block_end, file_name, draw_module):
    data = ""
    rpc_connection = config.get_rpc()
    block_hashes = blocks.get_all_block_hashes(block_start, block_end, config.BLOCK_INTERVAL, rpc_connection)
    start_time = time.time()
    tx_cache = cache.TxCache(100000)
    for block_number in range(block_start, block_end):
        block_index = block_number - block_start
        block_hash = block_hashes[block_index]
        d='.'
        for subdirectory in [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]:
            d = os.path.join(subdirectory, block_hash)
            if os.path.isdir(d):
                data += draw_module.draw(d, block_number, block_hash) + "\n"
                continue
    open(file_name, 'w').write(data)


