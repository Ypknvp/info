import rsa
import hashlib

# Function to create a digital signature using RSA and SHA256
def create_digital_signature(message, private_key):
    # Hash the message with SHA256
    hashed_msg = hashlib.sha256(message.encode()).digest()
    return rsa.sign(hashed_msg, private_key, 'SHA-256')

# Function to verify the digital signature
def verify_digital_signature(message, signature, public_key):
    # Hash the message with SHA256
    hashed_msg = hashlib.sha256(message.encode()).digest()
    try:
        rsa.verify(hashed_msg, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Main driver code
if __name__ == "__main__":
    message = input("Enter message to sign: ")

    # Generate RSA keys (public and private)
    public_key, private_key = rsa.newkeys(2048)

    # Create digital signature
    signature = create_digital_signature(message, private_key)
    print(f"Signature Value:\n {signature.hex()}")

    # Verify the digital signature
    is_verified = verify_digital_signature(message, signature, public_key)
    print(f"Verification: {is_verified}")
