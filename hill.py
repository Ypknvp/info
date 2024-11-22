import numpy as np

def encrypt(message, key):
    keyMatrix = np.array([[ord(key[i * 3 + j]) % 65 for j in range(3)] for i in range(3)])
    messageVector = np.array([[ord(c) % 65] for c in message])
    cipherMatrix = np.dot(keyMatrix, messageVector) % 26
    return ''.join(chr(c + 65) for c in cipherMatrix.flatten())

def main():
    message, key = input("Enter 3-letter message: ").upper()[:3], input("Enter 9-letter key: ").upper()[:9]
    print("Ciphertext:", encrypt(message, key))

if __name__ == "__main__":
    main()
