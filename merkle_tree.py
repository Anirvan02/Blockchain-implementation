import hashlib

def compute_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

class MerkleNode:
    def __init__(self, left=None, right=None, data=None):
        if left is None and right is None:
            self.hash = compute_hash(data)
        else:
            self.hash = compute_hash(left.hash + right.hash)
        self.left = left
        self.right = right

def build_merkle_tree(data_blocks):
    leaf_nodes = [MerkleNode(data=data) for data in data_blocks]

    while len(leaf_nodes) > 1:
        temp_nodes = []
        for i in range(0, len(leaf_nodes), 2):
            left = leaf_nodes[i]
            right = leaf_nodes[i + 1] if i + 1 < len(leaf_nodes) else left
            parent = MerkleNode(left, right)
            temp_nodes.append(parent)
        leaf_nodes = temp_nodes

    return leaf_nodes[0]

def verify_block(root, data_block, data_blocks):
    original_root = build_merkle_tree(data_blocks)

    if original_root.hash == root.hash:
        print(f"Data block '{data_block}' is intact.")
    else:
        print(f"Data block '{data_block}' has been tampered with!")

def tamper_data_block(data_blocks, index, new_data):
    data_blocks[index] = new_data

data_blocks = ["Block 1", "Block 2", "Block 3", "Block 4"]

merkle_root = build_merkle_tree(data_blocks)

print(f"Merkle Root Hash: {merkle_root.hash}")

tamper_data_block(data_blocks, 1, "Tampered Block 2")
tamper_data_block(data_blocks, 3, "Tampered Block 4")

for i, data_block in enumerate(data_blocks):
    verify_block(merkle_root, data_block, ["Block 1", "Block 2", "Block 3", "Block 4"])