import json

import eth

with open("daemons/abi/bep20.json") as f:
    BEP20_ABI = json.loads(f.read())

with open("daemons/tokens/bep20.json") as f:
    BEP20_TOKENS = json.loads(f.read())


class BNBDaemon(eth.ETHDaemon):
    name = "BNB"
    DEFAULT_PORT = 5006

    EIP1559_SUPPORTED = False
    DEFAULT_MAX_SYNC_BLOCKS = 300  # (60/3)=20*60 (a block every 3 seconds, keep up to 15 minutes of data)

    ABI = BEP20_ABI
    TOKENS = BEP20_TOKENS


if __name__ == "__main__":
    daemon = BNBDaemon()
    daemon.start()
