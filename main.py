import hashlib
import datetime as date

# Define a class to represent a block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # Initialize a block with its index, timestamp, data, and the hash of the previous block
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the SHA-256 hash of the block's contents
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

# Define a class to represent the blockchain
class Blockchain:
    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block of the blockchain (genesis block) with default values
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    def add_block(self, new_block):
        # Add a new block to the blockchain
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        # Verify the integrity of the blockchain by checking the hashes
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Create the blockchain
blockchain = Blockchain()

# Get user input to add blocks to the blockchain
while True:
    # Prompt user to enter the data for the new block
    block_data = input("Enter data for the new block (type 'exit' to stop): ")
    if block_data.lower() == 'exit':
        break

    # Get the current block index
    index = len(blockchain.chain)

    # Add the new block with user input data
    blockchain.add_block(Block(index, date.datetime.now(), block_data, ""))

# Print the contents of the blockchain
for block in blockchain.chain:
    print("\n")
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)