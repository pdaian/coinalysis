# This is dead code; originally, we considered transactions with a single input and lots of outputs "complex".  They are obviously not.
# This cleaned those transactions up and moved them to the simple transactions file

import os, json

def convert(filepath):
    print "processing", filepath
    contents = open(filepath).read()
    if not "#input" in contents:
        # Not in expected format
        open('screwedup', 'a').write(filepath + "\n")
        return
    inputs = contents.split("#input")[1].split("#output")[0].strip().splitlines()
    num_inputs = len(inputs)
    if num_inputs != 1:
        return
    outputs = contents.split("#input")[1].split("#output")[1].strip().splitlines()
    block = filepath.split("/")[-2]
    transaction = filepath.split("/")[-1]
    simple_tx_path = "/".join(filepath.split("/")[:-1]) + "/simple_txs"
    total_output_amount = 0.0
    for output in outputs:
        total_output_amount += float(output.strip().split()[-1])
    simple_tx_handle = open(simple_tx_path, 'a')
    simple_tx_handle.write(transaction + "," + str(total_output_amount) + "\n")
    simple_tx_handle.close()
    os.remove(filepath)
    print "Removed " + filepath

for root, directories, files in os.walk("."):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        if not "convert_format" in filepath and not "simple_tx" in filepath and not "processing_time" in filepath and not "totaltime" in filepath and not ".py" in filepath:
            convert(filepath)



