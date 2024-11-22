# Efficient power function to compute (a^b) % p
def power(a, b, p):
    result = 1
    a = a % p  # Ensure a is within the range of p
    while b > 0:
        # If b is odd, multiply result by a
        if b % 2 == 1:
            result = (result * a) % p
        # Reduce b by half and square a
        b = b // 2
        a = (a * a) % p
    return result

# Main function
def main():
    print("Welcome to the Diffie-Hellman Key Exchange Program!")
    print("Follow the prompts to generate shared secret keys.")

    # User inputs for the public keys P and G
    try:
        P = int(input("Enter a prime number P (e.g., 23): "))
        G = int(input("Enter a primitive root G for P (e.g., 9): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print("\nPublic values:")
    print(f"The value of P (prime number): {P}")
    print(f"The value of G (primitive root): {G}")

    # Alice chooses her private key a
    try:
        a = int(input("\nAlice, enter your private key a (a small positive integer): "))
        b = int(input("Bob, enter your private key b (a small positive integer): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print(f"\nThe private key a for Alice: {a}")
    print(f"The private key b for Bob: {b}")

    # Compute public keys
    x = power(G, a, P)  # Alice's public key
    y = power(G, b, P)  # Bob's public key

    print(f"\nComputed public keys:")
    print(f"Alice's public key (sent to Bob): {x}")
    print(f"Bob's public key (sent to Alice): {y}")

    # Generating the secret keys after exchanging public keys
    ka = power(y, a, P)  # Secret key for Alice
    kb = power(x, b, P)  # Secret key for Bob

    print("\nGenerated shared secret keys:")
    print(f"Secret key for Alice is: {ka}")
    print(f"Secret key for Bob is: {kb}")

    # Ensure the keys match
    if ka == kb:
        print("\nKey exchange successful! Both parties have the same secret key.")
    else:
        print("\nKey exchange failed. Secret keys do not match.")

if __name__ == "__main__":
    main()
23