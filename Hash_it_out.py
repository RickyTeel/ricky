import hashlib


class MerkleNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def md5_hash(data):
        return hashlib.md5(data.encode()).hexdigest()


def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


def build_merkle_tree(transactions):
    if not transactions:
        return None

    current_level = [MerkleNode(tx) for tx in transactions]
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            combined = left.value + right.value
            parent_hash = md5_hash(combined)
            parent = MerkleNode(parent_hash, left, right)
            next_level.append(parent)
        current_level = next_level
    return current_level[0]


def get_merkle_root(transactions):
    root = build_merkle_tree(transactions)
    return root.value if root else None


def generate_proof(transactions, target_tx):
    if target_tx not in transactions:
        return None

    index = transactions.index(target_tx)
    current = transactions[:]
    proof = []
    current_index = index

    while len(current) > 1:
        sibling_index = current_index - 1 if current_index % 2 else current_index + 1
        if sibling_index >= len(current):
            sibling_index = current_index
        proof.append(current[sibling_index])

        next_level = []
        for i in range(0, len(current), 2):
            right = current[i + 1] if i + 1 < len(current) else current[i]
            next_level.append(md5_hash(current[i] + right))
        current = next_level
        current_index //= 2

    return proof


def main():
    n = int(input("Number of transactions (power of 2): "))
    transactions = [input(f"Transaction {i + 1}: ").strip() for i in range(n)]
    tx0 = input("Target transaction: ").strip()

    print("\n----- RESULTS -----")
    if tx0 in transactions:
        print("tx0 is in Tx.")
    else:
        print("tx0 is not in Tx.")

    print("Merkle Root:", get_merkle_root(transactions))
    proof = generate_proof(transactions, tx0)
    if proof:
        print("Merkle Proof Path:")
        for item in proof:
            print(item)
    else:
        print("Merkle proof path is not available.")


if __name__ == "__main__":
    main()
