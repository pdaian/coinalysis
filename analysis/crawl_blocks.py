import blocks, transactions, config, os, json, threading, cache, time


def process_blocks(thread_id, block_start, block_end):
    rpc_connection = config.get_rpc()
    block_hashes = blocks.get_all_block_hashes(block_start, block_end, config.BLOCK_INTERVAL, rpc_connection)
    start_time = time.time()
    tx_cache = cache.TxCache(150000)
    for block in block_hashes:
        simple_txs = ""
        if os.path.isdir("results" + str(thread_id) + "/" + block):
            continue
        block_start_time = time.time()
        os.makedirs("results" + str(thread_id) + "/" + block)
        os.system("mkdir -p results" + str(thread_id) + "/" + block)
        simple_tx_handle = open("results" + str(thread_id) + "/" + block + "/simple_txs", 'a')
        if config.DEBUG:
            print str(thread_id) + " Processing block", block
        transaction_ids = blocks.get_all_transactions(block, rpc_connection)
        for transaction_id in transaction_ids:
            transaction = transactions.get_tx(transaction_id, tx_cache, rpc_connection)
            if transactions.is_coinbase(transaction):
                # We don't care about coinbase transactions at all
                continue
            if len(transaction['vout']) < 3 or (len(transaction['vin']) < 2):
                # Simple transaction
                sum = 0.0
                for output in transactions.get_formatted_outputs(transaction):
                    sum += output[1]
                simple_txs += transaction_id + "," + str(sum) + "\n"
                continue
            if transaction is not None:
                open("results" + str(thread_id) + "/" + block + '/' + transaction_id, 'w').write(transactions.format_transaction(transactions.parse_transaction(transaction, tx_cache, rpc_connection)))
            else:
                # Fatal error - this should never happen
                print "Invalid transaction", transaction_id
                exit(1)
        block_time_elapsed = time.time() - block_start_time
        open("results" + str(thread_id) + "/" + block +  "/processing_time", 'w').write(str(block_time_elapsed))
        simple_tx_handle.write(simple_txs)
        simple_tx_handle.close()
    time_elapsed = time.time() - start_time
    open(str(thread_id) + "_done", 'w').write(str(time_elapsed))


# First batch - process blocks 400k until present
t1 = threading.Thread(target=process_blocks, args=(1, 430000, 438746)) # latest block as of 1pm nov 13
t2 = threading.Thread(target=process_blocks, args=(2, 420000, 430000))
t3 = threading.Thread(target=process_blocks, args=(3, 410000, 420000))
t4 = threading.Thread(target=process_blocks, args=(4, 400000, 410000))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# Second batch - process blocks 280k until 400k
t1 = threading.Thread(target=process_blocks, args=(5, 370000, 400000)) 
t2 = threading.Thread(target=process_blocks, args=(6, 340000, 370000))
t3 = threading.Thread(target=process_blocks, args=(7, 310000, 340000))
t3 = threading.Thread(target=process_blocks, args=(8, 280000, 310000))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# Third batch - process blocks 200k until 280k
t1 = threading.Thread(target=process_blocks, args=(9, 260000, 280000))
t2 = threading.Thread(target=process_blocks, args=(10, 240000, 260000))
t3 = threading.Thread(target=process_blocks, args=(11, 220000, 240000))
t4 = threading.Thread(target=process_blocks, args=(12, 200000, 220000))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

# Last batch - process blocks 100k until 200k
t1 = threading.Thread(target=process_blocks, args=(13, 175000, 200000))
t2 = threading.Thread(target=process_blocks, args=(14, 150000, 175000))
t3 = threading.Thread(target=process_blocks, args=(15, 125000, 150000))
t4 = threading.Thread(target=process_blocks, args=(16, 100000, 125000))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()


print "ALL DONE!"
