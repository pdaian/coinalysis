import config
from bitcoinrpc.authproxy import JSONRPCException

def get_tx(txid, tx_cache, rpc_connection):
    """ Get a formatted transaction object for a given transaction ID, as a JSON object """
    try:
        if txid in tx_cache:
            return tx_cache[txid]
        tx = rpc_connection.decoderawtransaction(rpc_connection.getrawtransaction(txid))
        tx_cache[txid] = tx
        return tx
    except JSONRPCException:
        return None

def is_coinbase(tx):
    if len(tx['vin']) == 1 and 'coinbase' in tx['vin'][0]:
        return True
    return False

def get_formatted_outputs(tx):
    """ Returns a list of (output address, amounts) for parseable transactions, or None if none exist """
    outputs = []
    for output in tx['vout']:
        if 'scriptPubKey' in output and not 'addresses' in output['scriptPubKey']:
            # One of the outputs of this tx is malformed
            open('invalidoutputs', 'a').write(tx['txid'] + '\n')
        else:
            outputs += [(output['scriptPubKey']['addresses'][0], float(output['value']))]
    return outputs

def parse_transaction(tx, tx_cache, rpc_connection):
    """ For a given transaction object, return a pair of lists, one for input and one for output
    Where each list is a list of (address, amount) """
    if config.DEBUG:
        print "Processing tx", tx['txid']
    inputs = []
    for input in tx['vin']:
        num_output = input['vout']
        originating_tx = input['txid']
        formatted_outputs = get_formatted_outputs(get_tx(originating_tx, tx_cache, rpc_connection))
        try:
            originating_output = formatted_outputs[num_output]
            inputs += originating_output
        except IndexError:
            # One of the outputs this tx spends as input is malformed
            open('invalidinputs', 'a').write(tx['txid'] + '\n')
    outputs_inputs = [inputs]
    outputs_inputs += get_formatted_outputs(tx)
    return outputs_inputs

def format_transaction(parsed_tx):
    parsed_output = ""
    parsed_output += "#input\n"
    for input in range(0, len(parsed_tx[0])):
        if input % 2 == 0:
            parsed_output += parsed_tx[0][input] + " " + str(parsed_tx[0][input+1]) + "\n"
    parsed_output += "\n#output\n"
    for output in parsed_tx[1:]:
        parsed_output += output[0] + " " + str(output[1]) + "\n"

    parsed_output += "\n"
    return parsed_output
