from flask import Flask, render_template, request
from blockchaincrawl import blocks, transactions, config, cache
import command, os, json, threading, time

tx_cache = cache.TxCache(2000)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/do")
def do():
    rpc_connection = config.get_rpc()
    txid = request.args.get('txid')
    sample_transaction = transactions.get_tx(txid, tx_cache, rpc_connection)

    parsed_tx = transactions.parse_transaction(sample_transaction, tx_cache, rpc_connection)
    temp_file = open("/tmp/1", "w")
    script_input = ""
    script_input += "#input\n"
    for input in range(0, len(parsed_tx[0])):
        if input % 2 == 0:
            script_input += parsed_tx[0][input] + " " + str(parsed_tx[0][input+1]) + "\n"
    script_input += "\n#output\n"
    for output in parsed_tx[1:]:
        script_input += output[0] + " " + str(output[1]) + "\n"

    temp_file.write(script_input)
    temp_file.write("\n")
    temp_file.close()
    tx_command = command.Command("/usr/bin/java -cp bin graphAnalysis.TransactionAnalysis /tmp/1".split())
    tx_command.run(timeout = 5)
    output = tx_command.stdout
    if len(output.strip()) is 0:
        output = "Script timed out on your transaction!  Congrats, you are probably at least a bit secure :)"
    return render_template("done.html", tx_out = output, tx_rep = script_input)


def run():
    app.run(host='0.0.0.0')
