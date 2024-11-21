import hashlib

class HashPointerNode:
    def __init__(self, data, prev_node=None):
        self.data = data
        self.prev_node = prev_node
        if prev_node:
            self.hash_pointer = self.compute_hash(prev_node)
        else:
            self.hash_pointer = None

    def compute_hash(self, prev_node):
        data_to_hash = str(prev_node.data) + str(prev_node.hash_pointer)
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

def create_linked_list():
    node1 = HashPointerNode("Node 1 data")
    node2 = HashPointerNode("Node 2 data", node1)
    node3 = HashPointerNode("Node 3 data", node2)
    node4 = HashPointerNode("Node 4 data", node3)
    node5 = HashPointerNode("Node 5 data", node4)
    
    return [node1, node2, node3, node4, node5]

def tamper_node(node, new_data):
    node.data = new_data

def verify_list(nodes):
    for i in range(1, len(nodes)):
        expected_hash = nodes[i].compute_hash(nodes[i - 1])
        if nodes[i].hash_pointer != expected_hash:
            print(f"Node {i + 1} has been tampered!")
        else:
            print(f"Node {i + 1} is intact.")

nodes = create_linked_list()

tamper_node(nodes[1], "Tampered Node 2 data")
tamper_node(nodes[3], "Tampered Node 4 data")

verify_list(nodes)