Coinalysis
==========

Suite for analyzing blockchain data for address-based linking of shared send
and centralized tumbler transactions.

Getting the Data
----------------

The first step to run Coinalysis is to download the blockchain data in its 
current form.  One way to do this is to run ``blockchain_crawl/crawl_blocks.py``
after creating a ``results`` folder in ``blockchain_crawl``.  Then, move the resulting result
subdirectories to ``final_analysis`` once processing is complete.

*An RPC-enabled Bitcoin node is required for this.*

A faster way is to download the data off an existing node (we provide one at http://162.248.4.26:5000)
and unzip the ~40GB of blockchain data in the ``final_analysis`` folder.

The format of each result subdirectory is as follows:

- totaltime : total time spent processing these blocks by the script (may not be accurate if multiple
    script executions generated file)
- 1 folder per block.  Each block folder has a ``simpletxs`` file, which has 
    [transaction],[output amount] for each simple transaction in the block, and a file named for 
    each transaction ID of all the complex transactions in the block

A *simple transaction* is defined as a transaction that has one input or two/one outputs (most
transactions feature a transfer and change address).

Complex transactions are formatted like:
```
#input
[address] [amount]

#output
[address] [amount]
```

for example:
```
#input
1LkhppoM81Ni5Hb2rd54iiKuDS7rGUvAYj 0.02053905
169R5TLxsZ4PttgBcQceE7U32yoyT8gmYc 0.0418
1HmCnepma2Yvz7pomzc5gmDxBgSoo9EXN5 0.7357

#output
1HxtTp8yJ4e7PDgv9XtMZ6jqdFgy9a6BMh 0.3255
1Bwsj9BQHjr4Pdr11HqYL84bS5xQeFpMLm 0.0194
1Cw1BXVQsxCyrDz7JeLXpkJ3wjVZvkKP7T 0.45303905
```

for a three input three output transaction.

The ``invalidinputs`` and ``invalidoutputs`` in the top level folder have lists of transaction IDs
where either the input or output was not parseable by the script (these transactions are also unable
to be decoded by block explorers like blockchain.info).


The Web Interface
-----------------

*An RPC-enabled Bitcoin node is required for this.*

The web interface is a script that allows you to input a transaction ID and view the possible
flow decompositions inside that coinjoin transaction.  An example instance is running at 
http://162.248.4.26:5000

To run the web interface, install Flask and run ``python run_webapp.py`` in the ``coinjoin`` directory.

Java is required for the backend graph partition worker.


Generating the Graphs
---------------------

Generating the graphs for analyzing the anonymity sets of centralized tumblers proceeds by running the
``gather_data.py`` file followed by the ``draw_graphs.py`` file in the graphs folder.  Move all Python
files in this folder to the top level transaction graph storage folder before running.


Note of Warning
---------------

This is a class project :).  Code is not intended to be optimized for maximum performance, readability,
maintainability, (...).  For example, the "parse_transaction" and "format_transaction" functions 
badly need refactoring, but are left as is because of technical debt we encountered about halfway 
through our data gathering.  Pull requests to add comments and tests are also always appreciated.
