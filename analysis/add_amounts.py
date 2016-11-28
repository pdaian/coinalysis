import blocks, transactions, config, os, json, threading, cache, time

def add_amounts(file):
    new_file_contents = ""
    txs = open(file).read()
    if "," in txs:
        # Already converted
        return
    print "Processing", file
    txs = txs.splitlines()
    rpc_connection = config.get_rpc()
    tx_cache = cache.TxCache(100000)
    for line in txs:
        if len(line.strip()) is 0:
            continue
        tx = transactions.get_tx(line, tx_cache, rpc_connection)
        sum = 0.0
        for output in transactions.get_formatted_outputs(tx):
            sum += output[1]
        new_file_contents += line + "," + str(sum) + "\n"
    open(file, 'w').write(new_file_contents)


for root, directories, files in os.walk("."):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        if "simple_tx" in filepath:
            add_amounts(filepath)
