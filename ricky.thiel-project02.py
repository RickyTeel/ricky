import hashlib


def mine(minerName: str, D: int):
    if not isinstance(minerName, str) or not minerName:
        raise ValueError("minerName must be a non-empty string.")

    if not isinstance(D, int) or isinstance(D, bool) or not 1 <= D <= 4:
        raise ValueError("D must be an integer from 1 through 4.")

    nonce = 0
    target_prefix = "0" * D

    while True:
        coinbaseTx = f"Pay-{minerName}-3.125BTC-{nonce}"
        h = hashlib.sha256(coinbaseTx.encode("utf-8")).hexdigest()

        if h.startswith(target_prefix):
            return coinbaseTx, h

        nonce += 1


def main():
    minerName = "Ricky"
    D = 4

    coinbaseTx, h = mine(minerName, D)
    print("coinbaseTx =", coinbaseTx)
    print("h =", h)


if __name__ == "__main__":
    main()
