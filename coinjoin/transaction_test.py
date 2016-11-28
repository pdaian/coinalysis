from blockchaincrawl import blocks, transactions, config, cache
import command, os, json, threading, time

rpc_connection = config.get_rpc()
tx_cache = cache.TxCache(200000)
sample_transaction = transactions.get_tx("9f6f5f58467965d5c56829a98ddbfc1f3016d8501c4dfe8beb55963b0dfca532", tx_cache, rpc_connection)
sample_transaction = transactions.get_tx("4d0a566628d6974f7388850f934eb53b0de891b7f428ae1acb7dbca3a55b9d19", tx_cache, rpc_connection)
sample_transaction = transactions.get_tx("c38aac9910f327700e0f199972eed8ea7c6b1920e965f9cb48a92973e7325046", tx_cache, rpc_connection)

parsed_tx = transactions.parse_transaction(sample_transaction, tx_cache, rpc_connection)
temp_file = open("/tmp/1", "w")
temp_file.write("#input\n")
for input in range(0, len(parsed_tx[0])):
    if input % 2 == 0:
        temp_file.write(parsed_tx[0][input] + " " + str(parsed_tx[0][input+1]) + "\n")
temp_file.write("\n#output\n")
for output in parsed_tx[1:]:
    temp_file.write(output[0] + " " + str(output[1]) + "\n")

temp_file.write("\n")
temp_file.close()
command = command.Command("/usr/bin/java -cp bin graphAnalysis.TransactionAnalysis /tmp/1".split())
command.run(timeout = 60)

