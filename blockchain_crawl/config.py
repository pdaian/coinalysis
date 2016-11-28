RPC_USER = "bitcoinrpc"
RPC_PASSWORD = "wheetumblers"

BLOCK_START = 1
BLOCK_END = 30000 # latest block as of 12nov 1031 am
BLOCK_INTERVAL = 2000

DEBUG = True


from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def get_rpc():
    return AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(RPC_USER, RPC_PASSWORD))

