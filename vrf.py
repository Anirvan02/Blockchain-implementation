import hashlib
import ecdsa

def generate_key_pair():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def compute_vrf(private_key, participant_id):
    hashed_id = hashlib.sha256(participant_id.encode()).digest()

    vrf_output = private_key.sign(hashed_id)

    proof = vrf_output
    
    return vrf_output, proof

def verify_vrf(public_key, participant_id, vrf_output):
    hashed_id = hashlib.sha256(participant_id.encode()).digest()

    try:
        is_valid = public_key.verify(vrf_output, hashed_id)
        return is_valid
    except ecdsa.BadSignatureError:
        return False

def decentralized_lottery(participants):
    private_key, public_key = generate_key_pair()

    vrf_results = []
    for participant_id in participants:
        vrf_output, proof = compute_vrf(private_key, participant_id)
        vrf_results.append((participant_id, vrf_output, proof))

    winner = min(vrf_results, key=lambda x: x[1])

    is_verified = verify_vrf(public_key, winner[0], winner[1])
    
    if is_verified:
        print(f"The winner is: {winner[0]} with VRF: {winner[1]}")
        return winner[0]
    else:
        print("Winner verification failed!")
        return None

participants = ["Alice", "Bob", "Charlie", "Dave"]
winner = decentralized_lottery(participants)